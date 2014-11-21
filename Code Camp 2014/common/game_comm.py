#
# Don't change this file
#
import socket, errno, logging
from common.game_message import *
from common.object_message import *
from common.command_message import *
from common.event_message import *

WINDOWS_EAGAIN = 10035

ALL_MESSAGES = {}
ALL_MESSAGE_CODES = []
def setup_message_types():
    global ALL_MESSAGES
    global ALL_MESSAGE_CODES
    for k in GAME_MESSAGES:
        ALL_MESSAGES[k] = GAME_MESSAGES[k]
    for k in OBJECT_MESSAGES:
        ALL_MESSAGES[k] = OBJECT_MESSAGES[k]
    for k in COMMAND_MESSAGES:
        ALL_MESSAGES[k] = COMMAND_MESSAGES[k]
    for k in EVENT_MESSAGES:
        ALL_MESSAGES[k] = EVENT_MESSAGES[k]
    ALL_MESSAGE_CODES = ALL_MESSAGES.keys()
    return
setup_message_types()

####################################################################

E_0BYTES  = "0 Bytes Read"
E_BAD_CMD = "Bad Command"

class GameCommException(Exception):
    def __init__(self, msg):
        self.msg = msg
        return
        
    def is_0_bytes_read(self):
        return self.msg == E_0BYTES
        
    def is_bad_command(self):
        return self.msg == E_BAD_CMD
        
    def get_msg(self):
        return self.msg
        
    def __str__(self):
        return str(self.msg)
        
####################################################################        

class GameComm:

    def __init__(self, sock):
        self.logger = logging.getLogger('GameComm')
        self.ok = True
        self.sock = sock
        return

    def __nonzero__(self):
        return self.ok
        
    def _read_int(self):
        """skips whitespace, reads ascii digits, converts to int.  throws away first non-digit character after"""
        n = 0
        first = True
        while True:
            try:
                c = self.sock.recv(1)
                if len(c) == 0:
                    self.ok = False
                    raise GameCommException(E_0BYTES)
                    break
                if first and c.isspace():
                    continue
                elif c >= '0' and c <= '9':
                    n = n * 10 + ord(c) - ord('0')
                    first = False
                else:
                    break
            except socket.error as e:
                if e.errno == errno.EAGAIN or e.errno == WINDOWS_EAGAIN:
                    self.logger.warning("_read_int: %s", e.strerror)
                else:
                    raise e
        return n
        
    def _read_word(self):
        """skips whitespace, reads ascii characters, builds a string.  throws away first whitespace character after"""
        word = ""
        first = True
        while True:
            try:
                c = self.sock.recv(1)
                if len(c) == 0:
                    self.ok = False
                    raise GameCommException(E_0BYTES)
                    break
                if first and c.isspace():
                    continue
                elif (not first) and c.isspace():
                    break
                else:
                    word += c
                    first = False
            except socket.error as e:
                if e.errno == errno.EAGAIN or e.errno == WINDOWS_EAGAIN:
                    self.logger.warning("_read_word: %s", e.strerror)
                else:
                    raise e
        return word
        
    def _read_nbytes(self, n):
        """reads n bytes"""
        nread = 0
        msg = ""
        while n > nread:
            try:
                msg0 = self.sock.recv(n-nread)
                if len(msg0) == 0:
                    self.ok = False
                    raise GameCommException(E_0BYTES)
                    break
                nread += len(msg0)
                msg += msg0
            except socket.error as e:
                if e.errno == errno.EAGAIN or e.errno == WINDOWS_EAGAIN:
                    self.logger.warning("_read_nbytes: %s", e.strerror)
                else:
                    raise e
        self.logger.debug("'" + msg + "'" + str(len(msg)) + " " + str(n))
        return msg

    def read_mesg(self):
        """Reads one GameMessage object from the socket.
           Returns the object.
           On error, returns
             M_NONE if the GameComm has previously failed
             M_CLOSED if a 0 read occurs
             M_BAD_COMMAND if an unknown message type is received
        """
        try:
            msg = GameMessage()
            if not self.ok:
                return msg
            
            code = self._read_word()
            self.logger.debug('read_mesg: code: %s', code)
            size = self._read_int()
            self.logger.debug('read_mesg: size: %d', size)
            string = self._read_nbytes(size)
            self.logger.debug('read_mesg: string: %s', string)

            if code in ALL_MESSAGES:
                msg = ALL_MESSAGES[code](string)
                self.logger.info('read_mesg: msg: %s', msg)
            else:
                self.ok = False
                raise GameCommException(E_BAD_CMD + ":" + code)

            return msg
        except GameCommException as e:
            if e.is_0_bytes_read():
                msg = GameMessageClosed()
            elif e.is_bad_command():
                msg = GameMessageBadCommand()
            else:
                self.logger.error("Unexpected GameCommException: %s", e)
                raise e
        except socket.error as e:
            if e.errno == errno.EAGAIN or e.errno == WINDOWS_EAGAIN:
                self.logger.info("read_mesg: %s", e.strerror)
                msg = GameMessageEagain()
            else:
                self.logger.error("Unexpected socket.error: %s", e)
                raise e
                
        return msg

    def _write_mesg(self, code, size, text):
        string = "%s %d %s" % (code, size, text)
        self.sock.sendall(string)
        return
        
    def write_mesg(self, msg):
        try:
            if not self.ok:
                self.logger.error('write_mesg: self.ok = False')
                return False
            
            self.logger.info('write_mesg: msg: %s', msg)
            code = msg.get_command()
            
            if code in ALL_MESSAGE_CODES:
                # known command
                string = msg.to_string()
                size = len(string)
                self._write_mesg(code, size, string)
            else:
                self.ok = False
                raise GameCommException(E_BAD_CMD)

        except GameCommException as e:
            if e.is_bad_command():
                self.logger.error('write_mesg: bad command %s', code)
                return False
            else:
                self.logger.error('write_mesg: exception %s', e)
                raise e
                
        return True
        

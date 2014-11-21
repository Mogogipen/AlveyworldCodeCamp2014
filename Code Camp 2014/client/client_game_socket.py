#
# Don't change this file.
#
import socket, select, logging
from common.game_comm import *

class ClientGameSocket:
    """
    ClientGameSocket handles all socket communications
    from the client to the server.

    Methods:
    get_sock()                  : returns socket object 
    connect_to_server()         : connects to the configured server
    disconnect_from_server()    : disconnects from the server
    is_ready(fd)                : true if fd belongs to socket object
    send_messages(engine)       : sends all messages to game server, empties engine queue
    process_event(engine)       : receives one message from server, updates engine
    """

    def __init__(self, read_list, server_host="127.0.0.1", server_port=9999):
        self.logger = logging.getLogger('ClientGameSocket')
        self.logger.debug('__init__')
        self.read_list = read_list
        self.server_host = server_host
        self.server_port = server_port
        self.sock = None
        return

    def get_sock(self):
        return self.sock

    def connect_to_server(self):
        try:
            # build the socket to remote
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # connect to server
            self.sock.connect( (self.server_host, self.server_port) )
            # register for select
            self.read_list.append(self.sock.fileno())
            # make non-blocking so recv errors will trigger an exception
            self.sock.setblocking(0)
        except socket.error as e:
            self.logger.error("socket.error: %s", e)
            raise
        return

    def disconnect_from_server(self):
        try:
            if self.sock:
                # unregister from select
                if self.sock.fileno() in self.read_list:
                    self.read_list.remove(self.sock.fileno())
                # close socket
                self.sock.close()
                # remove reference
                self.sock = None
        except socket.error as e:
            self.logger.error("socket.error: %s", e)
            raise
        return

    def is_ready(self, fd):
        return self.sock and fd == self.sock.fileno()

    def send_messages(self, engine):
        if not engine: return
        try:
            gc = GameComm(self.sock)
            for msg in engine.get_message_queue():
                if not gc.write_mesg(msg):
                    self.logger.error("Error writing message: %s", msg)
            engine.clear_message_queue()
        except:
            self.logger.error("Error in send_messages.")
            raise
        return
        
    def process_event(self, engine):
        """Should not be called unless there is a message to read from the socket."""
        
        try:
            gc = GameComm(self.sock)
            msg = gc.read_mesg()
        except:
            raise
            
        code = msg.get_command()
        if code == M_ECHO:
            print msg.get_text()
        elif code == M_BROADCAST:
            print msg.get_text()
        elif code == M_CLOSED:
            print
            self.logger.info("Closing connection from server.")
            self.disconnect_from_server()
        elif code == M_EAGAIN:
            self.logger.info("Waiting to try again.")
        else:
            if engine:
                engine.process_server_message(msg)
        return


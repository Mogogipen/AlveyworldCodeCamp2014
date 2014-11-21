#
# Don't change this file
#
import json

####################################################################        

M_NONE           = "NONE"
M_ECHO           = "ECHO"
M_BROADCAST      = "BROADCAST"
M_LOGIN          = "LOGIN"
M_REQUEST_DUAL   = "REQUEST_DUAL"
M_WAIT_FOR_DUAL  = "WAIT_FOR_DUAL"
M_REQUEST_SINGLE = "REQUEST_SINGLE"
M_WAIT_FOR_SINGLE = "WAIT_FOR_SINGLE"
M_REQUEST_TOURNAMENT = "REQUEST_TOURNAMENT"
M_WAIT_FOR_TOURNAMENT = "WAIT_FOR_TOURNAMENT"
M_REQUEST_AI      = "REQUEST_AI"
M_WAIT_FOR_AI     = "WAIT_FOR_AI"
M_REQUEST_VIEW      = "REQUEST_VIEW"
M_WAIT_FOR_VIEW     = "WAIT_FOR_VIEW"
M_GAME_STARTING   = "GAME_STARTING"
M_GAME_OVER       = "GAME_OVER"
M_CLOSED         = "CLOSED"
M_BAD_COMMAND    = "BAD_COMMAND"
M_EAGAIN         = "EAGAIN"

####################################################################        
        
class GameMessage:

    def __init__(self, command=M_NONE):
        self.command = command
        self.data = {}
        return

    def get_command(self):
        return self.command

    def set_command(self, command):
        self.command = command
        return

    def set_data(self, key, value):
        self.data[key] = value
        return

    def get_data(self, key):
        if not key in self.data:
            return None
        return self.data[key]

    def to_string(self):
        return str(self)
        
    def from_string(self, string):
        tmp = json.loads(string)
        self.command = tmp['command']
        self.data = tmp['data']
        return

    def __str__(self):
        tmp = { 'command': self.command, 'data' : self.data }
        return json.dumps(tmp)

    def __repr__(self):
        return str(self)

class GameMessageEcho(GameMessage):

    def __init__(self):
        GameMessage.__init__(self, M_ECHO)
        self.set_text('')
        return
        
    def set_text(self, text):
        self.set_data('text', text)
        return
        
    def get_text(self):
        return self.get_data('text')
        
def string_to_echo_message(string):
    msg = GameMessageEcho()
    msg.from_string(string)
    return msg

class GameMessageBroadcast(GameMessage):

    def __init__(self):
        GameMessage.__init__(self, M_BROADCAST)
        self.set_text('')
        return
        
    def set_text(self, text):
        self.set_data('text', text)
        return
        
    def get_text(self):
        return self.get_data('text')
        
def string_to_broadcast_message(string):
    msg = GameMessageBroadcast()
    msg.from_string(string)
    return msg

class GameMessageLogin(GameMessage):

    def __init__(self):
        GameMessage.__init__(self, M_LOGIN)
        self.set_user('')          # user
        self.set_request(False)    # True if client->server request, False if server->client response
        self.set_result(False)     # If is response, True  if login successful, False otherwise
        return
        
    def set_user(self, user):
        self.set_data('user', user)
        return
        
    def get_user(self):
        return self.get_data('user')
        
    def set_request(self, value):
        self.set_data('request', value)
        return
        
    def get_request(self):
        return self.get_data('request')
        
    def set_result(self, value):
        self.set_data('result', value)
        return
        
    def get_result(self):
        return self.get_data('result')

def string_to_login_message(string):
    msg = GameMessageLogin()
    msg.from_string(string)
    return msg


class RequestDualMessage(GameMessage):
    def __init__(self):
        GameMessage.__init__(self, M_REQUEST_DUAL)
        return
        
def string_to_request_dual_message(string):
    msg = RequestDualMessage()
    msg.from_string(string)
    return msg
    
class WaitForDualMessage(GameMessage):
    def __init__(self):
        GameMessage.__init__(self, M_WAIT_FOR_DUAL)
        return
        
def string_to_wait_for_dual_message(string):
    msg = WaitForDualMessage()
    msg.from_string(string)
    return msg
    
class RequestSingleMessage(GameMessage):
    def __init__(self):
        GameMessage.__init__(self, M_REQUEST_SINGLE)
        return
        
def string_to_request_single_message(string):
    msg = RequestSingleMessage()
    msg.from_string(string)
    return msg

class WaitForSingleMessage(GameMessage):
    def __init__(self):
        GameMessage.__init__(self, M_WAIT_FOR_SINGLE)
        return
        
def string_to_wait_for_single_message(string):
    msg = WaitForSingleMessage()
    msg.from_string(string)
    return msg
    
class RequestTournamentMessage(GameMessage):
    def __init__(self):
        GameMessage.__init__(self, M_REQUEST_TOURNAMENT)
        return
        
def string_to_request_tournament_message(string):
    msg = RequestTournamentMessage()
    msg.from_string(string)
    return msg

class WaitForTournamentMessage(GameMessage):
    def __init__(self):
        GameMessage.__init__(self, M_WAIT_FOR_TOURNAMENT)
        return
        
def string_to_wait_for_tournament_message(string):
    msg = WaitForTournamentMessage()
    msg.from_string(string)
    return msg
    
class RequestAiMessage(GameMessage):
    def __init__(self):
        GameMessage.__init__(self, M_REQUEST_AI)
        return
        
def string_to_request_ai_message(string):
    msg = RequestAiMessage()
    msg.from_string(string)
    return msg

class WaitForAiMessage(GameMessage):
    def __init__(self):
        GameMessage.__init__(self, M_WAIT_FOR_AI)
        return
        
def string_to_wait_for_ai_message(string):
    msg = WaitForAiMessage()
    msg.from_string(string)
    return msg
    
class RequestViewMessage(GameMessage):
    def __init__(self):
        GameMessage.__init__(self, M_REQUEST_VIEW)
        return
        
def string_to_request_view_message(string):
    msg = RequestViewMessage()
    msg.from_string(string)
    return msg

class WaitForViewMessage(GameMessage):
    def __init__(self):
        GameMessage.__init__(self, M_WAIT_FOR_VIEW)
        return
        
def string_to_wait_for_view_message(string):
    msg = WaitForViewMessage()
    msg.from_string(string)
    return msg
    
class GameStartingMessage(GameMessage):
    def __init__(self, oname=""):
        GameMessage.__init__(self, M_GAME_STARTING)
        self.set_opponent_name(oname)
        return
    def set_opponent_name(self, oname):
        self.set_data('opponent_name', oname)
        return
    def get_opponent_name(self):
        return self.get_data('opponent_name')
        
def string_to_game_starting_message(string):
    msg = GameStartingMessage()
    msg.from_string(string)
    return msg
    
    
class GameOverMessage(GameMessage):
    def __init__(self, wname=""):
        GameMessage.__init__(self, M_GAME_OVER)
        self.set_winner_name(wname)
        return
    def set_winner_name(self, wname=""):
        self.set_data('winner_name', wname)
        return
    def get_winner_name(self):
        return self.get_data('winner_name')
        
def string_to_game_over_message(string):
    msg = GameOverMessage()
    msg.from_string(string)
    return msg
    
    
class GameMessageClosed(GameMessage):
    def __init__(self):
        GameMessage.__init__(self, M_CLOSED)
        return

class GameMessageBadCommand(GameMessage):
    def __init__(self):
        GameMessage.__init__(self, M_BAD_COMMAND)
        return
        
class GameMessageEagain(GameMessage):
    def __init__(self):
        GameMessage.__init__(self, M_EAGAIN)
        return

GAME_MESSAGES = { M_ECHO:            string_to_echo_message,
                  M_BROADCAST:       string_to_broadcast_message,
                  M_LOGIN:           string_to_login_message,
                  M_REQUEST_DUAL:    string_to_request_dual_message,
                  M_WAIT_FOR_DUAL:   string_to_wait_for_dual_message,
                  M_REQUEST_SINGLE:  string_to_request_single_message, 
                  M_WAIT_FOR_SINGLE: string_to_wait_for_single_message, 
                  M_REQUEST_TOURNAMENT:  string_to_request_tournament_message, 
                  M_WAIT_FOR_TOURNAMENT: string_to_wait_for_tournament_message, 
                  M_REQUEST_AI:      string_to_request_ai_message, 
                  M_WAIT_FOR_AI:     string_to_wait_for_ai_message, 
                  M_REQUEST_VIEW:    string_to_request_view_message, 
                  M_WAIT_FOR_VIEW:   string_to_wait_for_view_message, 
                  M_GAME_STARTING:   string_to_game_starting_message,
                  M_GAME_OVER:       string_to_game_over_message, }


#
# Don't change this file
#
GAME_STATE_NONE = 0
GAME_STATE_LOGGING_IN = 1
GAME_STATE_LOGGED_IN = 2
GAME_STATE_WAITING_FOR_DUAL = 3
GAME_STATE_WAITING_FOR_SINGLE = 4
GAME_STATE_WAITING_FOR_AI = 5
GAME_STATE_STARTED = 6
GAME_STATE_OVER = 7
GAME_STATE_WAITING_FOR_TOURNAMENT = 8
GAME_STATE_WAITING_FOR_VIEW = 9

class GameData:

    def __init__(self):
        self.objects = {}
        self.game_state = GAME_STATE_NONE
        self.name = ""
        self.opponent_name = ""
        self.winner_name = ""
        return

    # game states
    def set_logging_in(self):
        self.game_state = GAME_STATE_LOGGING_IN
        return
    def set_logged_in(self):
        self.game_state = GAME_STATE_LOGGED_IN
        return
    def set_waiting_for_dual(self):
        self.game_state = GAME_STATE_WAITING_FOR_DUAL
        return
    def set_waiting_for_single(self):
        self.game_state = GAME_STATE_WAITING_FOR_SINGLE
        return
    def set_waiting_for_tournament(self):
        self.game_state = GAME_STATE_WAITING_FOR_TOURNAMENT
        return
    def set_waiting_for_ai(self):
        self.game_state = GAME_STATE_WAITING_FOR_AI
        return
    def set_waiting_for_view(self):
        self.game_state = GAME_STATE_WAITING_FOR_VIEW
        return
    def set_game_started(self):
        self.game_state = GAME_STATE_STARTED
        return
    def set_game_over(self):
        self.game_state = GAME_STATE_OVER
        return
    # other parameters
    def set_name(self, name):
        self.name = name
        return
    def set_opponent_name(self, oname):
        self.opponent_name = oname
        return
    def set_winner_name(self, wname):
        self.winner_name = wname
        return

    # game states
    def get_logging_in(self):
        return self.game_state == GAME_STATE_LOGGING_IN
    def get_logged_in(self):
        return self.game_state == GAME_STATE_LOGGED_IN
    def get_waiting_for_dual(self):
        return self.game_state == GAME_STATE_WAITING_FOR_DUAL
    def get_waiting_for_single(self):
        return self.game_state == GAME_STATE_WAITING_FOR_SINGLE
    def get_waiting_for_tournament(self):
        return self.game_state == GAME_STATE_WAITING_FOR_TOURNAMENT
    def get_waiting_for_ai(self):
        return self.game_state == GAME_STATE_WAITING_FOR_AI
    def get_waiting_for_view(self):
        return self.game_state == GAME_STATE_WAITING_FOR_VIEW
    def get_game_started(self):
        return self.game_state == GAME_STATE_STARTED
    def get_game_over(self):
        return self.game_state == GAME_STATE_OVER
    # other parameters
    def get_name(self):
        return self.name
    def get_opponent_name(self):
        return self.opponent_name
    def get_winner_name(self):
        return self.winner_name

    # game objects
    def get_object(self, oid):
        if oid in self.objects:
            return self.objects[oid]
        return None
        
    def get_objects(self):
        return self.objects
        
    def update_object(self, obj):
        oid = obj.get_oid()
        self.objects[oid] = obj
        if obj.is_dead():
            del self.objects[oid]
        return
    
    def remove_object(self, obj):
        oid = obj.get_oid()
        del self.objects[oid]
        return

    def __str__(self):
        s = "GameData: "
        for oid in self.objects:
            s += "\n\t"
            s += str(self.objects[oid])
        return s

    def __repr__(self):
        return str(self)
        

        

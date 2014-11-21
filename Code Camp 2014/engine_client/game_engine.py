#
# Don't change this file
#

# Information methods on the game engine:
#   get_player_oid() return the object id of your player
#   get_opponent_oid()  return the object id of your opponent
#   get_data() return the game data object 
#   get_name() return your display name
#   get_opponent_name() return your opponent's display name
#   get_winner_name() return the winner's name, if there is a winner
#   get_object(oid) return the object identified by oid
#   get_objects() return the dictionary of all objects


# Action methods on the game engine:
#  Movement speed:
#    set_player_speed_stop() stop moving
#    set_player_speed_slow() move slowly, if enough mana
#    set_player_speed_medium() move medium, if enough mana, and enough experience
#    set_player_speed_fast() move fast, if enough mana, and enough experience
#  Movement direction:
#    set_player_direction(degrees) specify the direction to move, when you are not stopped
#  Missile range:
#    set_missile_range_none() disable missiles
#    set_missile_range_short() shoot short range, at next fire
#    set_missile_range_medium() shoot medium range, at next fire, if enough experience
#    set_missile_range_long() shoot long range, at next fire, if enough experience
#  Missile power:
#    set_missile_power_none() disable missiles
#    set_missile_power_low() shoot low power, at next fire
#    set_missile_power_medium() shoot medium power, at next fire, if enough experience
#    set_missile_power_high() shoot high power, at next fire, if enough experience
#  Missile direction:
#    set_missile_direction(degrees) specify the direction to fire, at next fire
#  Missile fire:
#    fire_missile() fire a missile, if enough mana for range and power combination
# 
# 

import logging
from common.game import GameData
from common.object_message import message_to_object
from common.event_message import message_to_event
from common.command_message import *
from common.game_message import *

MODE_DUAL = 1
MODE_SINGLE = 2
MODE_AI = 3
MODE_TOURNAMENT = 4
MODE_VIEW = 5

class ClientGameEngine:
    """
    Stores game information for client.
    Provides game actions client can take.
    Provides server->client message processing.
    Provides client->server message creation.
    """

    #########################
    #
    # Internal methods that should not be exposed
    # to the client.
    #
    def __init__(self, name, desired_mode=MODE_DUAL):
        self.logger = logging.getLogger('ClientGameEngine')
        self.logger.debug('__init__')
        self.desired_mode = desired_mode
        self.new_game(name)
        return

    def new_game(self, name):
        self.logger.debug('new_game')
        self.data = GameData()
        self.data.set_name(name)
        self.player_oid = -1
        self.opponent_oid = -1
        self.message_queue = []
        self.event_queue = []
        msg = GameMessageLogin()
        msg.set_user(self.data.get_name())
        msg.set_request(True)
        self.add_message(msg)
        return

    def add_message(self, msg):
        self.message_queue.append(msg)
        return

    def get_message_queue(self):
        return self.message_queue
        
    def clear_message_queue(self):
        self.message_queue = []
        return

    def add_event(self, event):
        self.event_queue.append(event)
        return
        
    def get_event_queue(self):
        return self.event_queue
        
    def clear_event_queue(self):
        self.event_queue = []
        return

    def process_server_message(self, msg):
        """
        Handles object update messages.
        Other message types should be handled as well.
        """
        self.logger.debug('process_server_message')
        obj = message_to_object(msg)
        event = message_to_event(msg)
        if obj is not None:
            self.logger.info('update_object:(%s)', obj)
            self.data.update_object(obj)
            if (self.player_oid > 0 and
                self.opponent_oid < 0 and
                obj.is_player() and
                self.player_oid != obj.get_oid()):
                self.opponent_oid = obj.get_oid()
            if obj.is_dead() and obj.is_player():
                if obj.get_oid() == self.opponent_oid:
                    self.opponent_oid = -1
                elif obj.get_oid() == self.player_oid:
                    self.player_oid = -1
        elif event is not None:
            self.logger.info('event:(%s)', event)
            self.add_event(event)
        else:
            code = msg.get_command()
            if code == M_PLAYER_OID:
                self.player_oid = msg.get_oid()
            elif code == M_LOGIN:
                if (not msg.get_request()) and msg.get_result():
                    self.data.set_logged_in()
                    if self.desired_mode == MODE_DUAL:
                        self.add_message(RequestDualMessage())
                    elif self.desired_mode == MODE_SINGLE:
                        self.add_message(RequestSingleMessage())
                    elif self.desired_mode == MODE_TOURNAMENT:
                        self.add_message(RequestTournamentMessage())
                    elif self.desired_mode == MODE_AI:
                        self.add_message(RequestAiMessage())
                    elif self.desired_mode == MODE_VIEW:
                        self.add_message(RequestViewMessage())
                    else:
                        self.logger.error("Unknown mode: %d", self.desired_mode)
            elif code == M_WAIT_FOR_DUAL:
                self.data.set_waiting_for_dual()
            elif code == M_WAIT_FOR_SINGLE:
                self.data.set_waiting_for_single()
            elif code == M_WAIT_FOR_TOURNAMENT:
                self.data.set_waiting_for_tournament()
            elif code == M_WAIT_FOR_AI:
                self.data.set_waiting_for_ai()
            elif code == M_WAIT_FOR_VIEW:
                self.data.set_waiting_for_view()
            elif code == M_GAME_STARTING:
                self.data.set_game_started()
                self.data.set_opponent_name(msg.get_opponent_name())
                self.add_message(RequestPlayerOidMessage())
            elif code == M_GAME_OVER:
                self.data.set_game_over()
                self.data.set_winner_name(msg.get_winner_name())
            else:
                self.logger.error("Unknown message type: %s", msg)
        return

    def __str__(self):
        return "ClientGameEngine(%d):\n%s" % (self.player_oid, self.data)

    #########################
    #
    # External methods for the client to use
    #
        
    #
    # Game Information Methods
    #
    def get_player_oid(self):
        return self.player_oid
    def get_opponent_oid(self):
        return self.opponent_oid
    def get_data(self):
        return self.data
    def get_name(self):
        return self.data.get_name()
    def get_opponent_name(self):
        return self.data.get_opponent_name()
    def get_winner_name(self):
        return self.data.get_winner_name()
    def get_object(self, oid):
        return self.data.get_object(oid)
    def get_objects(self):
        return self.data.get_objects()

    #
    # Game Action Methods
    #
    
    # move speed
    def set_player_speed_stop(self):
        self.add_message(SetPlayerSpeedMessage(T_SPEED_STOP))
        return
    def set_player_speed_slow(self):
        self.add_message(SetPlayerSpeedMessage(T_SPEED_SLOW))
        return
    def set_player_speed_medium(self):
        self.add_message(SetPlayerSpeedMessage(T_SPEED_MEDIUM))
        return
    def set_player_speed_fast(self):
        self.add_message(SetPlayerSpeedMessage(T_SPEED_FAST))
        return
        
    # move direction
    def set_player_direction(self, degrees):
        self.add_message(SetPlayerDirectionMessage(degrees))
        return

    # missile range
    def set_missile_range_none(self):
        self.add_message(SetMissileRangeMessage(T_RANGE_NONE))
        return
    def set_missile_range_short(self):
        self.add_message(SetMissileRangeMessage(T_RANGE_SHORT))
        return
    def set_missile_range_medium(self):
        self.add_message(SetMissileRangeMessage(T_RANGE_MEDIUM))
        return
    def set_missile_range_long(self):
        self.add_message(SetMissileRangeMessage(T_RANGE_LONG))
        return
        
    # missile direction
    def set_missile_direction(self, degrees):
        self.add_message(SetMissileDirectionMessage(degrees))
        return
        
    # missile power
    def set_missile_power_none(self):
        self.add_message(SetMissilePowerMessage(T_POWER_NONE))
        return
    def set_missile_power_low(self):
        self.add_message(SetMissilePowerMessage(T_POWER_LOW))
        return
    def set_missile_power_medium(self):
        self.add_message(SetMissilePowerMessage(T_POWER_MEDIUM))
        return
    def set_missile_power_high(self):
        self.add_message(SetMissilePowerMessage(T_POWER_HIGH))
        return
        
    # fire missile
    def fire_missile(self):
        self.add_message(FireMissileMessage())
        return

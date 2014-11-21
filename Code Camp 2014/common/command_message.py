#
# Don't change this file
#
from common.game_message import GameMessage

#
# client->server commands
#
M_REQUEST_PLAYER_OID   = "REQUEST_PLAYER_OID"
M_SET_PLAYER_SPEED     = "SET_PLAYER_SPEED"
M_SET_PLAYER_DIRECTION = "SET_PLAYER_DIRECTION"

M_SET_MISSILE_RANGE     = "SET_MISSILE_RANGE"
M_SET_MISSILE_DIRECTION = "SET_MISSILE_DIRECTION"
M_SET_MISSILE_POWER     = "SET_MISSILE_POWER"
M_FIRE_MISSILE          = "FIRE_MISSILE"

T_SPEED_STOP   = "SPEED_STOP"
T_SPEED_SLOW   = "SPEED_SLOW"
T_SPEED_MEDIUM = "SPEED_MEDIUM"
T_SPEED_FAST   = "SPEED_FAST"

T_RANGE_NONE    = "RANGE_NONE"
T_RANGE_SHORT   = "RANGE_SHORT"
T_RANGE_MEDIUM  = "RANGE_MEDIUM"
T_RANGE_LONG    = "RANGE_LONG"

T_POWER_NONE    = "POWER_NONE"
T_POWER_LOW     = "POWER_LOW"
T_POWER_MEDIUM  = "POWER_MEDIUM"
T_POWER_HIGH    = "POWER_HIGH"

class RequestPlayerOidMessage(GameMessage):
    def __init__(self):
        GameMessage.__init__(self, M_REQUEST_PLAYER_OID)
        return
        
def string_to_request_player_oid_message(string):
    msg = RequestPlayerOidMessage()
    msg.from_string(string)
    return msg

class SetPlayerSpeedMessage(GameMessage):
    def __init__(self, speed=T_SPEED_STOP):
        GameMessage.__init__(self, M_SET_PLAYER_SPEED)
        self.set_speed(speed)
        return
    def set_speed(self, speed=T_SPEED_STOP):
        self.set_data("speed", speed)
        return
    def get_speed(self):
        return self.get_data("speed")
        
def string_to_set_player_speed_message(string):
    msg = SetPlayerSpeedMessage()
    msg.from_string(string)
    return msg

        
class SetPlayerDirectionMessage(GameMessage):
    def __init__(self, degrees=0.):
        GameMessage.__init__(self, M_SET_PLAYER_DIRECTION)
        self.set_degrees(degrees)
        return
    def set_degrees(self, degrees=0.):
        self.set_data("degrees", degrees)
        return
    def get_degrees(self):
        return self.get_data("degrees")

def string_to_set_player_direction_message(string):
    msg = SetPlayerDirectionMessage()
    msg.from_string(string)
    return msg

class SetMissileRangeMessage(GameMessage):
    def __init__(self, mrange=T_RANGE_SHORT):
        GameMessage.__init__(self, M_SET_MISSILE_RANGE)
        self.set_range(mrange)
        return
    def set_range(self, mrange=T_RANGE_SHORT):
        self.set_data("range", mrange)
        return
    def get_range(self):
        return self.get_data("range")
        
def string_to_set_missile_range_message(string):
    msg = SetMissileRangeMessage()
    msg.from_string(string)
    return msg

class SetMissileDirectionMessage(GameMessage):
    def __init__(self, degrees=0.):
        GameMessage.__init__(self, M_SET_MISSILE_DIRECTION)
        self.set_degrees(degrees)
        return
    def set_degrees(self, degrees=0.):
        self.set_data("degrees", degrees)
        return
    def get_degrees(self):
        return self.get_data("degrees")

def string_to_set_missile_direction_message(string):
    msg = SetMissileDirectionMessage()
    msg.from_string(string)
    return msg

class SetMissilePowerMessage(GameMessage):
    def __init__(self, power=T_POWER_LOW):
        GameMessage.__init__(self, M_SET_MISSILE_POWER)
        self.set_power(power)
        return
    def set_power(self, power=T_POWER_LOW):
        self.set_data("power", power)
        return
    def get_power(self):
        return self.get_data("power")
        
def string_to_set_missile_power_message(string):
    msg = SetMissilePowerMessage()
    msg.from_string(string)
    return msg

class FireMissileMessage(GameMessage):
    def __init__(self):
        GameMessage.__init__(self, M_FIRE_MISSILE)
        return

def string_to_fire_missile_message(string):
    msg = FireMissileMessage()
    msg.from_string(string)
    return msg
        
        
#
# server->client commands
#
M_PLAYER_OID = "PLAYER_OID"

class PlayerOidMessage(GameMessage):
    def __init__(self, oid=-1):
        GameMessage.__init__(self, M_PLAYER_OID)
        self.set_oid(oid)
        return
    def set_oid(self, oid=-1):
        self.set_data("oid", oid)
        return
    def get_oid(self):
        return self.get_data("oid")
        
def string_to_player_oid_message(string):
    msg = PlayerOidMessage()
    msg.from_string(string)
    return msg

        
# 
COMMAND_MESSAGES = { M_REQUEST_PLAYER_OID:    string_to_request_player_oid_message,
                     M_SET_PLAYER_SPEED:      string_to_set_player_speed_message,
                     M_SET_PLAYER_DIRECTION:  string_to_set_player_direction_message,
                     M_SET_MISSILE_RANGE:     string_to_set_missile_range_message,
                     M_SET_MISSILE_DIRECTION: string_to_set_missile_direction_message,
                     M_SET_MISSILE_POWER:     string_to_set_missile_power_message,
                     M_FIRE_MISSILE:          string_to_fire_missile_message,
                     M_PLAYER_OID:            string_to_player_oid_message }


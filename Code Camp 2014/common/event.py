#
# Don't change this file
#

#
# Event types and the methods for each:
# MISSILE_FIRE - when a missile is fired
#   get_player_oid() returns the object id of the player that shot the missile
#   get_missile_oid() returns the object id of the missile that was fired
#   get_missile_range() returns the range of the missile that was fired
#   get_missile_power() returns the power of the missile that was fired
# MISSILE_MISFIRE - when a player tries to fire but doesn't have enough mana
#   get_player_oid() returns the object id of the player that tried to fire the missile
# MISSILE_HIT - when a missile hits something
#   get_player_oid() returns the object id of the player that shot the missile
#   get_missile_oid() returns the object id of the missile that hit something
#   get_target_oid() returns the object id of the object hit by the missile
# MISSILE_DYING - when a missile hits its maximum range and begins dying
#   get_player_oid() returns the object id of the player that shot the dying missile
#   get_missile_oid() returns the object id of the missile that is dying


import json

E_NONE = "NONE"
E_MISSILE_FIRE = "MISSILE_FIRE"
E_MISSILE_MISFIRE = "MISSILE_MISFIRE"
E_MISSILE_HIT = "MISSILE_HIT"
E_MISSILE_DYING = "MISSILE_DYING"
    
class Event:
    def __init__(self, kind=E_NONE):
        self.data = { }
        self.set_data('kind', kind)
        return

    def set_message(self, msg):
        for k in self.data:
            msg.set_data(k, self.data[k])
        return

    def set_from_message(self, msg):
        for k in msg.data:
            self.set_data(k, msg.get_data(k))
        return

    def get_kind(self):
        return self.get_data('kind')
        
    def set_kind(self, kind):
        self.set_data('kind', kind)
        return
        
    def set_data(self, key, value):
        self.data[key] = value
        return

    def get_data(self, key):
        if not key in self.data:
            return None
        return self.data[key]

    def __str__(self):
        tmp = { 'kind': self.get_kind(), 'data' : self.data }
        return json.dumps(tmp)

    def __repr__(self):
        return str(self)
        

class MissileFireEvent(Event):
    def __init__(self, player_oid=None, missile_oid=None, missile_range=None, missile_power=None):
        Event.__init__(self, E_MISSILE_FIRE)
        self.set_player_oid(player_oid)
        self.set_missile_oid(missile_oid)
        self.set_missile_range(missile_range)
        self.set_missile_power(missile_power)
        return
    def set_player_oid(self, player_oid=None):
        self.set_data("player_oid", player_oid)
        return
    def set_missile_oid(self, missile_oid=None):
        self.set_data("missile_oid", missile_oid)
        return
    def set_missile_range(self, missile_range=None):
        self.set_data("missile_range", missile_range)
        return
    def set_missile_power(self, missile_power=None):
        self.set_data("missile_power", missile_power)
        return
    def get_player_oid(self):
        return self.get_data("player_oid")
    def get_missile_oid(self):
        return self.get_data("missile_oid")
    def get_missile_range(self):
        return self.get_data("missile_range")
    def get_missile_power(self):
        return self.get_data("missile_power")

class MissileMisfireEvent(Event):
    def __init__(self, player_oid=None):
        Event.__init__(self, E_MISSILE_MISFIRE)
        self.set_player_oid(player_oid)
        return
    def set_player_oid(self, player_oid=None):
        self.set_data("player_oid", player_oid)
        return
    def get_player_oid(self):
        return self.get_data("player_oid")

class MissileHitEvent(Event):
    def __init__(self, player_oid=None, missile_oid=None, target_oid=None):
        Event.__init__(self, E_MISSILE_HIT)
        self.set_player_oid(player_oid)
        self.set_missile_oid(missile_oid)
        self.set_target_oid(target_oid)
        return
    def set_player_oid(self, player_oid=None):
        self.set_data("player_oid", player_oid)
        return
    def set_missile_oid(self, missile_oid=None):
        self.set_data("missile_oid", missile_oid)
        return
    def set_target_oid(self, target_oid=None):
        self.set_data("target_oid", target_oid)
        return
    def get_player_oid(self):
        return self.get_data("player_oid")
    def get_missile_oid(self):
        return self.get_data("missile_oid")
    def get_target_oid(self):
        return self.get_data("target_oid")

class MissileDyingEvent(Event):
    def __init__(self, player_oid=None, missile_oid=None):
        Event.__init__(self, E_MISSILE_DYING)
        self.set_player_oid(player_oid)
        self.set_missile_oid(missile_oid)
        return
    def set_player_oid(self, player_oid=None):
        self.set_data("player_oid", player_oid)
        return
    def set_missile_oid(self, missile_oid=None):
        self.set_data("missile_oid", missile_oid)
        return
    def get_player_oid(self):
        return self.get_data("player_oid")
    def get_missile_oid(self):
        return self.get_data("missile_oid")

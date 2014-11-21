#
# Don't change this file
#

# Information methods in the MissileData class
# get_range() how far it is able to travel
# get_power() how much damage it will cause
# get_player_oid() which player launched it
# get_hit_max_range() true if it traveled maximum range

from object import ObjectData
class MissileData(ObjectData):
    """
    All data associated with game Missile objects
    """

    def __init__(self, x=0, y=0, w=0, h=0, player_oid=-1):
        ObjectData.__init__(self, x, y, w, h)
        self.range = 0.0  # distance to travel
        self.power = 0.0  # damage caused
        self.player_oid = player_oid # player that shot this missile
        self.hit_max_range = False # True if died because traveled maximum distance without hitting anything
        return

    def set_message(self, msg):
        ObjectData.set_message(self, msg)
        msg.set_data('range', self.get_range())
        msg.set_data('power', self.get_power())
        msg.set_data('player_oid', self.get_player_oid())
        msg.set_data('hit_max_range', self.get_hit_max_range())
        return
        
    def set_from_message(self, msg):
        ObjectData.set_from_message(self, msg)
        self.set_range(msg.get_data('range'))
        self.set_power(msg.get_data('power'))
        self.set_player_oid(msg.get_data('player_oid'))
        self.set_hit_max_range(msg.get_data('hit_max_range'))
        return

    def get_range(self):
        return self.range

    def set_range(self, range):
        self.range = float(range)
        return
        
    def get_power(self):
        return self.power

    def set_power(self, power):
        self.power = float(power)
        return
        
    def get_player_oid(self):
        return self.player_oid

    def set_player_oid(self, player_oid):
        self.player_oid = player_oid
        return
        
    def get_hit_max_range(self):
        return self.hit_max_range

    def set_hit_max_range(self, hit_max_range):
        self.hit_max_range = hit_max_range
        return

    def is_missile(self):
        return True
    

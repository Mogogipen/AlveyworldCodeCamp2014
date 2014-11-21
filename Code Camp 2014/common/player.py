#
# Don't change this file
#

# Information methods available for all PlayerData objects
# get_experience()
# get_missile_range()
# get_missile_dx()
# get_missile_dy()
# get_missile_power()
# get_missile_mana()
# get_missile_mana_recharge_rate()
# get_missile_mana_max()
# get_move_mana()
# get_move_mana_recharge_rate()
# get_move_mana_max()

from object import ObjectData
class PlayerData(ObjectData):
    """
    All data associated with game Player objects
    """

    def __init__(self, x=0, y=0, w=0, h=0):
        ObjectData.__init__(self, x, y, w, h)
        self.experience = 0.0
        self.missile_range = 0.0
        self.missile_dx = 0.0
        self.missile_dy = 0.0
        self.missile_power = 0.0
        self.missile_mana = 0.0
        self.missile_mana_recharge_rate = 0.0
        self.missile_mana_max = 0.0
        self.move_mana = 0.0
        self.move_mana_recharge_rate = 0.0
        self.move_mana_max = 0.0
        return

    def set_message(self, msg):
        ObjectData.set_message(self, msg)
        msg.set_data('experience', self.get_experience())
        msg.set_data('missile_range', self.get_missile_range())
        msg.set_data('missile_dx', self.get_missile_dx())
        msg.set_data('missile_dy', self.get_missile_dy())
        msg.set_data('missile_power', self.get_missile_power())
        msg.set_data('missile_mana', self.get_missile_mana())
        msg.set_data('missile_mana_recharge_rate', self.get_missile_mana_recharge_rate())
        msg.set_data('missile_mana_max', self.get_missile_mana_max())
        msg.set_data('move_mana', self.get_move_mana())
        msg.set_data('move_mana_recharge_rate', self.get_move_mana_recharge_rate())
        msg.set_data('move_mana_max', self.get_move_mana_max())
        return
        
    def set_from_message(self, msg):
        ObjectData.set_from_message(self, msg)
        self.set_experience(msg.get_data('experience'))
        self.set_missile_range(msg.get_data('missile_range'))
        self.set_missile_dx(msg.get_data('missile_dx'))
        self.set_missile_dy(msg.get_data('missile_dy'))
        self.set_missile_power(msg.get_data('missile_power'))
        self.set_missile_mana(msg.get_data('missile_mana'))
        self.set_missile_mana_recharge_rate(msg.get_data('missile_mana_recharge_rate'))
        self.set_missile_mana_max(msg.get_data('missile_mana_max'))
        self.set_move_mana(msg.get_data('move_mana'))
        self.set_move_mana_recharge_rate(msg.get_data('move_mana_recharge_rate'))
        self.set_move_mana_max(msg.get_data('move_mana_max'))
        return
        
    def get_experience(self):
        return self.experience

    def set_experience(self, experience):
        self.experience = float(experience)
        return

    def add_experience(self, new_experience):
        self.experience += new_experience
        return
        
    def get_missile_range(self):
        return self.missile_range

    def set_missile_range(self, mrange):
        self.missile_range = float(mrange)
        return
        
    def get_missile_dx(self):
        return self.missile_dx

    def set_missile_dx(self, dx):
        self.missile_dx = float(dx)
        return
        
    def get_missile_dy(self):
        return self.missile_dy

    def set_missile_dy(self, dy):
        self.missile_dy = float(dy)
        return

    def get_missile_power(self):
        return self.missile_power

    def set_missile_power(self, power):
        self.missile_power = float(power)
        return

    def get_missile_mana(self):
        return self.missile_mana

    def set_missile_mana(self, mana):
        self.missile_mana = float(mana)
        return
        
    def get_missile_mana_recharge_rate(self):
        return self.missile_mana_recharge_rate

    def set_missile_mana_recharge_rate(self, mana_recharge_rate):
        self.missile_mana_recharge_rate = float(mana_recharge_rate)
        return
        
    def get_missile_mana_max(self):
        return self.missile_mana_max

    def set_missile_mana_max(self, mana_max):
        self.missile_mana_max = float(mana_max)
        return

    def get_move_mana(self):
        return self.move_mana

    def set_move_mana(self, mana):
        self.move_mana = float(mana)
        return
        
    def get_move_mana_recharge_rate(self):
        return self.move_mana_recharge_rate

    def set_move_mana_recharge_rate(self, mana_recharge_rate):
        self.move_mana_recharge_rate = float(mana_recharge_rate)
        return
        
    def get_move_mana_max(self):
        return self.move_mana_max

    def set_move_mana_max(self, mana_max):
        self.move_mana_max = float(mana_max)
        return

    def is_player(self):
        return True


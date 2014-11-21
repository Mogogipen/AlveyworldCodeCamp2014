#
# Don't change this file
#

# Information methods available for all ObjectData
# get_x() x position
# get_y() y position
# get_w() width
# get_h() height
# get_center() (x,y) pair of center of rectangle
# get_dx() fraction of speed in the x direction
# get_dy() fraction of speed in the y direction
# get_distance() distance traveled
# get_speed() speed
# get_state() STATE_ALIVE, STATE_DYING, or STATE_DEAD
# is_alive() True if alive
# is_dying() True if dying (0 health, but not removed from game)
# is_dead() True if dead (0 health, being removed from game)
# get_health() health amount
# get_max_health() maximum health amount
# get_dying_percent() a number from 0 to 1.
#   Each object spends 3 seconds in the "dying" state.  This tells
#   how much of that 3 seconds has passed
# get_px() x position, rounded to nearest integer
# get_py() y position, rounded to nearest integer
# get_pw() width, rounded to nearest integer
# get_ph() height, rounded to nearest integer
# get_pdistance() distance traveled, rounded to nearest integer


STATE_ALIVE = 1
STATE_DYING = 2
STATE_DEAD  = 3

INFINITE_HEALTH = 1000000

class ObjectData:
    """
    All data associated with generic game objects.
    """

    def __init__(self, x=0, y=0, w=0, h=0, oid=0):
        """
        All coordinates are floating point,
        in screen pixel units.
        """
        self.oid = int(oid)  # unique identifier for all valid objects
        self.x = float(x)    # position of left side
        self.y = float(y)    # position of top side
        self.w = float(w)    # width
        self.h = float(h)    # height
        self.dx = 1.         # dx, dy is a unit vector
        self.dy = 0.         # of the velocity
        self.distance = 0.   # total distance traveled by this object
        self.speed = 0.      # magnitude of velocity vector
        self.changed = True  # has object changed since last transmission
        self.state   = STATE_ALIVE # state of the object
        self.health  = INFINITE_HEALTH # health of object.  <= 0 is dead
        self.max_health = INFINITE_HEALTH # maximum health of object
        self.dying_percent = 0.0 # number 0.0 -> 1.0, percentage of time from 0 health to dead  only relevant if state == STATE_DYING
        return

    def set_message(self, msg):
        msg.set_data('oid', self.get_oid())
        msg.set_data('x', self.get_x())
        msg.set_data('y', self.get_y())
        msg.set_data('w', self.get_w())
        msg.set_data('h', self.get_h())
        msg.set_data('dx', self.get_dx())
        msg.set_data('dy', self.get_dy())
        msg.set_data('distance', self.get_distance())
        msg.set_data('speed', self.get_speed())
        msg.set_data('state', self.get_state())
        msg.set_data('health', self.get_health())
        msg.set_data('max_health', self.get_max_health())
        msg.set_data('dying_percent', self.get_dying_percent())
        return

    def set_from_message(self, msg):
        self.set_oid(msg.get_data('oid'))
        self.set_x(msg.get_data('x'))
        self.set_y(msg.get_data('y'))
        self.set_w(msg.get_data('w'))
        self.set_h(msg.get_data('h'))
        self.set_dx(msg.get_data('dx'))
        self.set_dy(msg.get_data('dy'))
        self.set_distance(msg.get_data('distance'))
        self.set_speed(msg.get_data('speed'))
        self.set_state(msg.get_data('state'))
        self.set_health(msg.get_data('health'))
        self.set_max_health(msg.get_data('max_health'))
        self.set_dying_percent(msg.get_data('dying_percent'))
        return
        
    def get_oid(self):
        return self.oid
        
    def get_x(self):
        return self.x
        
    def get_y(self):
        return self.y
        
    def get_w(self):
        return self.w
        
    def get_h(self):
        return self.h

    def get_center(self):
        return (self.x + self.w)/2, (self.y + self.h)/2
        
    def get_dx(self):
        return self.dx
        
    def get_dy(self):
        return self.dy
        
    def get_distance(self):
        return self.distance
        
    def get_speed(self):
        return self.speed
        
    def get_state(self):
        return self.state
        
    def get_health(self):
        return self.health
        
    def get_max_health(self):
        return self.max_health
        
    def get_dying_percent(self):
        return self.dying_percent

    # for display
    def get_px(self):
        return int(round(self.x))
    def get_py(self):
        return int(round(self.y))
    def get_pw(self):
        return int(round(self.w))
    def get_ph(self):
        return int(round(self.h))
    def get_pdistance(self):
        return int(round(self.distance))
        
    def set_oid(self, oid):
        self.oid = int(oid)
        return
        
    def set_x(self, x):
        self.x = float(x)
        return
        
    def set_y(self, y):
        self.y = float(y)
        return
        
    def set_w(self, w):
        self.w = float(w)
        return
        
    def set_h(self, h):
        self.h = float(h)
        return
        
    def set_dx(self, dx):
        self.dx = float(dx)
        return
        
    def set_dy(self, dy):
        self.dy = float(dy)
        return
        
    def set_distance(self, distance):
        self.distance = float(distance)
        return
        
    def add_distance(self, new_distance):
        self.distance += new_distance
        return
        
    def set_speed(self, speed):
        self.speed = float(speed)
        return
        
    def set_state(self, state):
        self.state = state
        return
    def set_alive(self):
        self.set_state(STATE_ALIVE)
        return
    def set_dying(self):
        self.set_state(STATE_DYING)
        return
    def set_dead(self):
        self.set_state(STATE_DEAD)
        return
    def is_alive(self):
        return self.state == STATE_ALIVE
    def is_dying(self):
        return self.state == STATE_DYING
    def is_dead(self):
        return self.state == STATE_DEAD

    def set_health(self, health):
        self.health = float(health)
        return
        
    def set_max_health(self, max_health):
        self.max_health = float(max_health)
        return
        
    def set_dying_percent(self, dying_percent):
        self.dying_percent = float(dying_percent)
        return
        
    def __str__(self):
        s = "%s(%d) %.1f,%.1f %.1fx%.1f -> %.1f,%.1f * %.1f" % (str(self.__class__),
                                                                self.oid, self.x, self.y, self.w, self.h,
                                                                self.dx, self.dy, self.speed)
        return s

    def __repr__(self):
        return str(self)
        
    def is_missile(self):
        return False
    def is_npc(self):
        return False
    def is_player(self):
        return False
    def is_wall(self):
        return False



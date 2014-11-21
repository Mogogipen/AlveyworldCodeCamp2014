import math
from common.object import INFINITE_HEALTH

# margin for floating point numbers to be equal
EPSILON = 0.001

# game parameters
# size of objects
PLAYER_WIDTH = 32
PLAYER_HEIGHT = 32
WALL_THICK = 16
NPC_WIDTH = 16
NPC_HEIGHT = 16
MISSILE_WIDTH = 8
MISSILE_HEIGHT = 8
FIELD_WIDTH = 896
FIELD_HEIGHT = 640
# number of objects
NUM_WALLS = 20
NUM_NPCS = 10

# Health of various object types
HEALTH_OBJECT  = INFINITE_HEALTH
HEALTH_MISSILE =   0.1
HEALTH_NPC     =   3.0
HEALTH_PLAYER  =  10.0*HEALTH_NPC
#HEALTH_PLAYER  =  2.0*HEALTH_NPC
HEALTH_WALL    = INFINITE_HEALTH

#
# level progression by experience points
# the levels are expressed in terms of health, due to
# xp = sum of damage caused
#
# indexes into XP_LEVELS[], order the progression here
XP_LEVEL_0            = 0
XP_LEVEL_SPEED_MEDIUM = 1
XP_LEVEL_MISSILE_MANA_MEDIUM = 2
XP_LEVEL_RANGE_MEDIUM = 3
XP_LEVEL_MOVE_MANA_MEDIUM = 4
XP_LEVEL_POWER_MEDIUM = 5
XP_LEVEL_MOVE_MANA_RECHARGE_MEDIUM = 6
XP_LEVEL_MISSILE_MANA_RECHARGE_MEDIUM = 7
XP_LEVEL_SPEED_FAST   = 8
XP_LEVEL_MISSILE_MANA_HIGH = 9
XP_LEVEL_RANGE_LONG   = 10
XP_LEVEL_MOVE_MANA_HIGH = 11
XP_LEVEL_POWER_HIGH   = 12
XP_LEVEL_MOVE_MANA_RECHARGE_FAST = 13
XP_LEVEL_MISSILE_MANA_RECHARGE_FAST = 14
XP_LEVEL_MAX          = 15
XP_STEP = HEALTH_NPC * 1.0  # kill 1 NPC per level
XP_LEVELS = [ float(x)*XP_STEP for x in range(XP_LEVEL_MAX)  ]

# speeds of the player, and experience levels required
# (pixels/second, minimum_experience)
PLAYER_SPEED_STOP   = (0.0,  XP_LEVELS[XP_LEVEL_0])
PLAYER_SPEED_SLOW   = (30.0, XP_LEVELS[XP_LEVEL_0])
PLAYER_SPEED_MEDIUM = (45.0, XP_LEVELS[XP_LEVEL_SPEED_MEDIUM])
PLAYER_SPEED_FAST   = (60.0, XP_LEVELS[XP_LEVEL_SPEED_FAST])

# Move mana variables
# maximum amount of move mana for a player
MOVE_MANA_MAX = [ (10., XP_LEVELS[XP_LEVEL_0]),
                  (15., XP_LEVELS[XP_LEVEL_MOVE_MANA_MEDIUM]),
                  (20., XP_LEVELS[XP_LEVEL_MOVE_MANA_HIGH]) ]
# units per second
MOVE_MANA_RECHARGE_RATE = [ (0.5, XP_LEVELS[XP_LEVEL_0]),
                            (1.0, XP_LEVELS[XP_LEVEL_MOVE_MANA_RECHARGE_MEDIUM]),
                            (1.5, XP_LEVELS[XP_LEVEL_MOVE_MANA_RECHARGE_FAST]) ]
                            
MOVE_MANA_RECHARGE_TIME = MOVE_MANA_MAX[0][0] / MOVE_MANA_RECHARGE_RATE[0][0]
MOVE_MANA_COST_RATE = MOVE_MANA_MAX[0][0] / (.25 * MOVE_MANA_RECHARGE_TIME) / PLAYER_SPEED_FAST[0]  # mana per second per speed
MOVE_MANA_COST_RATE = 1. / math.log(PLAYER_SPEED_FAST[0]/10.)


# range of the missiles, and experience levels required
# (pixels, minimum_experience)
MISSILE_RANGE_NONE     = (  0.0, XP_LEVELS[XP_LEVEL_0])
MISSILE_RANGE_SHORT    = (100.0, XP_LEVELS[XP_LEVEL_0])
MISSILE_RANGE_MEDIUM   = (200.0, XP_LEVELS[XP_LEVEL_RANGE_MEDIUM])
MISSILE_RANGE_LONG     = (300.0, XP_LEVELS[XP_LEVEL_RANGE_LONG])

# missile speed
# pixels/second
MISSILE_SPEED  = 80.0

# power of the missiles, and experience levels required
# (health points, minimum_experience)
MISSILE_POWER_NONE    = (  0.0,  XP_LEVELS[XP_LEVEL_0])
MISSILE_POWER_LOW     = (  0.5,  XP_LEVELS[XP_LEVEL_0])             # 3.0/0.5 -> 6 shots to kill npc
MISSILE_POWER_MEDIUM  = (  0.75, XP_LEVELS[XP_LEVEL_POWER_MEDIUM])  # 3.0/0.75 -> 4 shots to kill npc
MISSILE_POWER_HIGH    = (  1.5,  XP_LEVELS[XP_LEVEL_POWER_HIGH])    # 3.0/1.5 -> 2 shots to kill npc

# Missile mana variables
# maximum amount of missile mana for a player
MISSILE_MANA_MAX = [ (10., XP_LEVELS[XP_LEVEL_0]),
                     (15., XP_LEVELS[XP_LEVEL_MISSILE_MANA_MEDIUM]),
                     (20., XP_LEVELS[XP_LEVEL_MISSILE_MANA_HIGH]) ]
# units per second
MISSILE_MANA_RECHARGE_RATE = [ (0.5, XP_LEVELS[XP_LEVEL_0]),
                               (1.0, XP_LEVELS[XP_LEVEL_MISSILE_MANA_RECHARGE_MEDIUM]),
                               (1.5, XP_LEVELS[XP_LEVEL_MISSILE_MANA_RECHARGE_FAST]) ]
# 
MISSILE_MANA_COST_RATE = 2./(math.log(10*MISSILE_POWER_HIGH[0])*math.log(MISSILE_RANGE_LONG[0]))


# length of time object spends dying
DYING_TIME = 3.0
# length of time game waits before terminating
GAME_OVER_TIME = 2.0*DYING_TIME


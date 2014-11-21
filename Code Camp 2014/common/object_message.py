#
# Don't change this file
#
from common.game_message import GameMessage
from common.player  import PlayerData
from common.wall  import WallData
from common.npc  import NPCData
from common.missile  import MissileData

M_PLAYER_UPDATE = "PLAYER_UPDATE"
M_WALL_UPDATE   = "WALL_UPDATE"
M_NPC_UPDATE    = "NPC_UPDATE"
M_MISSILE_UPDATE    = "MISSILE_UPDATE"

class PlayerUpdateMessage(GameMessage):
    def __init__(self, player=None):
        GameMessage.__init__(self, M_PLAYER_UPDATE)
        if player:
            player.set_message(self)
        return

    def get_player(self):
        player = PlayerData()
        player.set_from_message(self)
        return player

def string_to_player_update_message(string):
    msg = PlayerUpdateMessage()
    msg.from_string(string)
    return msg
    
class WallUpdateMessage(GameMessage):
    def __init__(self, wall=None):
        GameMessage.__init__(self, M_WALL_UPDATE)
        if wall:
            wall.set_message(self)
        return

    def get_wall(self):
        wall = WallData()
        wall.set_from_message(self)
        return wall

def string_to_wall_update_message(string):
    msg = WallUpdateMessage()
    msg.from_string(string)
    return msg

class NPCUpdateMessage(GameMessage):
    def __init__(self, npc=None):
        GameMessage.__init__(self, M_NPC_UPDATE)
        if npc:
            npc.set_message(self)
        return

    def get_npc(self):
        npc = NPCData()
        npc.set_from_message(self)
        return npc

def string_to_npc_update_message(string):
    msg = NPCUpdateMessage()
    msg.from_string(string)
    return msg

class MissileUpdateMessage(GameMessage):
    def __init__(self, missile=None):
        GameMessage.__init__(self, M_MISSILE_UPDATE)
        if missile:
            missile.set_message(self)
        return

    def get_missile(self):
        missile = MissileData()
        missile.set_from_message(self)
        return missile

def string_to_missile_update_message(string):
    msg = MissileUpdateMessage()
    msg.from_string(string)
    return msg


def message_to_object(msg):
    code = msg.get_command()
    if code == M_WALL_UPDATE:
        obj = WallData()
    elif code == M_NPC_UPDATE:
        obj = NPCData()
    elif code == M_MISSILE_UPDATE:
        obj = MissileData()
    elif code == M_PLAYER_UPDATE:
        obj = PlayerData()
    else:
        obj = None
    if obj:
        obj.set_from_message(msg)
    return obj

# 
OBJECT_MESSAGES = { M_PLAYER_UPDATE:   string_to_player_update_message,
                    M_WALL_UPDATE:     string_to_wall_update_message,
                    M_NPC_UPDATE:      string_to_npc_update_message,
                    M_MISSILE_UPDATE:  string_to_missile_update_message}


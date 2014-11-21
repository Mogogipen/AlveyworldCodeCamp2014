#
# Don't change this file
#
from object import ObjectData
class NPCData(ObjectData):
    """
    All data associated with game NPC objects
    """

    def __init__(self, x=0, y=0, w=0, h=0):
        ObjectData.__init__(self, x, y, w, h)
        return
        
    def is_npc(self):
        return True

#
# Don't change this file
#
from object import ObjectData
class WallData(ObjectData):
    """
    All data associated with game Wall objects
    """

    def __init__(self, x=0, y=0, w=0, h=0):
        ObjectData.__init__(self, x, y, w, h)
        return

    def is_wall(self):
        return True


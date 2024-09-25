from enum import Enum

class Color(Enum):
    BLUE = 1
    YELLOW = 2
    RED = 3
    GREEN = 4
    

class Object:
    def __init__(self, object_id, size, color):
        self.id=object_id
        self.color=color
        self.size=size
        self.left=None
        self.right=None
        self.height=1
        self.bin_id=None
        pass

from node import Node

def comp_1(node_1, node_2):
  if node_1.val > node_2.val:
    return node_1
  else:
    return node_2
    pass

class AVLTree:
    def __init__(self, compare_function=comp_1):
        self.root = None
        self.size = 0
        self.comparator = compare_function

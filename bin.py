from avl import AVLTree
import avl
from node import Node
from object import Object
class Bin:
    def __init__(self, bin_id, capacity):
        self.id=bin_id
        self.capacity=capacity
        self.t=AVLTree(avl.comp_3)
        pass

    # def add_object(self, object):
    #     # Implement logic to add an object to this bin
        
    #     self.t.root = self.t.insert(self.t.root, object)
    #     print(self.t.in_order_traversal_ob(self.t.root))
    #     print(self.t.root.id)
    #     pass

    def remove_object(self, object_id):
        # Implement logic to remove an object by ID
        self.t.root=self.t.delete_obj(self.t.root, object_id)
        pass

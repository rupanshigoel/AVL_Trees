from node import Node
from exceptions import NoBinFoundException
from object import *

def comp_1(node_1, node_2):
    #compare by id
    if node_1.bin.id>node_2.bin.id:
        return 1
    else:
        return 0
    pass
def comp_2(node_1, node_2):
    if node_1.bin.capacity>node_2.bin.capacity:
        return 1
    elif node_1.bin.capacity<node_2.bin.capacity:
        return 0
    else:
        if node_1.bin.id>node_2.bin.id:
            return 1
        else:
            return 0
def comp_3(node_1, node_2):
    if node_1.id>node_2.id:
        return 1
    else:
        return 0
def comp_4(node_1, node_2):
    if node_1.bin.capacity>node_2.bin.capacity:
        return 1
    elif node_1.bin.capacity<node_2.bin.capacity:
        return 0
    else:
        return comp_1(node_2,node_1)
class AVLTree:
    def __init__(self, compare_function):
        self.root = None             # Root node of the AVL Tree
        self.size = 0                # Number of nodes in the tree
        self.comparator = compare_function  # Comparator function

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, root, node):
        if not root:
            return node

        cmp_result = self.comparator(node, root)
        if cmp_result == 0:
            root.left = self.insert(root.left, node)
        elif cmp_result > 0:
            root.right = self.insert(root.right, node)
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Get the balance factor
        balance = self.get_balance(root)

        # Balancing the tree
        # Left Left Case
        if balance > 1 and self.comparator(node, root.left) <= 0:
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and self.comparator(node, root.right) > 0:
            return self.left_rotate(root)

        # Left Right Case
        if balance > 1 and self.comparator(node, root.left) > 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left Case
        if balance < -1 and self.comparator(node, root.right) <= 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root

    def insert_node(self, bin_obj):
        """
        Public method to insert a Bin into the AVL Tree.
        """
        node = Node(bin_obj)
        self.root = self.insert(self.root, node)
        
        self.size += 1
    def min_value_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current
    def delete_obj(self, root, object_id):
        if not root:
            return root
        if object_id < root.id:
            root.left = self.delete_obj(root.left, object_id)
        elif object_id > root.id:
            root.right = self.delete_obj(root.right, object_id)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            temp = self.min_value_node(root.right)
            root.id=temp.id
            root.size=temp.size
            root.color=temp.color
            root.bin_id=temp.bin_id
            root.right = self.delete_obj(root.right, temp.id)

        if not root:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        # Left rotation
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # Right rotation
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # Left-Right rotation
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left rotation
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root
    
   


    def delete(self, root, value, id):
        # if id==159:
        #     print(root.bin.capacity,root.bin.id)
        if not root:
            return root
        if value < root.bin.capacity:
            root.left = self.delete(root.left, value, id)
        elif value > root.bin.capacity:
            root.right = self.delete(root.right, value, id)
       
        elif(id>root.bin.id) :
            # print(4)
            root.right = self.delete(root.right, value, id)
            
        elif(id<root.bin.id) :
            # print(5)
            root.left = self.delete(root.left, value, id)
        else:
            # print('f')
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            temp = self.min_value_node(root.right)
            root.bin=temp.bin
            root.right = self.delete(root.right, temp.bin.capacity, temp.bin.id)

        if not root:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        # Left rotation
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # Right rotation
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # Left-Right rotation
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left rotation
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root


    
    def search(self, root, bin_id):
        if not root:
            return None
        elif bin_id == root.bin.id:
            return root
        elif bin_id < root.bin.id:
            return self.search(root.left, bin_id)
        else:
            return self.search(root.right, bin_id)
    
    def search_obj(self, root, object_id):
        if not root:
            return None
        if object_id == root.id:
            return root
        elif object_id < root.id:
            return self.search_obj(root.left, object_id)
        else:
            return self.search_obj(root.right, object_id)
    

    def compact_fit(self, obj):
        current =self.root
        succ=None

        while(current):
            if obj.size<=current.bin.capacity:
                succ = current
                current = current.left
            else:
                current = current.right
        
        if succ is None:
            raise NoBinFoundException
        else:
            return succ
    def compact_fit_great(self,root, obj):
        can=self.compact_fit(obj)
        current=self.root
        if can is None:
            raise NoBinFoundException
        while(current):
            if current.bin.capacity==can.bin.capacity :
                if can.bin.id > current.bin.id:
                    return can
                else:
                    can=current
                    current=current.right
            elif (current.bin.capacity > can.bin.capacity):
                current=current.left
            else:
                current=current.right
        return can
            
    def largest_fit(self, obj):
        current = self.root
        while(current.right):
            current=current.right

        if(current.bin.capacity>=obj.size):
            return current
        else:
            raise NoBinFoundException
    def largest_fit_least(self, obj):
        candidate = self.largest_fit(obj)
        if(candidate is None):
            # print("y")
            raise NoBinFoundException
        current = self.root
        while(current):
            if(current.bin.capacity == candidate.bin.capacity):
                if(current.bin.id < candidate.bin.id):
                    candidate=current
                current=current.left
            elif(current.bin.capacity < candidate.bin.capacity):
                current=current.right
        return candidate
            
    def in_order_traversal(self, root):
        """
        Perform an in-order traversal of the AVL Tree.
        """
        nodes=[]
        if root is None:
            return nodes
        if root.left:
            nodes.extend(self.in_order_traversal(root.left))
        nodes.append((root.bin.capacity, root.bin.id))
        if root.right:
            nodes.extend(self.in_order_traversal(root.right))
        return nodes
    def in_order_traversal_ob(self, root):
        """
        Perform an in-order traversal of the AVL Tree.
        """
        nodes=[]
        if root is None:
            return nodes
        if root.left:
            nodes.extend(self.in_order_traversal_ob(root.left))
        nodes.append(root.id)
        if root.right:
            nodes.extend(self.in_order_traversal_ob(root.right))
        return nodes
    


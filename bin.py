from avl import AVLTree
class Bin:
    def __init__(self, bin_id, capacity):
        self.cap=capacity
        self.id=bin_id
        self.atree=AVLTree()
        pass

    def avl_search(self,id):
        if root is None:
            return None
        elif key < root.key:
            return self._search(root.left, key)
        elif key > root.key:
            return self._search(root.right, key)
        else: # otherwise, root is the element
            return root
        
    def _insert(self, object):
        # Implement logic to add an object to this bin
        if not root: # base case, no tree
            return newnode
        elif newnode.key < root.key: # insert at the left, if the new node is smaller
            debug("[+] Going left")
            root.left = self._insert(root.left, newnode, duplicated_keys)
        elif newnode.key > root.key: # if greater, insert at the right
            debug("[+] Going right")
            root.right = self._insert(root.right, newnode, duplicated_keys)
        else:
            if duplicated_keys:
                # duplicated keys allowed. We just fuse the values in a list
                if type(root.value) is not list:
                    aux = root.value
                    root.value = []
                    root.value.append(aux)
                root.value.append(newnode.value)
            else:
                return root # no duplicates allowed

        # update height after insertion
        root.update_height()
        debug("[+] Updated height of node {0}".format(root))
        return self._rebalance(root)

        pass

    def _rebalance(self, root: AVLNode) -> AVLNode:
        '''
        Rebalance operations for a given tree node
        '''
        bf = root.get_balance_factor()
        if bf > 1:
            if root.right.get_height(root.right.right) > root.right.get_height(root.right.left): # left-left imbalance
                root = self._left_rotate(root)
            else: # right-left
                root = self._right_left_rotate(root)
        elif bf < -1:
            if root.left.get_height(root.left.left) > root.left.get_height(root.left.right): # right-right imbalance
                root = self._right_rotate(root)
            else: # left-rigth
                root = self._left_right_rotate(root)
            
        return root

    def _right_rotate(self, root: AVLNode) -> AVLNode:
        debug("[+] Right rotation ")
        tmp = root.left
        root.left = tmp.right
        tmp.right = root

        root.update_height()
        tmp.update_height()

        return tmp

    def _left_right_rotate(self, root: AVLNode) -> AVLNode:
        debug("[*] Left-Right rotation ")
        root.left = self._left_rotate(root.left)
        return self._right_rotate(root)
    
    def _left_rotate(self, root: AVLNode) -> AVLNode:
        debug("[+] Left rotation ")
        tmp = root.right
        root.right = tmp.left
        tmp.left = root

        root.update_height()
        tmp.update_height()

        return tmp

    def _right_left_rotate(self, root: AVLNode) -> AVLNode:
        debug("[+] Right-Left rotation ")
        root.right = self._right_rotate(root.right)
        return self._left_rotate(root)

    def _remove(self, root: AVLNode, key) -> AVLNode:
        # search the element, like a BST
        if root is None: # element not found
            return None
        elif key < root.key:
            root.left = self._remove(root.left, key)
        elif key > root.key:
            root.right = self._remove(root.right, key)
        else: # element found
            # check number of childrens
            if root.left is None and root.right is None:
                # no children
                return None
            elif root.left is None:
                # right children only
                root = root.right
            elif root.right is None:
                # left children only
                root = root.left
            else:
                # two children
                aux = self.find_min(root.right)
                root.update_content(aux)
                root.right = self.remove(root.right, aux.key)
        
        # update heights
        root.update_height()
        if root is not None:
            root = self._rebalance(root)

        return root
    
    def remove(self, key):
        '''
        Remove the node with key in the current tree, if exists
        '''
        if self.root is None:
            print('[-] AVL tree is empty!')
        else:
            self.root = self._remove(self.root, key)

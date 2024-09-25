from bin import Bin
import avl
from node import Node
from avl import AVLTree
from object import Object, Color
from exceptions import NoBinFoundException
rachit = None

class GCMS:
    def __init__(self):
        # Maintain all the Bins and Objects in 

        #the tree storing bins in terms of id
        self.tree=AVLTree(avl.comp_1)

        #tree storing bins in terms of capacity
        self.treecap=AVLTree(avl.comp_2)

        #tree storing objects in terms of id
        self.objtree=AVLTree(avl.comp_3)
        
        pass 

    def add_bin(self, bin_id, capacity):
        bin=Bin(bin_id,capacity)
        bin2= Bin(bin_id,capacity)
        self.tree.insert_node(bin)
        self.treecap.insert_node(bin2)
        pass

    def add_object(self, object_id, size, color):
        obj=Object(object_id,size,color)
        obj2 = Object(object_id,size,color)
        
        if (obj.color==Color.BLUE):
            succ=self.treecap.compact_fit(obj)
            x=succ.bin.id
            y=succ.bin.capacity
            obj.bin_id=x
            way=self.tree.search(self.tree.root, x)
            way.bin.capacity-=obj.size
            self.treecap.root=self.treecap.delete(self.treecap.root, y, x)
            way.bin.t.root=way.bin.t.insert(way.bin.t.root, obj2)
            
            self.objtree.root=self.objtree.insert(self.objtree.root, obj )
            new=Bin(x, (y-obj.size))
            new2=Node(new)
            self.treecap.root=self.treecap.insert(self.treecap.root, new2)
        elif (obj.color==Color.GREEN):
            succ=self.treecap.largest_fit(obj)
            x=succ.bin.id
            y=succ.bin.capacity
            obj.bin_id=x
            way=self.tree.search(self.tree.root, x)
            way.bin.capacity-=obj.size
            self.treecap.root=self.treecap.delete(self.treecap.root, y, x)
            way.bin.t.root=way.bin.t.insert(way.bin.t.root, obj2)
            self.objtree.root=self.objtree.insert(self.objtree.root, obj )
            new=Bin(x, (y-obj.size))
            new2=Node(new)
            self.treecap.root=self.treecap.insert(self.treecap.root, new2)
            
        elif(obj.color==Color.RED):
            succ=self.treecap.largest_fit_least(obj)
            x=succ.bin.id

            y=succ.bin.capacity
            obj.bin_id=x
            way=self.tree.search(self.tree.root, x)
            way.bin.capacity-=obj.size
            self.treecap.root=self.treecap.delete(self.treecap.root, y, x)
            way.bin.t.root=way.bin.t.insert(way.bin.t.root, obj2)
            self.objtree.root=self.objtree.insert(self.objtree.root, obj )
            new=Bin(x, (y-obj.size))
            new2=Node(new)
            self.treecap.root=self.treecap.insert(self.treecap.root, new2)
            
            
        elif(obj.color==Color.YELLOW):
            succ=self.treecap.compact_fit_great(self.treecap.root, obj)
            if succ is None:
                raise NoBinFoundException
            else:
                x=succ.bin.id
                y=succ.bin.capacity
                obj.bin_id=x
                way=self.tree.search(self.tree.root, x)
                way.bin.capacity-=obj.size
                self.treecap.root=self.treecap.delete(self.treecap.root, y, x)
                way.bin.t.root=way.bin.t.insert(way.bin.t.root, obj2)
                self.objtree.root=self.objtree.insert(self.objtree.root, obj )
                new=Bin(x, (y-obj.size))
                new2=Node(new)
                self.treecap.root=self.treecap.insert(self.treecap.root, new2)
              
    def delete_object(self, object_id):
        ob=self.objtree.search_obj(self.objtree.root, object_id)
        z=ob.bin_id
        d=ob.size
        self.objtree.root=self.objtree.delete_obj(self.objtree.root, object_id)
        node2=self.tree.search(self.tree.root, z)
        q=node2.bin.capacity
        self.treecap.root=self.treecap.delete(self.treecap.root, q, z)
        node2.bin.capacity+=d
        b=Bin(z,q+d)
        c=Node(b)
        self.treecap.root=self.treecap.insert(self.treecap.root, c )
        node2.bin.remove_object(object_id)

    def bin_info(self, bin_id):
        # returns a tuple with current capacity of the bin and the list of objects in the bin (int, list[int])
        
        bin1= self.tree.search(self.tree.root, bin_id)
        
        info=(bin1.bin.capacity, bin1.bin.t.in_order_traversal_ob(bin1.bin.t.root))
        return info
    def object_info(self, object_id):
        # returns the bin_id in which the object is stored
        y=self.objtree.search_obj(self.objtree.root, object_id)
        if y is not None:
            return(y.bin_id)
        else:
            return None
        pass

    
    

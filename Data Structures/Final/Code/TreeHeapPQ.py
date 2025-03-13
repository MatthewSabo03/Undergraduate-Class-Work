from PriorityQueue_Interface import PriorityQueue_Interface
from Binary_Node import BinaryNode

class TreeHeapPQ(PriorityQueue_Interface):
    def __init__(self):
        self._list = None
        self._len = 0
        self._root = BinaryNode()
        
    def _add_helper(self, new_node):
        #Runs until current Node is at the bottom of the left side
        while self._list.get_left() is not None:
            self._list = self._list.get_left()
        
        #Checks if the right child of the parent is None, if it is then move back to parent
        #And insert the Node at the right child position
        if self._list.get_parent().get_right() is None:
            self._list = self._list.get_parent()
            self._list.set_right(new_node)
            new_node.set_parent(self._list)

            

    def add(self, key, data):
        #Checks if self._list is a Binary Node, if it is not then it Creates the trees
        if self._list is None:
            self._list = BinaryNode((key,data))
            self._root = self._list
            self._len +=1
        else:
            new_node = BinaryNode((key,data))
            _add_helper(self, new_node)
            #Moves current node to the left if both left and right child is not None
            while self._list.get_left() is not None and self._list.get_right() is not None:
                self._list = self._list.get_left()


    def min(self):
        return (self._list.get_element())

    def remove_min(self):
        pass

    def is_empty(self):
        return self._len == 0

    def __len__(self):
        return self._len
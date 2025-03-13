'''
' Class for nodes which will binary tree.
'''
from Double_Node import DNode

class BinaryNode(DNode):
    '''
    ' Constructor. Creates a node with an element, a parent node, a left node,
    '   and a right node. No paramteres are required but all can be specified.
    '''
    def __init__(self, element = None, parent_node = None, left_child = None, right_child = None):
        super().__init__(element, left_child, right_child)
        self._parent = parent_node                        # parent node reference

    #------------------------------- accessors -------------------------------
    '''
    ' Returns a reference to the parent node
    '''
    def get_parent(self):
        return self._parent

    '''
    ' Returns a reference to the left child node
    '''
    def get_left(self):
        return super().get_previous()

    '''
    ' Returns a reference to the right child node
    '''
    def get_right(self):
        return super().get_next()

    #------------------------------- mutators -------------------------------
    '''
    ' Sets the parent node and returns the old "parent child" that this
    '   node used to point to
    '''
    def set_parent(self, new_parent):
        old_parent = self._parent
        self._parent = new_parent
        return old_parent

    '''
    ' Sets the left child node and returns the old "left child" that this
    '   node used to point to
    '''
    def set_left(self, new_left):
        return self.set_previous(new_left)

    '''
    ' Sets the right child node and returns the old "right child" that this
    '   node used to point to
    '''
    def set_right(self, new_right):
        return self.set_next(new_right)

    #----------------------------- MAGIC METHOD -----------------------------
    def __str__(self):
        output =  "Element: " + str(self.get_element()) + ";   "
        output += "Has Parent: " + str(self.get_parent() is not None) + ";   "
        output += "Has Left: " + str(self.get_left() is not None) + ";   "
        output += "Has Right: " + str(self.get_right() is not None) + ";"
        return output

if __name__ == '__main__':
    b1 = BinaryNode(10)
    b2 = BinaryNode(20)
    b3 = BinaryNode(30)
    b5 = BinaryNode(50)
    b6 = BinaryNode(60)

    b1.set_left(b2)
    b2.set_parent(b1)
    
    b1.set_right(b3)
    b3.set_parent(b1)

    b2.set_right(b5)
    b5.set_parent(b2)
    
    b3.set_left(b6)
    b6.set_parent(b3)

    print(b1)
    print()
    print(b2)
    print()
    print(b3)
    print()
    print(b5)
    print()
    print(b6)
    print()

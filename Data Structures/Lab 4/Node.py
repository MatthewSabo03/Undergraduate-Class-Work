'''
' Class for nodes which will construct a singly linked list.
'''
class Node:
    '''
    ' Constructor. Creates a node with an element and a next
    '   node. No paramteres are required but all can be specified.
    '''
    def __init__(self, element = None, next_node = None):
        self._element = element
        self._next = next_node
        

    #------------------------------- accessors -------------------------------
    '''
    ' Returns the data element contained within this node
    '''
    def get_element(self):
        return self._element
    

    '''
    ' Returns a reference to the next node
    '''
    def get_next(self):
        return self._next
    

    #------------------------------- mutators -------------------------------
    '''
    ' Sets the data element contained within this code only if it
    '   doesn't already contain data
    '''
    def set_element(self, new_element):
        if self._element is None:
            self._element = new_element
            

    '''
    ' Sets the next node and returns the old "next node" that this
    '   node used to point to
    '''
    def set_next(self, new_next):
        old_next = self._next
        self._next = new_next
        return old_next
    

if __name__ == '__main__':
    head = Node(5, Node(7, Node(9, Node(10, Node("potato salad")))))
        
    print(head.get_element())
    print(head.get_next().get_element())
    print(head.get_next().get_next().get_element())
    print(head.get_next().get_next().get_next().get_element())
    print(head.get_next().get_next().get_next().get_next().get_element())
    print(head.get_next().get_next().get_next().get_next().get_next())

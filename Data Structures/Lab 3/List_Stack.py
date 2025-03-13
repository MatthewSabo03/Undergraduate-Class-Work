from Stack_Interface import Stack_Interface
from exceptions import EmptyStackException

class ListStack(Stack_Interface):

    # Constructor. Creates a new empty stack.
    def __init__(self):
       self._data = []


    # Adds value to the "top" of the stack. Values are inserted in a
    #   last-in-first-out fashion meaning the element returned by pop
    #   will be the last element added by push.
    def push(self, new_element):
        self._data.append(new_element)


    # Removes and returns an element from "top" of the stack. Values are
    #   inserted in a last-in-first-out fashion meaning the element returned
    #   by pop will be the last element added by push.
    def pop(self):
        #I) Try to store the element at the top of the stack
        saved_element = self.peek()

        #II) Remove the top element in the stack
        del(self._data[len(self)-1])

        #III) Return the stored value            
        return saved_element


    # Returns an element from "top" of the stack. Values are
    #   inserted in a last-in-first-out fashion meaning the element returned
    #   by top will be the last element added by push.
    def peek(self):
        if len(self) > 0:
            return self._data[len(self)-1]
        else:
            raise EmptyStackException("No elements in stack")


    # Returns the number of elements in the stack
    def __len__(self):
        return len(self._data)

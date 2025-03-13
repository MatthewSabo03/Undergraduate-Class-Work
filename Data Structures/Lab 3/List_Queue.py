from Queue_Interface import Queue_Interface
from exceptions import EmptyQueueException

class ListQueue(Queue_Interface):

    # Constructor. Creates a new empty queue using a dynamic array.
    def __init__(self):
        self._data = []


    # Adds value to the "tail" of the queue. Values are inserted in a
    #   first-in-first-out fashion meaning the element returned by dequeue
    #   will be the first element added by enqueue
    def enqueue(self, new_element):
        self._data.append(new_element)


    # Removes and returns an element from "head" of the queue. Values are
    #   inserted in a first-in-first-out fashion meaning the element returned
    #   by dequeue will be the first element added by enqueue
    def dequeue(self):
        #I) Try to store the element at the front of the queue
        return_value = self.first()
        
        #II) Remove the first element in the queue
        del(self._data[0])

        #III) Return the value
        return return_value


    # Returns an element from "head" of the queue. Values are
    #   inserted in a first-in-first-out fashion meaning the element returned
    #   by dequeue will be the first element added by enqueue
    def first(self):
        #I) If the queue is empty, throw an exception
        if(self.is_empty()):
            raise EmptyQueueException("No elements in queue")

        #II) Return the element at the top of the stack
        return self._data[0]


    # Returns the number of elements in the queue
    def __len__(self):
        return len(self._data)

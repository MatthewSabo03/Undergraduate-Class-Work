from abc import abstractmethod, ABC

class Queue_Interface(ABC):

    # Constructor. Creates a new empty queue.
    @abstractmethod
    def __init__(self):
        pass


    # Adds value to the "tail" of the queue. Values are inserted in a
    #   first-in-first-out fashion meaning the element returned by dequeue
    #   will be the first element added by enqueue
    @abstractmethod
    def enqueue(self, value):
        pass


    # Removes and returns an element from "head" of the queue. Values are
    #   inserted in a first-in-first-out fashion meaning the element returned
    #   by dequeue will be the first element added by enqueue
    @abstractmethod
    def dequeue(self):
        pass


    # Returns an element from "head" of the queue. Values are
    #   inserted in a first-in-first-out fashion meaning the element returned
    #   by dequeue will be the first element added by enqueue
    @abstractmethod
    def first(self):
        pass


    # Returns the number of elements in the queue
    @abstractmethod
    def __len__(self):
        pass


    # Returns True if there are any elements in the queue, False otherwise
    def is_empty(self):
        return len(self) == 0

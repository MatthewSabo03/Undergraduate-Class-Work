from abc import abstractmethod, ABC

class PriorityQueue_Interface(ABC):

    # Constructor. Creates a new empty priority queue.
    @abstractmethod
    def __init__(self):
        pass

    # Adds value to the priority queue with the associated key value. Values
    #   will be returned arbitrarily based on having the minimum key value
    #   remaining in the priority queue.
    @abstractmethod
    def add(self, key, value):
        pass

    # Removes and returns a (key, value) pair with a minimum key value in the
    #   priority queue. Values will be returned arbitrarily based on having
    #   the minimum key value remaining in the priority queue.
    @abstractmethod
    def remove_min(self):
        pass

    # Returns a (key, value) pair with a minimum key value in the
    #   priority queue. Values will be returned arbitrarily based on having
    #   the minimum key value remaining in the priority queue.
    @abstractmethod
    def min(self):
        pass

    # Returns True if there are any elements in the priority queue,
    #   False otherwise
    @abstractmethod
    def is_empty(self):
        pass
    
    # Returns the number of elements in the priority queue
    @abstractmethod
    def __len__(self):
        pass

from PriorityQueue_Interface import PriorityQueue_Interface
from Node import Node

class LinkedLinkedPQ(PriorityQueue_Interface):
    def __init__(self):
        self._data = None
        self._key = None
    
    def add(self, key, data):
        #Runs if self._key does not have Nodes
        if self._key is None:
            self._key = Node(key)
            self._data = Node(data)
        
        #Runs if self._key has Nodes
        else:
            #Creates new nodes for the new data
            new_nodek = Node(key)
            new_noded = Node(data)
            
            #Runs if the element in the current Node in self._key is greater than key
            #Adds the element to the front of the list
            if self._key.get_element() > key:

                #Sets the next in the new nodes and then equals key and data to those lists 
                new_nodek.set_next(self._key)
                self._key = new_nodek
                new_noded.set_next(self._data)
                self._data = new_noded
            
            #Runs if the element in the current Node in self._key is less than key
            #Adds the new nodes to either the middle or last position of the lists
            else:

                #Creates new linked lists and copys both linked lists so pointers can be reset after adding new node
                resKey = Node()
                resData = Node()
                resKey.set_next(self._key)
                resKey = resKey.get_next()
                resData.set_next(self._data)
                resData = resData.get_next()

                #Moves the current Node to the next position in both self._key and self._data
                while self._key.get_next() is not None and self._key.get_next().get_element() < key:
                    self._key = self._key.get_next()
                    self._data = self._data.get_next()

                #Checks if the current Node is at the end of self._key 
                #If it is not then it sets the next value for the new node to the next value in both lists
                if self._key.get_next() is not None:
                    new_nodek.set_next(self._key.get_next())
                    new_noded.set_next(self._data.get_next())
                
                #Adds the new nodes to the next position in the list
                self._key.set_next(new_nodek)
                self._data.set_next(new_noded)

                #Copys both lists back onto eachother so the current position in the list gets reset to the start
                self._key = resKey
                self._data = resData



    def min(self):
       return (self._key.get_element(), self._data.get_element())

    def remove_min(self):
        #Sets the current min to rkey and rdata
        rkey = self._key.get_element()
        rdata = self._data.get_element()

        #Removes the current Node from the list
        self._key = self._key.get_next()
        self._data = self._data.get_next()
        return (rkey, rdata)
        
    def is_empty(self):
        if self._key is None:
            return True
        else:
            return False

    def __len__(self):
        i = 0
        #nodePointer is created so that the current position of the main list doesn't change
        nodePointer = self._key
        while nodePointer is not None:
            i+=1
            if nodePointer.get_next() is None:
                break
            nodePointer = nodePointer.get_next()
        return i
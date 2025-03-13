from PriorityQueue_Interface import PriorityQueue_Interface
from Node import Node

class LinkedLinkedPQ(PriorityQueue_Interface):
    def __init__(self):
        self._list = None
        self._head = None
    
    def add(self, key, data):
        #Creates a new node that has the singly linked list of key and data
        dataList = Node(key, Node(data))
        
        #Runs if self._list does not have Nodes
        if self._list is None:
            self._list = Node(dataList)
            self._head = self._list
        
        #Runs if self._list has Nodes
        else:
            #Creates the node that will be put into the main list and element is set to the linked list of key and data
            new_node = Node(dataList)
            
            #Runs if the element in the current Node in self._list is greater than key
            #Adds the element to the front of the list
            if self._list.get_element().get_element() > key:

                #Sets the next of the new node to the front of the list and changes the values of list and head to the new node 
                new_node.set_next(self._list)
                self._list = new_node
                self._head = self._list

            #Runs if the element in the current Node in self._list is less than key
            #Adds the new nodes to either the middle or last position of the lists
            else:

                #Moves the current Node to the next position in self._list
                while self._list.get_next() is not None and self._list.get_next().get_element().get_element() < key:
                    self._list = self._list.get_next()
                
                #Checks if the current Node is at the end of self._list 
                #If it is not then it sets the next value for the new node to the next value in self._list
                if self._list.get_next() is not None:
                    new_node.set_next(self._list.get_next())
                
                #Adds the new nodes to the next position in the list
                self._list.set_next(new_node)

                #Resets the position of list back to the start of the main list
                self._list = self._head



    def min(self):
       return (self._head.get_element().get_element(), self._head.get_element().get_next().get_element())

    def remove_min(self):
        #Sets the current min to rkey
        rkey = (self._list.get_element().get_element(), self._list.get_element().get_next().get_element())
        #Removes the current Node from the list and resets head
        self._list = self._list.get_next()
        self._head = self._list
        return (rkey)
        
    def is_empty(self):
        if self._list is None:
            return True
        else:
            return False

    def __len__(self):
        i = 0
        #nodePointer is created so that the current position of the main list doesn't change
        nodePointer = self._list
        while nodePointer is not None:
            i+=1
            if nodePointer.get_next() is None:
                break
            nodePointer = nodePointer.get_next()
        return i
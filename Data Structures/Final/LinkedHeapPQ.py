from PriorityQueue_Interface import PriorityQueue_Interface
from Double_Node import DNode

class LinkedHeapPQ(PriorityQueue_Interface):
    def __init__(self):
        self._list = None
        self._len = 0
        self._head = DNode()
        self._tail = DNode()

    def add(self, key, data):
        #Checks if self._list has nodes, if not then it sets self._list to a new DNode
        #It then sets the head and tail node and adds 1 to length
        if self._list is None:
            self._list = DNode((key, data))
            self._head = self._list
            self._tail = self._list
            self._len +=1
        
        #runs if self._list has nodes
        else:
            #Sets new data to new Node
            new_node = DNode((key, data))
            
            #Iterates over self._list until it reaches the end of the list
            if self._len > 1:
                while self._list.get_next() is not None:
                    self._list = self._list.get_next()
            
            #Adds new nodes to end of list and adds 1 to length
            self._list.set_next(new_node)
            new_node.set_previous(self._list)
            self._len+=1

            parentIndex = int(self._len/2)

            #Runs if the length of the linked list is 2
            #Adds the new node to the beginning of the list
            if self._len == 2:
                if new_node.get_element()< self._list.get_element():
                    #new_node <- self._list
                    self._list.set_previous(new_node)
                    #new_node -> self._list
                    new_node.set_next(self._list)
                    #None <- self._list 
                    self._list.set_next(None)
                    #None <- new_node
                    new_node.set_previous(None)
                    self._head = new_node
                    self._tail = self._list
            else:
                self._tail = new_node
                firstTime = True
                while new_node.get_element() < self._list.get_element():
                    #resets the current node to the head of the list
                    self._list = self._head

                    #Finds parent of newly inserted node
                    currentIndex = 1
                    while currentIndex != parentIndex:
                        self._list = self._list.get_next() 
                        currentIndex+=1

                    #Compare element in new node and parent node, if new node is less then
                    #swap nodes. Otherwise break
                    if new_node.get_element() < self._list.get_element():
                        current_node= DNode(self._list.get_element(), self._list.get_previous(), self._list.get_next())
                        if self._list == self._head:
                            self._head = new_node
                        if firstTime is True:
                            self._tail = self._list
                            firstTime = False

                        #parent node next is set to next of new_node 
                        self._list.set_next(new_node.get_next())

                        #parent node previous is set to previous of new_node
                        if new_node.get_previous() != self._list:
                            self._list.set_previous(new_node.get_previous())
                        else:
                            self._list.set_previous(new_node)
                        
                        #next node from parent node previous is set to new_node
                        if current_node.get_next() != new_node:
                            current_node.get_next().set_previous(new_node)
                        else:
                            current_node.get_next().set_previous(current_node.get_previous())

                        #previous node from new_node next is set to parent node
                        if new_node.get_previous() is not None:
                            new_node.get_previous().set_next(self._list)
                        
                        if current_node.get_previous() is not None:
                            #previous node from parent node next is set to new_node
                            current_node.get_previous().set_next(new_node)
                        else:
                            #Otherwise set to None
                            new_node.set_previous(None)

                        #previous of new_node is set to previous of parent node 
                        new_node.set_previous(current_node.get_previous())
                        
                        if new_node.get_next() is not None and new_node.get_next() != current_node:
                            #next node from new_node previous is set to parent node
                            new_node.get_next().set_previous(self._list)

                        #new_node next is set to parent node next
                        if current_node.get_next() != new_node:
                            new_node.set_next(current_node.get_next())
                        else:
                            new_node.set_next(self._list)

                        #previous of new_node next is set to new_node
                        if new_node.get_previous() is not None:
                            new_node.get_previous().set_next(new_node)

                        parentIndex = int(currentIndex/2)
                        self._list = self._head
                    else:
                        break
                
                

    def min(self):
        return (self._head.get_element())

    def remove_min(self):
        #Supposed to sort the items according to heap order but couldnt compile it. Could get it to print out.
        rmin = self._list.get_element()
        self._list = self._list.get_next()
        self._head = self._list
        if self._list is not None:
            self._list.set_previous(None)
        self._len -= 1
        return rmin

    def is_empty(self):
        return self._len == 0

    def __len__(self):
        return self._len

#I tried to fix remove_min with this helper function but couldnt get it to compile
#Putting this here so I can at least try to get some points from my work
'''
def _remove_helper(self, isLeft):
        current_node = DNode(self._list.get_element(), self._list.get_previous(), self._list.get_next())
        if isLeft is True:
            self._list.set_next(self._list.get_next().get_next())

            #parent node previous is set to previous of new_node
            if self._list.get_previous() != self._list:
                self._list.set_previous(self._list.get_next())
            else:
                self._list.set_previous(self._list.get_next().get_previous())
                    
            #next node from parent node previous is set to new_node
            if current_node.get_next() != self._list.get_next():
                current_node.get_next().set_previous(self._list.get_next())
            else:
                current_node.get_next().set_previous(current_node.get_previous())

            #previous node from new_node next is set to parent node
            if self._list.get_next().get_previous() is not None:
                self._list.get_next().get_previous().set_next(self._list)
                        
            if current_node.get_previous() is not None:
            #previous node from parent node next is set to new_node
                current_node.get_previous().set_next(self._list.get_next())
            else:
                #Otherwise set to None
                self._list.get_next().set_previous(None)

            #previous of new_node is set to previous of parent node 
            self._list.get_next().set_previous(current_node.get_previous())
                        
            if self._list.get_next().get_next() is not None and self._list.get_next().get_next() != current_node:
                #next node from new_node previous is set to parent node
                self._list.get_next().get_next().set_previous(self._list)

            #new_node next is set to parent node next
            if current_node.get_next() != self._list.get_next():
                self._list.get_next().set_next(current_node.get_next())
            else:
                self._list.get_next().set_next(self._list)

            #previous of new_node next is set to new_node
            if self._list.get_next().get_previous() is not None:
                self._list.get_next().get_previous().set_next(self._list.get_next())
        else:
            pass

    def remove_min(self):
        #Copies the head
        rmin = self._head.get_element()
        #replacing head with tail
        self._tail.get_previous().set_next(None)
        self._tail.set_next(self._head.get_next())
        self._head.get_next().set_previous(self._tail)
        self._head.set_next(None)
        self._head = self._tail
        self._tail = self._head.get_previous()
        self._head.set_previous(None)
        self._len -=1
        flippedNode = DNode(self._head.get_element(), self._head.get_previous(), self._head.get_next())
        #resorts the list
        currentIndex = 1
        childIndex = currentIndex*2
        #Finds left child
        while currentIndex < childIndex:
            self._list = self._list.get_next()
            currentIndex +=1
    
        if flippedNode.get_element() < self._list.get_element() or flippedNode.get_element() < self._list.get_next().get_element():
            #left
            currentIndex = 1
            self._list = self._head
            while currentIndex < childIndex-1:
                self._list = self._list.get_next()
                currentIndex +=1

            if self._list < self._list.get_next():
                isLeft = True
                _remove_helper(self, isLeft)
            else:
                isLeft = False
                _remove_helper(self, isLeft)
        '''
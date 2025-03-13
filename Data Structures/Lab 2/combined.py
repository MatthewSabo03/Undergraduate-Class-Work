#imports
from Double_Node import DNode
from Node import Node

def _node_helper(list_node):
    #Takes a variable and makes it a node
    new_node = DNode(list_node)
    new_node = list_node
    return new_node


def combine_sorted(list1, list2):
    cList = DNode()
    cList2 = DNode()
    head = DNode()
    firstTime = True
    #Checks if either list has nothing in it
    if (list1 is None or list2 is None):
        #Runs if list 1 is not empty and adds all values of list 1 to cList
        if list1.get_element() is not None:
            while list1.get_next() is not None:
                cList = _node_helper(list1)
                cList = cList._next
                list1 = list1._next
            if firstTime is True:
                firstTime = False
                head = cList

        #runs if list 2 is not empty and adds all values of list 2 to cList
        elif list2.get_element() is not None:
            while list1._next is not None:
                cList._next = _node_helper(list2)
                cList = cList._next
                list2 = list2._next
                if firstTime is True:
                    firstTime = False
                    head = cList

        #Runs if both lists are empty
        else:
            return None

    else:
        #Runs until it reaches the end of either list
        while (list1.get_next() is not None) and (list2.get_next() is not None):

            #Runs if list 1 is greater than list 2 
            if list1.get_element() > list2.get_element():
                new_node = DNode(list2.get_element())
                new_node.set_previous(cList2)
                cList2.set_next(new_node)

                CList2 = CList.get_next()
                list2 = list2.get_next()
                
                #adds Node from list 2 to cList
                cList._next = _node_helper(list2)
                cList = cList._next
                list2 = list2._next

            #Runs if list 2 is greater than list 1
            elif list1.get_element() < list2.get_element():
                #adds Node from list 1 to cList
                cList._next = _node_helper(list1)
                cList = cList._next
                list1 = list1._next

            #Runs if list 1&2 are equal
            else:
                #adds both nodes to cList
                cList._next = _node_helper(list1)
                list1 = list1._next
                cList._next = _node_helper(list2)
                list2 = list2._next
                cList = cList._next
                
                
            if firstTime is True:
                firstTime = False
                head = cList

        #Runs if list 1 reached the end first
        if list1._next is None:

            if list1.get_element() is not None:
                #Adds last value in list 1 to the end of array
                cList._next = _node_helper(list1)
                cList = cList._next

            while list2.get_next() is not None:
                #Runs until list 2 reaches end of list
                cList = _node_helper(list2)
                list2 = list2._next
                cList = cList._next

        #Runs if list 2 reached the end first
        elif list2._next is None:

            if list2.get_element is not None:
                #Adds last value in list 2 to the end of array
                cList._next = _node_helper(list2)
                cList = cList._next

            while list1._next is not None:
                #Runs until list 1 reaches end of list
                cList._next = _node_helper(list1)
                list1 = list1._next
                cList = cList._next

    cList2 = head
    return cList2

#I can't figure the sytax to get the two input lists to not be mutable
#tried my best and spent about 4 hours on it and can't figure it out. Sorry about that




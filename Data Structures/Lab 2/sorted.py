from Node import Node

def insert_sorted(head_node, new_element):
    #Sets new_element as a Node
    new_node = Node(new_element)

    #sets up list traversal
    next_node = Node()
    prev_node = Node()

    #Check for manual element insertion
    insertRecord = False

    #Runs if there is no elements in linked list and adds new_element to head
    if head_node is None:
        head_node = new_node
        insertRecord = True

    #Runs if there is values in the linked list
    else:
        prev_node = head_node
        if head_node.get_next() is None:
            if (new_node.get_element() < head_node.get_element()):
                insertRecord = True
                new_node._next = head_node
                head_node = new_node
            else:
                head_node._next = new_node
        else:
            #sets next_node as the node ahead of the current node
            next_node = head_node.get_next()

            #iterates over every value in the linked list until prev_node = None
            while prev_node.get_next() is not None:

                #Compares the values of new_node and next_node
                if (new_node.get_element() < next_node.get_element()):
                    #adds 
                    insertRecord = True
                    new_node._next = next_node
                    if prev_node == head_node:

                        if new_node.get_element() < head_node.get_element():
                            new_node._next = head_node
                            head_node = new_node

                        else:
                            prev_node._next = new_node

                    else:
                        prev_node._next = new_node
                    break

                else:
                    prev_node = prev_node._next
                    next_node = prev_node._next

    #Runs if no values were ever manually put into the list        
    if insertRecord is False:
        prev_node._next = new_node

    return head_node        
        
        
        
        
            
    


#'''
#Test code can go below if you want
#'''
#if __name__ == '__main__':
    #linkedList = Node()
    #sortedList = insert_sorted(linkedList,3)
    #sortedList = insert_sorted((insert_sorted(linkedList,3)),4)

#print(sortedList.get_element())
#print(sortedList.get_next().get_element())
#print(node.get_next().get_next().get_element())
    

#[3->4->6]
#insert 5
#output needs to = [3->4->5->6]
#returns 3

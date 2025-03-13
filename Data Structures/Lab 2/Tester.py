'''
' Tester code for Lab 03.
'''

from Node import Node
from Double_Node import DNode
from sorted import insert_sorted
from combined import combine_sorted

'''
Function which takes a pointer to a node and a parameter which represents
  the type_of_node that we need to check for. If all of the nodes in the list
  are of type Node or None. It returns true if this is a well-formed
  linked list and false otherwise.
'''
def _list_valid(current_node, type_of_node):

    #I) While the current Node is not None
    while not current_node is None:

        #A) If the type of the current node is not None, return false
        if type(current_node) != type_of_node:
            return False

        #B) Move the current_node to the next node
        current_node = current_node.get_next()

    #II) If we are here, then we got through the entire linked list
    #       so return true
    return True

'''
  Functino which takes a pointer to a node and determines if the elements in
  the list are in order (either non-decreasing or non-increasing.
'''
def _list_ordered(current_node):

    #I) Set a variable that says if direction has been determined and another
    #       for the direction of movement
    direction_determined = False
    list_increasing = False

    #III) While the current Node and the current Node's next is not None
    while (not current_node is None) and (not current_node.get_next() is None):

        #A) If the direction has not been determined and the elements in the
        #       current node and the next node are different
        if (not direction_determined) and \
           (current_node.get_element() != current_node.get_next().get_element()):

            #1) Set the direction determined variable to true
            direction_determined = True

            #2) Set the list_increasing variable appropriately
            list_increasing = (current_node.get_element() < current_node.get_next().get_element())

        #B) If the direction has been determined
        if direction_determined:

            #1) If the list is increasing and the element in the current node
            #       is greater than the element in the next, return False
            if list_increasing and \
               (current_node.get_element() > current_node.get_next().get_element()):
                return False

            #2) Else, if the list is not increasing and the element in the
            #       current node is less than the element in the next, return False
            elif (not list_increasing) and \
               (current_node.get_element() < current_node.get_next().get_element()):
                return False
        
        #C) Move the current_node to the next node
        current_node = current_node.get_next()

    #II) If we are here, then we got through the entire linked list
    #       so return true
    return True

'''
Function which takes a pointer to a node and prints out the list based on it.
  Note: We can move through the either list with just the get_next method.
'''
def _list_output(current_node):
    index = 0

    #I) Declare our output string as the header
    output_string = "Linked List\n------------------\n"

    #II) While the current Node is not None
    while not current_node is None:
        
        #A) Add the index to the output string
        output_string += "[" + str(index) + "] :\t"
        
        #B) Add the element to the output string followed by an arrow
        output_string += str(current_node.get_element()) + " →\n"

        #C) Update the current Node to the current node's next Node
        current_node = current_node.get_next()

        #D) Update the index
        index += 1

    #III) Add the done message and some formatting to the end
    output_string += "Done!\n"
    
    #IV) Return the output
    return output_string


#I) Test the elements from the insert_sorted function for ints
print("--------------------------------------------------------------------")
print("I) Test the elements from the insert_sorted function for ints")
print("--------------------------------------------------------------------")
print("   3 -> 4 -> 5")
print("--------------------------------------------------------------------")

#Empty
head_num = insert_sorted(None, 5)
print(_list_output(head_num))

#Front
head_num = insert_sorted(head_num, 3)
print(_list_output(head_num))

#Middle
head_num = insert_sorted(head_num, 4)
print(_list_output(head_num))

print("--------------------------------------------------------------------")
print("   3 -> 4 -> 5 -> 10 -> 15 -> 15")
print("--------------------------------------------------------------------")

#End
head_num = insert_sorted(head_num, 15)
print(_list_output(head_num))

head_num = insert_sorted(head_num, 15)
print(_list_output(head_num))

head_num = insert_sorted(head_num, 10)
print(_list_output(head_num))

print("--------------------------------------------------------------------")
print("   3 -> 3 -> 4 -> 5 -> 6 -> 8 -> 10 -> 15 -> 15")
print("--------------------------------------------------------------------")

head_num = insert_sorted(head_num, 3)
print(_list_output(head_num))

head_num = insert_sorted(head_num, 8)
print(_list_output(head_num))

head_num = insert_sorted(head_num, 6)
print(_list_output(head_num))


#II) Ensure that the list is singly-linked and in order
print("--------------------------------------------------------------------")
print("#II) Ensure that the list is singly-linked and in order")
print("--------------------------------------------------------------------")

print("Singly-Linked:\t\t" + str(_list_valid(head_num, type(Node()))))
print("Ordered Correctly:\t" + str(_list_ordered(head_num)))




#III) Test the elements from the insert_sorted function for strs
print("--------------------------------------------------------------------")
print("IIII) Test the elements from the insert_sorted function for strs")
print("--------------------------------------------------------------------")
print("   Elvis -> Superman -> Yoda")
print("--------------------------------------------------------------------")

#Empty
head_str = insert_sorted(None, "Elvis")
print(_list_output(head_str))

#End
head_str = insert_sorted(head_str, "Superman")
print(_list_output(head_str))

#End
head_str = insert_sorted(head_str, "Yoda")
print(_list_output(head_str))



print("--------------------------------------------------------------------")
print("   Alf -> Chewie -> E.T. -> Elvis -> Superman -> Xenomorph -> Yoda")
print("--------------------------------------------------------------------")

#Front
head_str = insert_sorted(head_str, "E.T.")
print(_list_output(head_str))

#Front
head_str = insert_sorted(head_str, "Alf")
print(_list_output(head_str))

#Middle
head_str = insert_sorted(head_str, "Xenomorph")
print(_list_output(head_str))

#Middle
head_str = insert_sorted(head_str, "Chewie")
print(_list_output(head_str))




#IV) Ensure that the list is singly-linked and in order
print("--------------------------------------------------------------------")
print("#IV) Ensure that the list is singly-linked and in order")
print("--------------------------------------------------------------------")

print("Singly-Linked:\t\t" + str(_list_valid(head_str, type(Node()))))
print("Ordered Correctly:\t" + str(_list_ordered(head_str)))




#V) Test the elements from the combine_sorted function
print("--------------------------------------------------------------------")
print("V) Test the elements from the combine_sorted function")
print("--------------------------------------------------------------------")
print("   list1:\t3 -> 6 -> 7 -> 9 -> 10")
print("   list2:\t1 -> 2 -> 5 -> 8 -> 9")
print("--------------------------------------------------------------------")

list01_1 = Node(3, Node(6, Node(7, Node(9, Node(10, None)))))
list01_2 = Node(1, Node(2, Node(5, Node(8, Node(9, None)))))

print('Standard')
print('list1')
print(_list_output(list01_1))
print('list2')
print(_list_output(list01_2))
print('ProblemStandard')
dlist01_num = combine_sorted(list01_1, list01_2)
print(_list_output(dlist01_num))

input()
print("--------------------------------------------------------------------")

print('Reversed')
print('list1')
print(_list_output(list01_1))
print('list2')
print(_list_output(list01_2))
print('ProblemReversed')
dlist02_num = combine_sorted(list01_2, list01_1)
print(_list_output(dlist02_num))

input()
print("--------------------------------------------------------------------")

list01_1 = Node(3, Node(6, Node(7, Node(9, Node(10, None)))))
list01_2 = Node(1, Node(2, Node(5, Node(8, Node(9, None)))))
print('List 2 empty')
dlist03_num = combine_sorted(list01_1, None)
print(_list_output(dlist03_num))

input()
print("--------------------------------------------------------------------")

print('List 1 empty')
dlist04_num = combine_sorted(None, list01_2)
print(_list_output(dlist04_num))

input()
print("--------------------------------------------------------------------\n")

print('Both lists empty')
dlist05_num = combine_sorted(None, None)
print(dlist05_num)

input()


#VI) Ensure that the lists is doubly-linked and in order
print("--------------------------------------------------------------------")
print("#VI) Ensure that the lists is doubly-linked and in order")
print("--------------------------------------------------------------------")

print("Doubly-Linked:\t" + str(_list_valid(dlist01_num, type(DNode()))))
print("\t\t" + str(_list_valid(dlist02_num, type(DNode()))))
print("\t\t" + str(_list_valid(dlist03_num, type(DNode()))))
print("\t\t" + str(_list_valid(dlist04_num, type(DNode()))))
print("\t\t" + str(_list_valid(dlist05_num, type(DNode()))))

print()

print("Ordered Correctly:\t" + str(_list_ordered(dlist01_num)))
print("\t\t\t" + str(_list_ordered(dlist02_num)))
print("\t\t\t" + str(_list_ordered(dlist03_num)))
print("\t\t\t" + str(_list_ordered(dlist04_num)))
print("\t\t\t" + str(_list_ordered(dlist05_num)))

input()


#VII) Test the elements from the combine_sorted function
print("--------------------------------------------------------------------")
print("VII) Test the elements from the combine_sorted function")
print("--------------------------------------------------------------------")
print("   list1:\tConnery -> Elba -> Moore -> Old Connery")
print("   list2:\tAllen -> Brosnan -> Craig -> Dalton -> Lazenby")
print("--------------------------------------------------------------------")

list02_1 = Node("Connery", Node("Elba", Node("Moore", Node("Old Connery", None))))
list02_2 = Node("Allen", Node("Brosnan", Node("Craig", Node("Dalton", Node("Lazenby", None)))))

#Standard
dlist01_str = combine_sorted(list02_1, list02_2)
print(_list_output(dlist01_str))

input()
print("--------------------------------------------------------------------")

#Reversed
dlist02_str = combine_sorted(list02_2, list02_1)
print(_list_output(dlist02_str))

input()
print("--------------------------------------------------------------------")

#List 2 empty
dlist03_str = combine_sorted(list02_1, None)
print(_list_output(dlist03_str))

input()
print("--------------------------------------------------------------------")

#List 1 empty
dlist04_str = combine_sorted(None, list02_2)
print(_list_output(dlist04_str))

input()


#VIII) Ensure that the lists is doubly-linked and in order
print("--------------------------------------------------------------------")
print("#VIII) Ensure that the lists is doubly-linked and in order")
print("--------------------------------------------------------------------")

print("Doubly-Linked:\t" + str(_list_valid(dlist01_str, type(DNode()))))
print("\t\t" + str(_list_valid(dlist02_str, type(DNode()))))
print("\t\t" + str(_list_valid(dlist03_str, type(DNode()))))
print("\t\t" + str(_list_valid(dlist04_str, type(DNode()))))

print()

print("Ordered Correctly:\t" + str(_list_ordered(dlist01_str)))
print("\t\t\t" + str(_list_ordered(dlist02_str)))
print("\t\t\t" + str(_list_ordered(dlist03_str)))
print("\t\t\t" + str(_list_ordered(dlist04_str)))

input()


#IX) Check that the previous links of the lists are populated
print("--------------------------------------------------------------------")
print("#IX) Check that the previous links of the lists are populated")
print("--------------------------------------------------------------------")
print("   10 -> 9 -> 9 -> 8 -> 7 -> 6 -> 5 -> 3 -> 2 -> 1")
print("--------------------------------------------------------------------")

dlist01_num_tail = dlist01_num.get_next().get_next().get_next().get_next().get_next().get_next().get_next().get_next().get_next()

output_string = "Linked List\n------------------\n"
while not dlist01_num_tail is None:
    print(dlist01_num_tail.get_element())
    dlist01_num_tail = dlist01_num_tail.get_previous()
print("Done!\n")

input()
print("--------------------------------------------------------------------")
print("   Old Connery -> Moore -> Lazenby -> Elba -> Dalton -> Craig ->")
print("        Connery -> Brosnan -> Allen")
print("--------------------------------------------------------------------")

dlist01_str_tail = dlist01_str.get_next().get_next().get_next().get_next().get_next().get_next().get_next().get_next()

output_string = "Linked List\n------------------\n"
while not dlist01_str_tail is None:
    print(dlist01_str_tail.get_element())
    dlist01_str_tail = dlist01_str_tail.get_previous()
print("Done!\n")

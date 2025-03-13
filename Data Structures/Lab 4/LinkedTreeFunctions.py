# Matthew Sabo
# 272155
# CISC 160-02
# Lab 04

from Binary_Node import BinaryNode
'''
Function which takes the root node of a sorted binary tree and an element.
  This function finds where in the binary tree that the element should be
  inserted (by using the algorithm provided in the lab booklet) so that the
  the tree stays in order.
PARAM:   root_node      The root of the linked list
PARAM:   new_element    The new element to be added into the list
RETURNS: The node at the root of the sorted binary tree.
'''
def insert(root_node, new_element):
  if root_node is None: #Checks if the root_node is None
    root_node = BinaryNode(new_element) # Creates new node with new element and sets it as the root
    return root_node
  else:
    if new_element < root_node.get_element():
      if root_node.get_left() is None: #Checks if the left side of the tree has a node
        newNode = BinaryNode(new_element)
        root_node.set_left(newNode)
        newNode.set_parent(root_node)
      else: # If the left side has a node then it calls the insert function with the root now being at that node
        root_node.set_left(insert(root_node.get_left(), new_element)) 
    else:
      if root_node.get_right() is None: #Checks if the right side of tree has a node
        newNode = BinaryNode(new_element)
        root_node.set_right(newNode)
        newNode.set_parent(root_node)
      else: #If the right side has a node then it calls the insert function with the root now being at that node
        root_node.set_right(insert(root_node.get_right(), new_element)) 

  return root_node


'''
Function which takes the root node of a binary tree and prints the tree using
  inorder traversal. Inorder traversal prints the left subtree first, then
  prints the element in the current node, then prints the right subtree.
PARAM:   root_node      The root of the linked list
'''
def _print_tree_inorder(root_node):
  if root_node is None: #If the tree doesnt have any values it returns None
    return
  _print_tree_inorder(root_node.get_left()) # recursively goes down left side of the list and prints the element of each node
  print(root_node.get_element())
  _print_tree_inorder(root_node.get_right())# recursively goes down the right side of the list and then prints the element of each node
    

'''
Function which takes the root node of a sorted binary tree and an element.
  This function searchs the tree for that element using an iterative
  methodology. As it goes, the function creates a path of element in the nodes
  traversed and returns that path at the end.
PARAM:   root_node      The root of the linked list
PARAM:   element        The element to be found in the tree
RETURNS: The path through the tree from the root to the element's node, or
           None if the element cannot be found in the tree.
'''
def _iterative_path_helper(root_node, element, path): #Helper Function to do the logic for iterative path
  if root_node is None: #Checks if the root is none at startup
    return 
  else:
    while root_node is not None: #Runs while the root is not none but stops when tree has no more values
      path.append(root_node.get_element()) #adds element of root node to the list
      if root_node.get_element() == element: #Checks if the element of the current node equals the element
        return path
      elif root_node.get_element() < element: #If element is greater than the node then it changes the root_node to the right node
        root_node = root_node.get_right()
      else: # If element is less than the current node then it changes root_node to the left
        root_node = root_node.get_left()
    return path # if the while loop breaks then this runs. Only runs if element is not in tree
  

def iterative_path(root_node, element):
  path = []
  _iterative_path_helper(root_node, element, path) #Calls on the helper function to do logic
  if path[len(path)-1] == element:#Checks if the last element in the list is equal to element
      return path 
  else: #If element is not in the list then it returns None
    return None 
  
'''
Function which takes the root node of a sorted binary tree and an element.
  This function searchs the tree for that element using a recursive
  methodology. As it goes, the function creates a path of element in the nodes
  traversed and returns that path at the end.
PARAM:   root_node      The root of the linked list
PARAM:   element        The element to be found in the tree
RETURNS: The path through the tree from the root to the element's node, or
           None if the element cannot be found in the tree.
'''

def _recursive_path_helper(root_node, element, path, foundElement):
  if root_node is None or foundElement is True:#Runs if root_node is not a node or 
    return
  else:
    path.append(root_node.get_element())
    if root_node.get_element() == element: 
      foundElement = True
      return path
    elif root_node.get_element() < element: #Checks if the value of root_node is less than element
      _recursive_path_helper(root_node.get_right(), element, path, foundElement)#Calls itself and moves root_node to the right child
    else: #Runs if the value of root_node is more than the element
      _recursive_path_helper(root_node.get_left(),element, path, foundElement)#Calls itself and moves root_node to the left child


def recursive_path(root_node, element):
    path = []
    foundElement = False
    _recursive_path_helper(root_node, element, path, foundElement)#Calls on helper function to do logic
    if path[len(path)-1] == element:#Checks last value of list to see if it equals the element
      return path
    else: #If the element is not in the list then it returns None
      return None

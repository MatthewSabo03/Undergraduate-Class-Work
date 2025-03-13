# CISC 233 LAB 4 Self-Balancing Binary Search Trees
# Author: Matthew Sabo
# Date Created: 3/21/2023
# Last Modified: 3/31/2023

import random
import sys

rotation_count = 0

'''
RedBlackTree Implementation pulled from https://favtutor.com/blogs/red-black-tree-python
'''

# Define Node
class Node():
	def __init__(self,val):
		self.val = val                                   # Value of Node
		self.parent = None                               # Parent of Node
		self.left = None                                 # Left Child of Node
		self.right = None                                # Right Child of Node
		self.color = 1                                   # Red Node as new node is always inserted as Red Node

# Define R-B Tree
class RBTree():

	def __init__(self):
		self.NULL = Node ( 0 )
		self.NULL.color = 0
		self.NULL.left = None
		self.NULL.right = None
		self.root = self.NULL

	# Insert New Node
	def insertNode(self, key):
		node = Node(key)
		node.parent = None
		node.val = key
		node.left = self.NULL
		node.right = self.NULL
		#Sets root colour as Red
		node.color = 1 

		y = None
		x = self.root

		# Find position for new node
		while x != self.NULL :
			y = x
			if node.val < x.val :
				x = x.left
			else :
				x = x.right

		# Set parent of Node as y
		node.parent = y

		# If parent i.e, is none then it is root node
		if y == None :
			self.root = node
		# Check if it is right Node or Left Node by checking the value
		elif node.val < y.val :
			y.left = node
		else :
			y.right = node

		# Root node is always Black
		if node.parent == None :
			node.color = 0
			return

		# If parent of node is Root Node
		if node.parent.parent == None :
			return

		# Else call for Fix Up
		self.fixInsert ( node )


	def minimum(self, node):
		while node.left != self.NULL:
			node = node.left
		return node

	# Code for left rotate
	def LR ( self , x ) :
		global rotation_count
		# Y = Right child of x
		y = x.right
		# Change right child of x to left child of y
		x.right = y.left
		if y.left != self.NULL :
			y.left.parent = x
		
		# Change parent of y as parent of x
		y.parent = x.parent
		
		# If parent of x == None ie. root node
		if x.parent == None :
			# Set y as root
			self.root = y      
		elif x == x.parent.left :
			x.parent.left = y
		else :
			x.parent.right = y
		y.left = x
		x.parent = y
		
		rotation_count +=1

	# Code for right rotate
	def RR ( self , x ) :
		global rotation_count
		# Y = Left child of x
		y = x.left         
		# Change left child of x to right child of y
		x.left = y.right   
		if y.right != self.NULL :
			y.right.parent = x

		# Change parent of y as parent of x
		y.parent = x.parent
		
		# If x is root node 
		if x.parent == None :    
			# Set y as root
			self.root = y        
		elif x == x.parent.right :
			x.parent.right = y
		else :
			x.parent.left = y
		y.right = x
		x.parent = y
		rotation_count += 1

	# Fix Up Insertion
	def fixInsert(self, k):
		#While parent is red
		while k.parent.color == 1:
			#If parent is right child of its parent
			if k.parent == k.parent.parent.right:
				#Left child of grandparent
				u = k.parent.parent.left
				#if color of left child of grandparent i.e, uncle node is red
				if u.color == 1:
					#Set both children of grandparent as black
					u.color = 0
					k.parent.color = 0
					#Set grandparent node as Red
					k.parent.parent.color = 1
					#repeat the algorithm with parent node to check conflicts
					k = k.parent.parent
				else:
					#If k is left child of it's parent
					if k == k.parent.left:                # If k is left child of it's parent
						k = k.parent
						self.RR(k)                        # Call for right rotation
					k.parent.color = 0
					k.parent.parent.color = 1
					self.LR(k.parent.parent)

			#If parent is left child of its parent
			else:
				#Right child of grandparent
				u = k.parent.parent.right
				
				#If color of right child of grandparent i.e, uncle node is red
				if u.color == 1:
					#Set color of childs as black
					u.color = 0
					k.parent.color = 0
					
					#set color of grandparent as Red
					k.parent.parent.color = 1

					#Repeat Algorithm on grandparent to remove conflicts
					k = k.parent.parent
				
				else:
					#If k is right child of its parent
					if k == k.parent.right:
						k = k.parent
						#Call left rotate on parent of k
						self.LR(k)
					k.parent.color = 0
					k.parent.parent.color = 1
					#Call right rotate on grandparent
					self.RR(k.parent.parent)

			#If k reaches root then break        
			if k == self.root:
				break

		#Set color of root as black
		self.root.color = 0

	# Function to fix issues after deletion
	def fixDelete ( self , x ) :
		while x != self.root and x.color == 0 :           # Repeat until x reaches nodes and color of x is black
			if x == x.parent.left :                       # If x is left child of its parent
				s = x.parent.right                        # Sibling of x
				if s.color == 1 :                         # if sibling is red
					s.color = 0                           # Set its color to black
					x.parent.color = 1                    # Make its parent red
					self.LR ( x.parent )                  # Call for left rotate on parent of x
					s = x.parent.right
				
				# If both the child are black
				if s.left.color == 0 and s.right.color == 0 :
					s.color = 1                           # Set color of s as red
					x = x.parent
				
				else :
					if s.right.color == 0 :               # If right child of s is black
						s.left.color = 0                  # set left child of s as black
						s.color = 1                       # set color of s as red
						self.RR ( s )                     # call right rotation on x
						s = x.parent.right

					s.color = x.parent.color
					x.parent.color = 0                    # Set parent of x as black
					s.right.color = 0
					self.LR ( x.parent )                  # call left rotation on parent of x
					x = self.root
			
			else :                                        # If x is right child of its parent
				s = x.parent.left                         # Sibling of x
				if s.color == 1 :                         # if sibling is red
					s.color = 0                           # Set its color to black
					x.parent.color = 1                    # Make its parent red
					self.RR ( x.parent )                  # Call for right rotate on parent of x
					s = x.parent.left

				if s.right.color == 0 and s.right.color == 0 :
					s.color = 1
					x = x.parent
				
				else :
					if s.left.color == 0 :                # If left child of s is black
						s.right.color = 0                 # set right child of s as black
						s.color = 1
						self.LR ( s )                     # call left rotation on x
						s = x.parent.left

					s.color = x.parent.color
					x.parent.color = 0
					s.left.color = 0
					self.RR ( x.parent )
					x = self.root
		x.color = 0

	# Function to transplant nodes
	def __rb_transplant ( self , u , v ) :
		if u.parent == None :
			self.root = v
		elif u == u.parent.left :
			u.parent.left = v
		else :
			u.parent.right = v
		v.parent = u.parent

	# Function to handle deletion
	def delete_node_helper ( self , node , key ) :
		z = self.NULL
		while node != self.NULL :                          # Search for the node having that value/ key and store it in 'z'
			if node.val == key :
				z = node

			if node.val <= key :
				node = node.right
			else :
				node = node.left

		if z == self.NULL :                                # If Kwy is not present then deletion not possible so return
			print ( "Value not present in Tree !!" )
			return

		y = z
		y_original_color = y.color                          # Store the color of z- node
		if z.left == self.NULL :                            # If left child of z is NULL
			x = z.right                                     # Assign right child of z to x
			self.__rb_transplant ( z , z.right )            # Transplant Node to be deleted with x
		elif (z.right == self.NULL) :                       # If right child of z is NULL
			x = z.left                                      # Assign left child of z to x
			self.__rb_transplant ( z , z.left )             # Transplant Node to be deleted with x
		else :                                              # If z has both the child nodes
			y = self.minimum ( z.right )                    # Find minimum of the right sub tree
			y_original_color = y.color                      # Store color of y
			x = y.right
			if y.parent == z :                              # If y is child of z
				x.parent = y                                # Set parent of x as y
			else :
				self.__rb_transplant ( y , y.right )
				y.right = z.right
				y.right.parent = y

			self.__rb_transplant ( z , y )
			y.left = z.left
			y.left.parent = y
			y.color = z.color
		if y_original_color == 0 :                          # If color is black then fixing is needed
			self.fixDelete ( x )

	#Function to handle in order traversal of node
	def in_order_helper(self, node):
		if node != self.NULL:
			self.in_order_helper(node.left)
			print(node.val, end=" ")
			self.in_order_helper(node.right)
			
	# Deletion of node
	def delete_node ( self , val ) :
		self.delete_node_helper ( self.root , val )         # Call for deletion

	#In order Traversal of tree
	def inorder(self):
		self.in_order_helper(self.root)
	
	# Function to print
	def __printCall ( self , node , indent , last ) :
		if node != self.NULL :
			print(indent, end=' ')
			if last :
				print ("R----",end= ' ')
				indent += "     "
			else :
				print("L----",end=' ')
				indent += "|    "

			s_color = "RED" if node.color == 1 else "BLACK"
			print ( str ( node.val ) + "(" + s_color + ")" )
			self.__printCall ( node.left , indent , False )
			self.__printCall ( node.right , indent , True )

	# Function to call print
	def print_tree ( self ) :
		self.__printCall ( self.root , "" , True )

'''
AVL Tree implementation pulled from https://www.programiz.com/dsa/avl-tree
'''

# Create a tree node
class TreeNode(object):
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None
		self.height = 1
	
class AVLTree(object):

	# Function to insert a node
	def insert_node(self, root, key):

		# Find the correct location and insert the node
		if not root:
			return TreeNode(key)
		elif key < root.key:
			root.left = self.insert_node(root.left, key)
		else:
			root.right = self.insert_node(root.right, key)

		root.height = 1 + max(self.getHeight(root.left),
							  self.getHeight(root.right))

		# Update the balance factor and balance the tree
		balanceFactor = self.getBalance(root)
		if balanceFactor > 1:
			if key < root.left.key:
				return self.rightRotate(root)
			else:
				root.left = self.leftRotate(root.left)
				return self.rightRotate(root)

		if balanceFactor < -1:
			if key > root.right.key:
				return self.leftRotate(root)
			else:
				root.right = self.rightRotate(root.right)
				return self.leftRotate(root)

		return root

	# Function to delete a node
	def delete_node(self, root, key):

		# Find the node to be deleted and remove it
		if not root:
			return root
		elif key < root.key:
			root.left = self.delete_node(root.left, key)
		elif key > root.key:
			root.right = self.delete_node(root.right, key)
		else:
			if root.left is None:
				temp = root.right
				root = None
				return temp
			elif root.right is None:
				temp = root.left
				root = None
				return temp
			temp = self.getMinValueNode(root.right)
			root.key = temp.key
			root.right = self.delete_node(root.right,
										  temp.key)
		if root is None:
			return root

		# Update the balance factor of nodes
		root.height = 1 + max(self.getHeight(root.left),
							  self.getHeight(root.right))

		balanceFactor = self.getBalance(root)

		# Balance the tree
		if balanceFactor > 1:
			if self.getBalance(root.left) >= 0:
				return self.rightRotate(root)
			else:
				root.left = self.leftRotate(root.left)
				return self.rightRotate(root)
		if balanceFactor < -1:
			if self.getBalance(root.right) <= 0:
				return self.leftRotate(root)
			else:
				root.right = self.rightRotate(root.right)
				return self.leftRotate(root)
		return root

	# Function to perform left rotation
	def leftRotate(self, z):
		global rotation_count
		y = z.right
		T2 = y.left
		y.left = z
		z.right = T2
		z.height = 1 + max(self.getHeight(z.left),
						   self.getHeight(z.right))
		y.height = 1 + max(self.getHeight(y.left),
						   self.getHeight(y.right))
		rotation_count += 1
		return y

	# Function to perform right rotation
	def rightRotate(self, z):
		global rotation_count
		y = z.left
		T3 = y.right
		y.right = z
		z.left = T3
		z.height = 1 + max(self.getHeight(z.left),
						   self.getHeight(z.right))
		y.height = 1 + max(self.getHeight(y.left),
						   self.getHeight(y.right))
		rotation_count += 1
		return y

	# Get the height of the node
	def getHeight(self, root):
		if not root:
			return 0
		return root.height

	# Get balance factore of the node
	def getBalance(self, root):
		if not root:
			return 0
		return self.getHeight(root.left) - self.getHeight(root.right)

	def getMinValueNode(self, root):
		if root is None or root.left is None:
			return root
		return self.getMinValueNode(root.left)

	def preOrder(self, root):
		if not root:
			return
		print("{0} ".format(root.key), end="")
		self.preOrder(root.left)
		self.preOrder(root.right)
	
	def inOrder(self, root):
		if not root:
			return
		self.inOrder(root.left)
		print(root.key, end=" ")
		self.inOrder(root.right)

	# Print the tree
	def printHelper(self, currPtr, indent, last):
		if currPtr != None:
			sys.stdout.write(indent)
			if last:
				sys.stdout.write("R----")
				indent += "     "
			else:
				sys.stdout.write("L----")
				indent += "|    "
			print(currPtr.key)
			self.printHelper(currPtr.left, indent, False)
			self.printHelper(currPtr.right, indent, True)
	
	def print_tree(self, root):
		self.printHelper(root, "", True)

'''
Functions that define input and output
'''
def randomInsertRB(num, tree):
	global rotation_count
	rotation_count = 0
	randombst = RBTree()
	list = random.sample(range(0, num),num)
	for x in list:
		randombst.insertNode(x)
	if tree is True:
		print('Random Order RB with length of :', num)
		randombst.print_tree()
	else:
		print('Random Order RB with length of :', num)
		randombst.inorder()
		print()
		print()

def reverseInsertRB(num, tree):
	global rotation_count
	rotation_count = 0
	reversebst = RBTree()
	list = random.sample(range(0, num),num)
	list.sort(reverse=True)
	for x in list:
		reversebst.insertNode(x)
	if tree is True:
		print('Reverse Order RB with length of :', num)
		reversebst.print_tree()
	else:
		print('Reverse Order RB with length of :', num)
		reversebst.inorder()
		print()
		print()

def inOrderInsertRB(num, tree):
	global rotation_count
	rotation_count = 0
	inOrderbst = RBTree()
	list = random.sample(range(0, num),num)
	list.sort()
	for x in list:
		inOrderbst.insertNode(x)
	if tree is True:
		print('In Order RB with length of :', num)
		inOrderbst.print_tree()
	else:
		print('In Order RB with length of :', num)
		inOrderbst.inorder()
		print()
		print()

def randomInsertAVL(num, tree):
	global rotation_count
	rotation_count = 0
	randomavl = AVLTree()
	root = None
	list = random.sample(range(0, num),num)
	for x in list:
		root = randomavl.insert_node(root, x)
	if tree is True:
		print('Random Order AVL with length of :', num)
		randomavl.print_tree(root)
	else:
		print('Random Order AVL with length of :', num)
		randomavl.inOrder(root)
		print()
		print()

def reverseInsertAVL(num, tree):
	global rotation_count
	rotation_count = 0
	reverseavl = AVLTree()
	root = None
	list = random.sample(range(0, num),num)
	list.sort(reverse=True)
	for x in list:
		root = reverseavl.insert_node(root, x)
	if tree is True:
		print('Reverse Order AVL with length of :', num)
		reverseavl.print_tree(root)
	else:
		print('Random Order AVL with length of :', num)
		reverseavl.inOrder(root)
		print()
		print()

def inOrderInsertAVL(num, tree):
	global rotation_count
	rotation_count = 0
	inOrderavl = AVLTree()
	root = None
	list = random.sample(range(0, num),num)
	list.sort()
	for x in list:
		root = inOrderavl.insert_node(root, x)
	if tree is True:
		print('Random Order AVL with length of :', num)
		inOrderavl.print_tree(root)
	else:
		print('Random Order AVL with length of :', num)
		inOrderavl.inOrder(root)
		print()
		print()

def randomInsertAlg(num):
	global rotation_count
	rotation_count = 0
	list = random.sample(range(0, num),num)
	
	randomtreerb = RBTree()
	for x in list:
		randomtreerb.insertNode(x)
	print('Balancing Algorithm : Red-Black')
	print('Data Size :', num)
	print('Insertion Order : Random Insert')
	print('Number of Rotations Performed :', rotation_count)
	print()

	randomtreeavl = AVLTree()
	rotation_count = 0
	root = None
	for x in list:
		root = randomtreeavl.insert_node(root, x)
	print('Balancing Algorithm : AVL')
	print('Data Size :', num)
	print('Insertion Order : Random Insert')
	print('Number of Rotations Performed :', rotation_count)
	print()

def reverseInsertAlg(num):
	global rotation_count
	rotation_count = 0
	list = random.sample(range(0, num),num)
	list.sort(reverse=True)
	
	reversetreerb = RBTree()
	for x in list:
		reversetreerb.insertNode(x)
	print('Balancing Algorithm : Red-Black')
	print('Data Size :', num)
	print('Insertion Order : Reverse Insert')
	print('Number of Rotations Performed :', rotation_count)
	print()

	reversetreeavl = AVLTree()
	rotation_count = 0
	root = None
	for x in list:
		root = reversetreeavl.insert_node(root, x)
	print('Balancing Algorithm : AVL')
	print('Data Size :', num)
	print('Insertion Order : Reverse Insert')
	print('Number of Rotations Performed :', rotation_count)
	print()

def inOrderInsertAlg(num):
	global rotation_count
	rotation_count = 0
	list = random.sample(range(0, num),num)
	list.sort()
	
	reversetreerb = RBTree()
	for x in list:
		reversetreerb.insertNode(x)
	print('Balancing Algorithm : Red-Black')
	print('Data Size :', num)
	print('Insertion Order : In-Order Insert')
	print('Number of Rotations Performed :', rotation_count)
	print()

	reversetreeavl = AVLTree()
	rotation_count = 0
	root = None
	for x in list:
		root = reversetreeavl.insert_node(root, x)
	print('Balancing Algorithm : AVL')
	print('Data Size :', num)
	print('Insertion Order : In-Order Insert')
	print('Number of Rotations Performed :', rotation_count)
	print()


if __name__ == "__main__":
	#Task 1 Output
	print("------")
	print("TASK 1")
	print("------")
	randomInsertRB(32, True)
	reverseInsertRB(32, True)
	inOrderInsertRB(32, True)

	randomInsertRB(256, False)
	reverseInsertRB(256, False)
	inOrderInsertRB(256, False)
	
	#Task 2 Output
	print("------")
	print("TASK 2")
	print("------")
	randomInsertAVL(32, True)
	reverseInsertAVL(32, True)
	inOrderInsertAVL(32, True)
	
	randomInsertAVL(256, False)
	reverseInsertAVL(256, False)
	inOrderInsertAVL(256, False)

	#Task 3 Output
	print("------")
	print("TASK 3")
	print("------")
	randomInsertAlg(256)
	reverseInsertAlg(256)
	inOrderInsertAlg(256)

	randomInsertAlg(1024)
	reverseInsertAlg(1024)
	inOrderInsertAlg(1024)

	randomInsertAlg(2048)
	reverseInsertAlg(2048)
	inOrderInsertAlg(2048)
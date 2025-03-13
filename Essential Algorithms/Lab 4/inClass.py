from random import sample

TAB = '   '
step_count = 0

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A utility function to insert a new node with the given key
def insert(root, key):
    global step_count
    step_count += 1
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


# A utility function to do inorder tree traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


# Utility to display tree structure, with tree tipped to the left, with root at the left side
def display_tree(node, indent=0):
    if node:
        display_tree(node.right, indent+1)
        print(TAB*indent, node.val)
        display_tree(node.left, indent+1)


#Defines types of lists that can be sorted
balanced_list = [50, 30, 20, 40, 70, 60, 80]
inorder_list = [20, 30, 40, 50, 60, 70, 80]
reverse_list = [x for x in range(80, 10, -5)]
random_list = sample(range(0, 100), 15)

step_count = 0
r = None
for element in random_list:
    r = insert(r, element)


# Print inoder traversal of the BST
inorder(r)

print()
display_tree(r)

print()
print('average steps to insert: ', step_count/len(random_list))
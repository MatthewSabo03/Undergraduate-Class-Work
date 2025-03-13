'''
' Tester code for Lab 04.
'''

from Binary_Node import BinaryNode
from LinkedTreeFunctions import (_print_tree_inorder, insert, iterative_path,
                                 recursive_path)

pause = False

#I) Test the BinaryNode object
print("-------------------------------------------")
print("I) Test the BinaryNode object")
print("-------------------------------------------")

b1 = BinaryNode(10)
b3 = BinaryNode(30)
b4 = BinaryNode(40)
b5 = BinaryNode(50)
b6 = BinaryNode("Taco")

b2 = BinaryNode(20, b1, b4, b5)

b1.set_left(b2)

b1.set_right(b3)
b3.set_parent(b1)

b2.set_right(b5)

b3.set_left(b6)
b6.set_parent(b3)

print("b2 neighbors:\tparent:\t\t10 = " + str(b2.get_parent().get_element()))
print("\t\tleft child:\t40 = " + str(b2.get_left().get_element()))
print("\t\tleft child:\t50 = " + str(b2.get_right().get_element()))
print("10:\t" + str(b1.get_element()))
print("20:\t" + str(b1.get_left().get_element()))
print("30:\t" + str(b1.get_right().get_element()))
print("10:\t" + str(b1.get_left().get_parent().get_element()))
print("10:\t" + str(b1.get_right().get_parent().get_element()))
print("50:\t" + str(b1.get_right().get_parent().get_left().get_right().get_element()))
print("Taco:\t" + str(b1.get_left().get_parent().get_right().get_left().get_element()))

if pause:
    input()

#II) Test the insert function with integers
print("-------------------------------------------")
print("II) Test the insert function with integers")
print("-------------------------------------------")
print("                          10")
print("                       /      \\")
print("                     5          15")
print("                   /   \\      /    \\")
print("                 2       8 12        20")
print("                       /  \\/  \\")
print("                     6    10    13")
print("                                   \\")
print("                                     14")

root = insert(None, 10)
print("| 10 |")
_print_tree_inorder(root)

print("\n-------\n")

root = insert(root, 5)
print("| 5 -> 10 |")
_print_tree_inorder(root)

print("\n-------\n")

root = insert(root, 15)
print("| 5 -> 10 -> 15 |")
_print_tree_inorder(root)

print("\n-------\n")

root = insert(root, 2)
print("| 2 -> 5 -> 10 -> 15 |")
_print_tree_inorder(root)

print("\n-------")

if pause:
    input()

root = insert(root, 20)
print("| 2 -> 5 -> 10 -> 15 -> 20 |")
_print_tree_inorder(root)

print("\n-------\n")

root = insert(root, 12)
print("| 2 -> 5 -> 10 -> 12 -> 15 -> 20 |")
_print_tree_inorder(root)

print("\n-------\n")

root = insert(root, 8)
print("| 2 -> 5 -> 8 -> 10 -> 12 -> 15 -> 20 |")
_print_tree_inorder(root)

print("\n-------")

if pause:
    input()

root = insert(root, 10)
print("| 2 -> 5 -> 8 -> 10 -> 10 -> 12 -> 15 -> 20 |")
_print_tree_inorder(root)

print("\n-------\n")

root = insert(root, 13)
print("| 2 -> 5 -> 8 -> 10 -> 10 -> 12 -> 13 -> 15 -> 20 |")
_print_tree_inorder(root)

print("\n-------")

if pause:
    input()

root = insert(root, 6)
print("| 2 -> 5 -> 6 -> 8 -> 10 -> 10 -> 12 -> 13 -> 15 -> 20 |")
_print_tree_inorder(root)

print("\n-------")

if pause:
    input()

root = insert(root, 14)
print("| 2 -> 5 -> 6 -> 8 -> 10 -> 10 -> 12 -> 13 -> 14 -> 15 -> 20 |")
_print_tree_inorder(root)


if pause:
    input()

#III) Test the insert function with strings
print("-------------------------------------------")
print("III) Test the insert function with strings")
print("-------------------------------------------")
print("                        Louis")
print("                   /             \\")
print("             Dana                  Walter")
print("              \\                 /         \\")
print("               Egon        Peter           Zuul")
print("                 \\         /    \\           /")
print("                Janine   Oscar  Ray      Winston")
print("                 /  \\            \\")
print("             Gozer Janosz       Slimer")
print("                                    \\")
print("                                    Vigo")

root2 = insert(None, "Louis Tully")
print("| Louis Tully |")
_print_tree_inorder(root2)

print("\n-------\n")

root2 = insert(root2, "Walter Peck")
print("| Louis Tully -> Walter Peck |")
_print_tree_inorder(root2)

print("\n-------\n")

root2 = insert(root2, "Dana Barrett")
print("| Dana Barrett -> Louis Tully -> Walter Peck |")
_print_tree_inorder(root2)

print("\n-------\n")

root2 = insert(root2, "Peter Venkman")
print("| Dana Barrett -> Louis Tully -> Peter Venkman -> Walter Peck |")
_print_tree_inorder(root2)

print("\n-------")

if pause:
    input()

root2 = insert(root2, "Ray Stanz")
print("| Dana Barrett -> Louis Tully -> Peter Venkman -> Ray Stanz -> Walter Peck |")
_print_tree_inorder(root2)

print("\n-------\n")

root2 = insert(root2, "Zuul")
print("| Dana Barrett -> Louis Tully -> Peter Venkman -> Ray Stanz -> Walter Peck\n\t-> Zuul |")
_print_tree_inorder(root2)

print("\n-------\n")

root2 = insert(root2, "Egon Spengler")
print("| Dana Barrett -> Egon Spengler -> Louis Tully -> Peter Venkman -> Ray Stanz\n\t-> Walter Peck -> Zuul |")
_print_tree_inorder(root2)

print("\n-------")

if pause:
    input()

root2 = insert(root2, "Winston Zeddemore")
print("| Dana Barrett -> Egon Spengler -> Louis Tully -> Peter Venkman -> Ray Stanz\n\t-> Walter Peck -> Winston Zeddemore -> Zuul |")
_print_tree_inorder(root2)

print("\n-------\n")

root2 = insert(root2, "Janine Melnitz")
print("| Dana Barrett -> Egon Spengler -> Janine Melnitz -> Louis Tully ->\n\tPeter Venkman -> Ray Stanz -> Walter Peck -> Winston Zeddemore -> Zuul |")
_print_tree_inorder(root2)

print("\n-------")

if pause:
    input()

root2 = insert(root2, "Slimer")
print("| Dana Barrett -> Egon Spengler -> Janine Melnitz -> Louis Tully ->\n\tPeter Venkman -> Ray Stanz -> Slimer -> Walter Peck ->\n\tWinston Zeddemore -> Zuul |")
_print_tree_inorder(root2)

print("\n-------\n")

root2 = insert(root2, "Gozer the Gozerian")
print("| Dana Barrett -> Egon Spengler -> Gozer the Gozerian ->\n\tJanine Melnitz -> Louis Tully -> Peter Venkman -> Ray Stanz ->\n\tSlimer -> Walter Peck -> Winston Zeddemore -> Zuul |")
_print_tree_inorder(root2)

print("\n-------")

if pause:
    input()

root2 = insert(root2, "Vigo the Carpathian")
print("| Dana Barrett -> Egon Spengler -> Gozer the Gozerian ->\n\tJanine Melnitz -> Louis Tully -> Peter Venkman -> Ray Stanz ->\n\tSlimer -> Vigo the Carpathian -> Walter Peck -> Winston Zeddemore ->\n\tZuul |")
_print_tree_inorder(root2)

print("\n-------\n")

root2 = insert(root2, "Janosz Poha")
print("| Dana Barrett -> Egon Spengler -> Gozer the Gozerian ->\n\tJanine Melnitz -> Janosz Poha -> Louis Tully -> Peter Venkman ->\n\tRay Stanz -> Slimer -> Vigo the Carpathian -> Walter Peck ->\n\tWinston Zeddemore -> Zuul |")
_print_tree_inorder(root2)

print("\n-------")

if pause:
    input()

root2 = insert(root2, "Oscar")
print("| Dana Barrett -> Egon Spengler -> Gozer the Gozerian ->\n\tJanine Melnitz -> Janosz Poha -> Louis Tully -> Oscar ->\n\tPeter Venkman -> Ray Stanz -> Slimer -> Vigo the Carpathian ->\n\tWalter Peck -> Winston Zeddemore -> Zuul |")
_print_tree_inorder(root2)


if pause:
    input()

#IV) Test the full tree construction
print("-------------------------------------------")
print("#IV) Test the full tree construction")
print("-------------------------------------------")

node13 = root.get_right().get_left().get_right()
print("13:\t" + str(node13.get_element()))
print("12:\t" + str(node13.get_parent().get_element()))
print("15:\t" + str(node13.get_parent().get_parent().get_element()))
print("10:\t" + str(node13.get_parent().get_parent().get_parent().get_element()))
print("None:\t" + str(node13.get_parent().get_parent().get_parent().get_parent()))

print()

nodeGozer  = root2.get_left().get_right().get_right().get_left()
print("Gozer:\t" + str(nodeGozer.get_element()))
print("Janine:\t" + str(nodeGozer.get_parent().get_element()))
print("Egon:\t" + str(nodeGozer.get_parent().get_parent().get_element()))
print("Dana:\t" + str(nodeGozer.get_parent().get_parent().get_parent().get_element()))
print("Louis:\t" + str(nodeGozer.get_parent().get_parent().get_parent().get_parent().get_element()))
print("None:\t" + str(nodeGozer.get_parent().get_parent().get_parent().get_parent().get_parent()))

print()

nodeJanosz = root2.get_left().get_right().get_right().get_right()
print("Janosz:\t" + str(nodeJanosz.get_element()))
print("Janine:\t" + str(nodeJanosz.get_parent().get_element()))
print("Egon:\t" + str(nodeJanosz.get_parent().get_parent().get_element()))
print("Dana:\t" + str(nodeJanosz.get_parent().get_parent().get_parent().get_element()))
print("Louis:\t" + str(nodeJanosz.get_parent().get_parent().get_parent().get_parent().get_element()))
print("None:\t" + str(nodeJanosz.get_parent().get_parent().get_parent().get_parent().get_parent()))

print()

if pause:
    input()

#IV) Test the iterative path function
print("-------------------------------------------")
print("#IV) Test the iterative path function")
print("-------------------------------------------")


print("10, 15, 12, 13, 14\t= " + str(iterative_path(root, 14)))
print("10, 15, 20\t\t= " + str(iterative_path(root, 20)))
print("10, 5, 8, 6\t\t= " + str(iterative_path(root, 6)))
print("10, 5\t\t\t= " + str(iterative_path(root, 5)))
print("10\t\t\t= " + str(iterative_path(root, 10)))
print("None\t\t\t= " + str(iterative_path(root, -1)))
print("None\t\t\t= " + str(iterative_path(root, 11)))
print("None\t\t\t= " + str(iterative_path(root, 19)))
print("None\t\t\t= " + str(iterative_path(root, 21)))

print()

print("Louis, Dana, Egon, Janine, Janosz\n = " + str(iterative_path(root2, "Janosz Poha")) + "\n")
print("Louis, Dana, Egon, Janine, Gozer\n = " + str(iterative_path(root2, "Gozer the Gozerian")) + "\n")
print("Louis, Walter, Peter, Ray, Slimer\n = " + str(iterative_path(root2, "Slimer")) + "\n")
print("Louis, Walter, Peter\n = " + str(iterative_path(root2, "Peter Venkman")) + "\n")
print("Louis, Walter, Zuul, Winston\n = " + str(iterative_path(root2, "Winston Zeddemore")) + "\n")
print("Louis Tully\t\t\t= " + str(iterative_path(root2, "Louis Tully")))
print("None\t\t\t\t= " + str(iterative_path(root2, "Casey Casum")))
print("None\t\t\t\t= " + str(iterative_path(root2, "Larry King")))
print("None\t\t\t\t= " + str(iterative_path(root2, "Bobby Brown")))
print("None\t\t\t\t= " + str(iterative_path(root2, "Cheech Marin")))
print()

if pause:
    input()

#V) Test the recursive path function
print("-------------------------------------------")
print("#V) Test the recursive path function")
print("-------------------------------------------")


print("10, 15, 12, 13, 14\t= " + str(recursive_path(root, 14)))
print("10, 15, 20\t\t= " + str(recursive_path(root, 20)))
print("10, 5, 8, 6\t\t= " + str(recursive_path(root, 6)))
print("10, 5\t\t\t= " + str(recursive_path(root, 5)))
print("10\t\t\t= " + str(recursive_path(root, 10)))
print("None\t\t\t= " + str(recursive_path(root, -1)))
print("None\t\t\t= " + str(recursive_path(root, 11)))
print("None\t\t\t= " + str(recursive_path(root, 19)))
print("None\t\t\t= " + str(recursive_path(root, 21)))

print()

print("Louis, Dana, Egon, Janine, Janosz\n = " + str(recursive_path(root2, "Janosz Poha")) + "\n")
print("Louis, Dana, Egon, Janine, Gozer\n = " + str(recursive_path(root2, "Gozer the Gozerian")) + "\n")
print("Louis, Walter, Peter, Ray, Slimer\n = " + str(recursive_path(root2, "Slimer")) + "\n")
print("Louis, Walter, Peter\n = " + str(recursive_path(root2, "Peter Venkman")) + "\n")
print("Louis, Walter, Zuul, Winston\n = " + str(recursive_path(root2, "Winston Zeddemore")) + "\n")
print("Louis Tully\t\t\t= " + str(recursive_path(root2, "Louis Tully")))
print("None\t\t\t\t= " + str(recursive_path(root2, "Casey Casum")))
print("None\t\t\t\t= " + str(recursive_path(root2, "Larry King")))
print("None\t\t\t\t= " + str(recursive_path(root2, "Bobby Brown")))
print("None\t\t\t\t= " + str(recursive_path(root2, "Cheech Marin")))
print()




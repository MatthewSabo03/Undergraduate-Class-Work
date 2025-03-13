'''
' Tester code for Question 02 (LinkedHeapPQ) of the Final Project.
'''

from LinkedHeapPQ import LinkedHeapPQ

#2.1) Test the LinkedHeapPQ constructor
print("------------------------------------------------------------")
print("2.1) Test the LinkedHeapPQ constructor")
print("------------------------------------------------------------")

pq = LinkedHeapPQ()
pause = False

print("len:      0\t= " + str(len(pq)))
print("is_empty: True\t= " + str(pq.is_empty()))

if pause:
    input()
else:
    print()

#2.2) Test accessing an empty LinkedHeapPQ
print("------------------------------------------------------------")
print("2.2) Test accessing an empty LinkedHeapPQ")
print("------------------------------------------------------------")

try:
    print("None:\t= " + str(pq.min()))
except:
    print("None:\t= None (via exception)")

try:
    print("None:\t= " + str(pq.remove_min()))
except:
    print("None:\t= None (via exception)")

if pause:
    input()
else:
    print()
    
#2.3) Test the LinkedHeapPQ add method with ints as keys
print("------------------------------------------------------------")
print("2.3) Test the LinkedHeapPQ add method with ints keys")
print("------------------------------------------------------------")

pq.add(5, 10)

print("len:      1\t\t\t= " + str(len(pq)))
print("is_empty: False\t\t\t= " + str(pq.is_empty()))
print("min:      (5, 10)\t\t= " + str(pq.min()))
print()

pq.add(2, 1)

print("len:      2\t\t\t= " + str(len(pq)))
print("is_empty: False\t\t\t= " + str(pq.is_empty()))
print("min:      (2, 1)\t\t= " + str(pq.min()))
print()

pq.add(23, "My Password is Taco")

print("len:      3\t\t\t= " + str(len(pq)))
print("is_empty: False\t\t\t= " + str(pq.is_empty()))
print("min:      (2, 1)\t\t= " + str(pq.min()))
print()

pq.add(-10, "Baklava")

print("len:      4\t\t\t= " + str(len(pq)))
print("is_empty: False\t\t\t= " + str(pq.is_empty()))
print("min:      (-10, 'Baklava')\t= " + str(pq.min()))
print()

pq.add(0, "Should be second")

print("len:      5\t\t\t= " + str(len(pq)))
print("is_empty: False\t\t\t= " + str(pq.is_empty()))
print("min:      (-10, 'Baklava')\t= " + str(pq.min()))
print()

pq.add(123, "Last")

print("len:      6\t\t\t= " + str(len(pq)))
print("is_empty: False\t\t\t= " + str(pq.is_empty()))
print("min:      (-10, 'Baklava')\t= " + str(pq.min()))

if pause:
    input()
else:
    print()

pq.add(-5, "Weird, right?")

print("len:      7\t\t\t= " + str(len(pq)))
print("is_empty: False\t\t\t= " + str(pq.is_empty()))
print("min:      (-10, 'Baklava')\t= " + str(pq.min()))
print()

pq.add(0, "Should be first")

print("len:      8\t\t\t= " + str(len(pq)))
print("is_empty: False\t\t\t= " + str(pq.is_empty()))
print("min:      (-10, 'Baklava')\t= " + str(pq.min()))
print()

pq.add(47, 555.55)

print("len:      9\t\t\t= " + str(len(pq)))
print("is_empty: False\t\t\t= " + str(pq.is_empty()))
print("min:      (-10, 'Baklava')\t= " + str(pq.min()))
print()

pq.add(1, ["A", "list", "of", "stuff"])

print("len:      10\t\t\t= " + str(len(pq)))
print("is_empty: False\t\t\t= " + str(pq.is_empty()))
print("min:      (-10, 'Baklava')\t= " + str(pq.min()))
print()

pq.add(-15, "¡Top!")

print("len:      11\t\t\t= " + str(len(pq)))
print("is_empty: False\t\t\t= " + str(pq.is_empty()))
print("min:      (-15, '¡Top!')\t= " + str(pq.min()))
print()

if pause:
    input()
else:
    print()

#2.4) Test the LinkedHeapPQ min and remove_min methods
print("------------------------------------------------------------")
print("2.4) Test the LinkedHeapPQ min and remove_min methods")
print("------------------------------------------------------------")


print("remove_min: (-15, '¡Top!')\t\t= " + str(pq.remove_min()))
print("len:        10\t\t\t\t= " + str(len(pq)))
print("is_empty:   False\t\t\t= " + str(pq.is_empty()))
print()

print("min:        (-10, 'Baklava')\t\t= " + str(pq.min()))
print("remove_min: (-10, 'Baklava')\t\t= " + str(pq.remove_min()))
print("len:        9\t\t\t\t= " + str(len(pq)))
print("is_empty:   False\t\t\t= " + str(pq.is_empty()))
print()

print("min:        (-5, 'Weird, right?')\t= " + str(pq.min()))
print("remove_min: (-5, 'Weird, right?')\t= " + str(pq.remove_min()))
print("len:        8\t\t\t\t= " + str(len(pq)))
print("is_empty:   False\t\t\t= " + str(pq.is_empty()))
print()

print("min:        (0, 'Should be first')\t= " + str(pq.min()))
print("remove_min: (0, 'Should be first')\t= " + str(pq.remove_min()))
print("len:        7\t\t\t\t= " + str(len(pq)))
print("is_empty:   False\t\t\t= " + str(pq.is_empty()))
print()

print("min:        (0, 'Should be second')\t= " + str(pq.min()))
print("remove_min: (0, 'Should be second')\t= " + str(pq.remove_min()))
print("len:        6\t\t\t\t= " + str(len(pq)))
print("is_empty:   False\t\t\t= " + str(pq.is_empty()))

if pause:
    input()
else:
    print()

print("min:        (1, ['A', 'list', 'of', 'stuff'])\n\t  = " + str(pq.min()))
print("remove_min: (1, ['A', 'list', 'of', 'stuff'])\n\t  = " + str(pq.remove_min()))
print("len:        5\t\t\t\t= " + str(len(pq)))
print("is_empty:   False\t\t\t= " + str(pq.is_empty()))
print()

print("min:        (2, 1)\t\t\t= " + str(pq.min()))
print("remove_min: (2, 1)\t\t\t= " + str(pq.remove_min()))
print("len:        4\t\t\t\t= " + str(len(pq)))
print("is_empty:   False\t\t\t= " + str(pq.is_empty()))
print()

print("min:        (5, 10)\t\t\t= " + str(pq.min()))
print("remove_min: (5, 10)\t\t\t= " + str(pq.remove_min()))
print("len:        3\t\t\t\t= " + str(len(pq)))
print("is_empty:   False\t\t\t= " + str(pq.is_empty()))
print()

print("min:        (23, 'My Password is Taco')\t= " + str(pq.min()))
print("remove_min: (23, 'My Password is Taco')\t= " + str(pq.remove_min()))
print("len:        2\t\t\t\t= " + str(len(pq)))
print("is_empty:   False\t\t\t= " + str(pq.is_empty()))
print()

print("min:        (47, 555.55)\t\t= " + str(pq.min()))
print("remove_min: (47, 555.55)\t\t= " + str(pq.remove_min()))
print("len:        1\t\t\t\t= " + str(len(pq)))
print("is_empty:   False\t\t\t= " + str(pq.is_empty()))
print()

print("min:        (123, 'Last')\t\t= " + str(pq.min()))
print("remove_min: (123, 'Last')\t\t= " + str(pq.remove_min()))
print("len:        0\t\t\t\t= " + str(len(pq)))
print("is_empty:   True\t\t\t= " + str(pq.is_empty()))

if pause:
    input()
else:
    print()

#2.5) Test the LinkedHeapPQ add method with floats as keys
print("------------------------------------------------------------")
print("2.5) Test the LinkedHeapPQ add method floats as keys")
print("------------------------------------------------------------")

pq.add(5, 10)
pq.add(2.15, 1)
pq.add(23.5, "My Password is Taco")
pq.add(-10.4, "Baklava")
pq.add(0.6, "Should be second")
pq.add(123.467, "Last")
pq.add(-4.9, "Weird, right?")
pq.add(0.6, "Should be first")
pq.add(47, 555.55)
pq.add(1.0000007, ["A", "list", "of", "stuff"])
pq.add(-14.55, "¡Top!")

print("len:      11\t\t\t= " + str(len(pq)))
print("is_empty: False\t\t\t= " + str(pq.is_empty()))
print("min:      (-14.55, '¡Top!')\t= " + str(pq.min()))
print()

print("remove_min: (-14.55, '¡Top!')\t\t  = " + str(pq.remove_min()))
print("remove_min: (-10.4, 'Baklava')\t\t  = " + str(pq.remove_min()))
print("remove_min: (-4.9, 'Weird, right?')\t  = " + str(pq.remove_min()))
print("remove_min: (0.6, 'Should be first')\t  = " + str(pq.remove_min()))
print("remove_min: (0.6, 'Should be second')\t  = " + str(pq.remove_min()))
print("remove_min: (1.0000007, ['A', 'list', 'of', 'stuff'])\n\t  = " + str(pq.remove_min()))
print("remove_min: (2.15, 1)\t\t\t  = " + str(pq.remove_min()))
print("remove_min: (5, 10)\t\t\t  = " + str(pq.remove_min()))
print("remove_min: (23.5, 'My Password is Taco') = " + str(pq.remove_min()))
print("remove_min: (47, 555.55)\t\t  = " + str(pq.remove_min()))
print("remove_min: (123.467, 'Last')\t\t  = " + str(pq.remove_min()))
print()

print("len:      0\t= " + str(len(pq)))
print("is_empty: True\t= " + str(pq.is_empty()))

try:
    print("min:      None\t= " + str(pq.min()))
except:
    print("min:      None\t= None (via exception)")

if pause:
    input()

#2.6) Test the LinkedHeapPQ add method with strings as keys
print("------------------------------------------------------------")
print("2.6) Test the LinkedHeapPQ add method strings as keys")
print("------------------------------------------------------------")

pq.add("baklava", 10)
pq.add("apescat!", 1)
pq.add("zoo", "My Password is Taco")
pq.add("!2", "Baklava")
pq.add("Apescat!", "Second")
pq.add("æÞëşɔαէ‼֍Ὡ☺☻☼♠♣♥♦", "Last")
pq.add("2.7", "Weird, right?")
pq.add("Apescat!", "First")
pq.add("åpescat!", 555.55)
pq.add("apes", ["A", "list", "of", "stuff"])
pq.add("!!", "¡Top!")

print("len:      11\t\t\t= " + str(len(pq)))
print("is_empty: False\t\t\t= " + str(pq.is_empty()))
print("min:      ('!!', '¡Top!')\t= " + str(pq.min()))
print()

print("remove_min: ('!!', '¡Top!')\t\t  = " + str(pq.remove_min()))
print("remove_min: (!2, 'Baklava')\t\t  = " + str(pq.remove_min()))
print("remove_min: ('2.7', 'Weird, right?')\t  = " + str(pq.remove_min()))
print("remove_min: ('Apescat!', 'First')\t  = " + str(pq.remove_min()))
print("remove_min: ('Apescat!', 'Second')\t  = " + str(pq.remove_min()))
print("remove_min: ('apes', ['A', 'list', 'of', 'stuff'])\n\t  = " + str(pq.remove_min()))
print("remove_min: ('apescat!', 1)\t\t  = " + str(pq.remove_min()))
print("remove_min: ('baklava', 10)\t\t  = " + str(pq.remove_min()))
print("remove_min: ('zoo', 'My Password is Taco')= " + str(pq.remove_min()))
print("remove_min: ('åpescat!', 555.55)\t  = " + str(pq.remove_min()))
print("remove_min: ('æÞëşɔαէ‼֍Ὡ☺☻☼♠♣♥♦', 'Last') = " + str(pq.remove_min()))
print()

print("len:      0\t= " + str(len(pq)))
print("is_empty: True\t= " + str(pq.is_empty()))

try:
    print("min:      None\t= " + str(pq.min()))
except:
    print("min:      None\t= None (via exception)")

if pause:
    input()
else:
    print()

#2.7) Try to test the underlying heap structure. MAY NOT WORK!
print("------------------------------------------------------------")
print("2.7) Try to test the underlying heap structure. MAY NOT WORK!")
print("------------------------------------------------------------")

pq.add(5, 10)
pq.add(2, 1)
pq.add(47, 555.55)
pq.add(23, "My Password is Taco")
pq.add(0, "Should be second")
pq.add(123, "Last")
pq.add(-5, "Weird, right?")
pq.add(0, "Should be first")
pq.add(-10, "Baklava")
pq.add(1, ["A", "list", "of", "stuff"])
pq.add(-15, "¡Top!")

pointer = None

if pointer is None:
    try:
        pointer = pq._head
    except:
        pass

if pointer is None:
    try:
        pointer = pq.head
    except:
        pass

if pointer is None:
    try:
        pointer = pq._head_node
    except:
        pass

if pointer is None:
    try:
        pointer = pq.head_node
    except:
        pass

if pointer is None:
    try:
        pointer = pq._h
    except:
        pass

if pointer is None:
    try:
        pointer = pq.h
    except:
        pass

if pointer is None:
    try:
        pointer = pq._header
    except:
        pass

if pointer is None:
    try:
        pointer = pq.header
    except:
        pass

if pointer is None:
    try:
        pointer = pq._first
    except:
        pass

if pointer is None:
    try:
        pointer = pq.first
    except:
        pass

if pointer is None:
    try:
        pointer = pq._data
    except:
        pass

if pointer is None:
    try:
        pointer = pq.data
    except:
        pass

if pointer == None:
    print("Head node unidentified. Check the internal structure.")
else:
    print("Going forward from the head node")
    print("------------------------------------------------------------")
    print("(-15, '¡Top!')\t\t= " + str(pointer.get_element()))
    pointer = pointer.get_next()
    print("(-10, 'Baklava')\t= " + str(pointer.get_element()))
    pointer = pointer.get_next()
    print("(0, 'Should be first')\t= " + str(pointer.get_element()))
    pointer = pointer.get_next()
    print("(0, 'Should be second')\t= " + str(pointer.get_element()))
    pointer = pointer.get_next()
    print("(-5, 'Weird, right?')\t= " + str(pointer.get_element()))
    pointer = pointer.get_next()
    print("(123, 'Last')\t\t= " + str(pointer.get_element()))
    pointer = pointer.get_next()
    print("(47, 555.55)\t\t= " + str(pointer.get_element()))
    pointer = pointer.get_next()
    print("(23, 'My Password is Taco')\t= " + str(pointer.get_element()))
    pointer = pointer.get_next()
    print("(2, 1)\t\t\t= " + str(pointer.get_element()))
    pointer = pointer.get_next()
    print("(5, 10)\t\t\t= " + str(pointer.get_element()))
    pointer = pointer.get_next()
    print("(1, ['A', 'list', 'of', 'stuff'])\n\t  = " + str(pointer.get_element()))
    print("tail.get_next()\t\t= " + str(pointer.get_next()))

    if pause:
        input()
    else:
        print()
    
    print("------------------------------------------------------------")
    print("Going backward from the tail node")
    print("------------------------------------------------------------")
    print("(1, ['A', 'list', 'of', 'stuff'])\n\t  = " + str(pointer.get_element()))
    pointer = pointer.get_previous()
    print("(5, 10)\t\t\t= " + str(pointer.get_element()))
    pointer = pointer.get_previous()
    print("(2, 1)\t\t\t= " + str(pointer.get_element()))
    pointer = pointer.get_previous()
    print("(23, 'My Password is Taco')\t= " + str(pointer.get_element()))
    pointer = pointer.get_previous()
    print("(47, 555.55)\t\t= " + str(pointer.get_element()))
    pointer = pointer.get_previous()
    print("(123, 'Last')\t\t= " + str(pointer.get_element()))
    pointer = pointer.get_previous()
    print("(-5, 'Weird, right?')\t= " + str(pointer.get_element()))
    pointer = pointer.get_previous()
    print("(0, 'Should be second')\t= " + str(pointer.get_element()))
    pointer = pointer.get_previous()
    print("(0, 'Should be first')\t= " + str(pointer.get_element()))
    pointer = pointer.get_previous()
    print("(-10, 'Baklava')\t= " + str(pointer.get_element()))
    pointer = pointer.get_previous()
    print("(-15, '¡Top!')\t\t= " + str(pointer.get_element()))
    print("head.get_previous()\t= " + str(pointer.get_previous()))

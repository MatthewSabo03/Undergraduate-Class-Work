from Stack_Interface import Stack_Interface
from List_Stack import ListStack
from Queue_Interface import Queue_Interface
from List_Queue import ListQueue
from exceptions import EmptyQueueException 

'''
Function which takes a string and uses a stack to validate if the string,
    without any spaces or punctuation and normalized for capitalization, is a
    palindrome.
RETURNS: True if the string would be considered a palindrome, false otherwise
'''

def is_palindrome_stack(string):
    
    #Initilizes stack and variables needed for function
    rightStack = ListStack()
    leftStack = ListStack()
    i=0
    p=1
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_`¡ '''
    isPalindrome = False

    #Makes string uppercase
    upperString = string.upper()

    #Removes punctuation and spaces from string
    strippedString = upperString.translate(upperString.maketrans('', '', punctuation))

    #Finds what value is in the middle of the list and rounds down
    middleOfList = int(len(strippedString)/2)

    #Splits strippedString into list
    splitString = [x for x in strippedString]

    #Compares each side of the list by each element
    while i<middleOfList:
        while p<(len(splitString)/2):
            leftStack.push(splitString[middleOfList-p]) #Pushes left element onto leftStack
            rightStack.push(splitString[middleOfList+p]) #Pushes right element onto rightStack
            p+=1
        if  leftStack.pop() == rightStack.pop(): #Compares the top of the left and right stacks
            isPalindrome = True
        else:
            isPalindrome = False
            break #Breaks the loop because it is not a palindrome if values dont match
        i+=1

    return isPalindrome

        


'''
Function which takes a string and uses queues to validate if the string,
    without any spaces or punctuation and normalized for capitalization, is a
    palindrome.
RETURNS: True if the string would be considered a palindrome, false otherwise
'''
def is_palindrome_queue(string):
    rightQueue = ListQueue()
    leftQueue = ListQueue()
    i=0
    p=1
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_`¡ '''
    isPalindrome = False

    #Makes string uppercase
    upperString = string.upper()

    #Removes punctuation and spaces from string
    strippedString = upperString.translate(upperString.maketrans('', '', punctuation))

    #Finds what value is in the middle of the list and rounds down
    middleOfList = int(len(strippedString)/2)

    #Splits strippedString into list
    splitString = [x for x in strippedString]

    #Compares each side of the list by each element
    while i<middleOfList:
        while p<(len(splitString)/2):
            leftQueue.enqueue(splitString[middleOfList-p]) #Pushes left element onto leftQueue
            rightQueue.enqueue(splitString[middleOfList+p])#Pushes right element onto rightQueue
            p+=1
        if leftQueue.dequeue() == rightQueue.dequeue(): #Compares the top of the left and right Queues
            isPalindrome = True
        else:
            isPalindrome = False
            break #Breaks the loop because it is not a palindrome if values dont match
        i+=1

    return isPalindrome


'''
Test code can go below if you want
'''
if __name__ == '__main__':
    pass

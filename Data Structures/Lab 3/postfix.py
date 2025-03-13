from List_Stack import ListStack
from exceptions import RPNError

'''
Function which takes a string and uses a stack to calculate the value of the
equation passed in. This equation is assumed to be in postfix/reverse Polish
notation.
RETURNS: The value that the equation evaluates to using postfix notation
'''
def postfix_calculator(string):
    stack = ListStack()
    i=0
    p=0
    numbers = [0,1,2,3,4,5,6,7,8,9]
    operators = ["+","-","*","/"]

    #makes string into list
    splitString = string.split()

    while i<len(splitString):
        if splitString[i].isdigit() or splitString[i] in operators: #Runs if element is valid 
            if splitString[i].isdigit(): #Runs if element is a number
                stack.push(int(splitString[i]))
            else:
                if stack.__len__() >= 2: #Checks if stack has elements
                    first_added = stack.pop() 
                    second_added = stack.pop()
                    if splitString[i] == "+":
                        stack.push(float(second_added+first_added))
                    if splitString[i] == "-":
                        stack.push(float(second_added-first_added))
                    if splitString[i] == "*":
                        stack.push(float(second_added*first_added))
                    if splitString[i] == "/":
                        if first_added == 0:
                            return RPNError("ERROR")
                        else:
                            stack.push(float(second_added/first_added))
                else:
                    return RPNError("ERROR")      
        else: #Runs if element is not valid
            return RPNError("ERROR")
        i+=1

    if stack.__len__() == 1:#Runs after while loop and returns value
        return stack.pop()
    else:
        return RPNError("ERROR")
                    
                
'''
Test code can go below if you want
'''
if __name__ == '__main__':
    pass

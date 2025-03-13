import sys

# Global constants
INPUTS    = ["M", "A", "C"]
MENU_TEXT = ["Month Count", "Analyze Data", "Calclate Expenses"]
FUNCTIONS = ["monthCount()", "analyzeData()", "calculateExpenses()"]
DEBUG     = False

# Global Variables for Data
debitTable = [[]]
netTable = [[]]
deliveredTable = [[]]
receivedTable = [[]]

numberMonths = -1
totalNet = -1
totalDelivered = -1
totalReceived = -1


#---------------------- SETUP FUNCTIONS ----------------------#


#################################################################################
#
#   Function which 
#
#   Precondition:  
#   Precondition:  
#   Precondition:  
#   Postcondition: 
#   Invariant:     
#
#################################################################################
def readFile(fileName):

    #-------- ASSERTION TESTING --------#
    assert isinstance(fileName, str), "File name is not a string"
    #-----------------------------------#

    #I) Get access to necessary global variables
    global DEBUG, debitTable, netTable, deliveredTable, receivedTable
    
    #II) Try to open and use the file
    try:
        inputFile = open(fileName, "r")
        rawData = inputFile.readlines()

        #A) Default the storage table to the size of the raw data - 1 in each
        #       dimension (to account for the header row and row label)
        debitTable     = [[0] * 12 for j in range(len(rawData) - 1)]
        netTable       = [[0] * 12 for j in range(len(rawData) - 1)]
        deliveredTable = [[0] * 12 for j in range(len(rawData) - 1)]
        receivedTable  = [[0] * 12 for j in range(len(rawData) - 1)]
        
        #B) For each row in the file after the first/header row. This will cause
        #       us to need to add one to each index while reading.
        for rowNum in range(0, len(rawData) - 1):
            
            #1) Split the line on the tab character
            parsedRow = rawData[rowNum + 1].split("\t")
                       
            #2) For each of the 12 months of data (remember each row has a
            #        leading column with the year data so +1 to each index)
            for colNum in range(12):
                
                #a) Split the current record on a semi-colon and a space
                currentMonth = parsedRow[colNum + 1].split("; ")

                #b) If the debug flag is set to true, print debug statements
                if DEBUG:
                    print(currentMonth)
                
                #c) Store each element appropriately in the corresponding table
                debitTable[rowNum][colNum]     = currentMonth[0]
                netTable[rowNum][colNum]       = float(currentMonth[1])
                deliveredTable[rowNum][colNum] = float(currentMonth[2])
                receivedTable[rowNum][colNum]  = float(currentMonth[3])
                
        #C) Close the file
        inputFile.close()

    #III) If the file cannot be opened, display an error message
    except (FileNotFoundError, OSError) as e:
        print("File could not be opened properly.\n")

#################################################################################
#
#   Function which 
#
#   Precondition:  
#   Precondition:  
#   Precondition:  
#   Postcondition: 
#   Invariant:     
#
#################################################################################
def analyzeFile():

    #I) Get access to necessary global variables
    global DEBUG, debitTable, netTable, deliveredTable, receivedTable
    global numberMonths, totalNet, totalDelivered, totalReceived

    #-------- ASSERTION TESTING --------#
    assert isinstance(debitTable, list), "Debit table is not a list"
    assert isinstance(netTable, list), "Net table is not a list"
    assert isinstance(deliveredTable, list), "Delivered table is not a list"
    assert isinstance(receivedTable, list), "Received table is not a list"
    #-----------------------------------#

    #II) Initialize each of the necessary global variables
    numberMonths = totalNet = totalDelivered = totalReceived = 0

    #III) For each row in the tables
    for row in range(len(debitTable)):
        
        #A) For each column in the tables
        for col in range(len(debitTable[0])):

            #1) Increment the number of months
            numberMonths += 1

            #2) If the current entry in the debit table says "DEBIT"
            if debitTable[row][col] == "DEBIT":
                #a) Add the netTable entry from totalNet
                totalNet += netTable[row][col]

            #3) Else, if the current entry in the debit table says "CREDIT"
            else:
                #b) Subtract the netTable entry from totalNet
                totalNet -= netTable[row][col]

            #4) Add the current deliveredTable and receivedTable entries to
            #       totalDelivered and totalReceived, respectively
            totalDelivered += deliveredTable[row][col]
            totalReceived  += receivedTable[row][col]
            
    #VI) If the debug flag is set to true, print debug statements
    if DEBUG:
        print("Number of Months: " + str(numberMonths))
        print("Total Net Usage:  " + str(totalNet))
        print("Total Delivered:  " + str(totalDelivered))
        print("Total Received:   " + str(totalReceived))

#################################################################################
#
#   Function which 
#
#   Precondition:  
#   Precondition:  
#   Precondition:  
#   Postcondition: 
#   Invariant:     
#
#################################################################################
def printMenuAndGetInput():
    
    #I) Get access to necessary global variables
    global INPUTS, MENU_TEXT

    #-------- ASSERTION TESTING --------#
    assert len(INPUTS) == len(MENU_TEXT), "List of valid inputs must be the same length as list of menu text"
    #-----------------------------------#

    #II) Print the menu header
    print("----------------------------------")
    print("MENU OPTIONS")
    print("----------------------------------")

    #III) Print the contents of the dynamic menu lists
    for i in range(len(INPUTS)):
        print(INPUTS[i] + ") " + MENU_TEXT[i])

    #IV) Print the quit command
    print("Q) Quit Program")
    print("")

    #V) Get and return input from the user
    return input("> ")


#---------------------- QUERY FUNCTIONS ----------------------#

#################################################################################
#
#   Function which 
#
#   Precondition:  
#   Precondition:  
#   Precondition:  
#   Postcondition: 
#   Invariant:     
#
#################################################################################
def monthCount():
    global numberMonths
    print("Number of months in file: " + str(numberMonths) + "\n")

#################################################################################
#
#   Function which 
#
#   Precondition:  
#   Precondition:  
#   Precondition:  
#   Postcondition: 
#   Invariant:     
#
#################################################################################
def analyzeData():
    global numberMonths, totalNet, totalDelivered, totalReceived
    print("Avg. Net Use per Month:   " + str(totalNet/numberMonths))
    print("Avg. Delivered per Month: " + str(totalDelivered/numberMonths))
    print("Avg. Received per Month:  " + str(totalReceived/numberMonths))
    print("Net Use Audit Difference: " + str(totalNet-(totalDelivered-totalReceived)))
    print()

#################################################################################
#
#   Function which 
#
#   Precondition:  
#   Precondition:  
#   Precondition:  
#   Postcondition: 
#   Invariant:     
#
#################################################################################
def calculateExpenses():
    global DEBUG, netTable, debitTable
    global numberMonths, totalNet, totalDelivered, totalReceived

    #I) Continually ask the user for a cost until they give a valid number
    cost = ""
    while cost == "":
        cost = input("What is the cost per kWh (current rate = 0.07): ")
        try:
            cost = float(cost)
        except:
            cost = ""

    #II) Find the minimum and maximum monthly net usage
    minRow = minCol = maxRow = maxCol = 0
    minSign = maxSign = 1 if debitTable[minRow][minCol] == "DEBIT" else -1
    for row in range(len(netTable)):
        for col in range(len(netTable[0])):
            sign = 1 if debitTable[row][col] == "DEBIT" else -1
            if (sign * netTable[row][col]) < (minSign * netTable[minRow][minCol]):
                minSign = sign
                minRow = row
                minCol = col
            if (sign * netTable[row][col]) > (maxSign * netTable[maxRow][maxCol]):
                maxSign = sign
                maxRow = row
                maxCol = col

    #VI) If the debug flag is set to true, print debug statements
    if DEBUG:
        print("(" + str(minRow) + "," + str(minCol) + ")\t = " + str(minSign * netTable[minRow][minCol]))
        print("(" + str(maxRow) + "," + str(maxCol) + ")\t = " + str(maxSign * netTable[maxRow][maxCol]))

    #V) Print the average, min, and max monthly cost at the given rate
    print("At a price of " + '${:,.2f}'.format(cost) + " per kWh, you can expect:")
    print("---------------------------------------------")
    print("Average Monthly Cost: " + '${:,.2f}'.format(cost * (totalNet/numberMonths)))
    print("Minimum Monthly Cost: " + '${:,.2f}'.format(cost * minSign * netTable[minRow][minCol]))
    print("Maximum Monthly Cost: " + '${:,.2f}'.format(cost * maxSign * netTable[maxRow][maxCol]))
    print()


#----------------------- MAIN FUNCTION -----------------------#


def main(file = None):

    #I) Get access to necessary global variables
    global INPUTS, FUNCTIONS, DEBUG
    
    #II) Try to get the first command-line parameter
    try:
        fileName = sys.argv[1]
        
    #III) If there was an index exception, then there was no file name specified.
    #       at the command line.
    except IndexError as e:

        #A) If the parameter file is populated, use that
        if file is not None:
            fileName = file
        #B) Else, use the default file name
        else
            fileName = "usage-data.txt"
        
    #IV) Else, if it was any other kind of exception, display an error message,
    #       then quit to command prompt
    except:
        input("No file specified and the default file name (usage-data.txt) does not exist.\nExiting...")
        exit(-1)

    #V) Read in the data from the file
    readFile(fileName)

    #VI) If the debug flag is set to true, print debug statements
    if DEBUG:
        print(debitTable)
        print(netTable)
        print(deliveredTable)
        print(receivedTable)

    #VII) Analyze the data
    analyzeFile()

    #VIII) While the user doesn't input a Q (in order to quit)
    currentInput = "M"
    while currentInput.upper() in INPUTS:

        #A) Print the menu and get user input
        currentInput = printMenuAndGetInput()

        #B) If the debug flag is set to true, print debug statements
        if DEBUG:
            print("Current Input => " + currentInput)

        #C) Find the index of the element in the list, if it exists,
        #       regardless of case
        index = 0
        while index < len(INPUTS) \
                and INPUTS[index] != currentInput.upper():
            index += 1

        #D) If the input (ignoring case), matches an element in the inputs list
        if currentInput.upper() in INPUTS:

            #1) Dynamically run the function using the eval function
            eval(FUNCTIONS[index])
        

if(__name__ == "__main__"):
    main()

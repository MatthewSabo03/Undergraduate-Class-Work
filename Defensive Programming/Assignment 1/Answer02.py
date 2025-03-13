# Question 01
#
# Code takes two date-structured file names as parameters which each contains
# 3 sections of sales data. The header of each section starts with an X and
# then is followed by 1 or more rows of sales data. The function will parse the
# names of each file into its component date parts. It will then aggregate the
# sales data by section and then write the resulting information into a new,
# combined file.
#
# You may assume that any variables used are appropriately scoped and
# initialized.

import sys

def combine_files(fileName1, fileName2):
    
    data1 = openFileData(fileName1, "r")
    data2 = openFileData(fileName2, "r")

    #X) Open up a file for writing called combined.txt
    combinedFile = open("combined.txt", "w")

    #XI) If the combined file has successfully open in write mode
    if combinedFile.mode == 'w':

        #1) Write the date of the files to the first line in the format
        #       yyyy/mm/dd hh:mm:ss
        combinedFile.write("Date 1: " + fileNameProcess(fileName1) + "\n")
        combinedFile.write("Date 2: " + fileNameProcess(fileName2) + "\n")

        #3) Write a blank line then a line with a single X
        combinedFile.write("\n")
        combinedFile.write("X\n")
        
        i=0
        for i in range(min(len(data1), len(data2))):
            combinedFile.write((data1[i] + data2[2]) + "\n")
            combinedFile.write("X\n")
            
        
    #XII) Close the combined file
    combinedFile.close()

def fileNameProcess(string):
    # I) Capture the relevant date/time components for each file name
    #
    # 0         1         2
    # 01234567890123456789012345
    # 08-21-1980_04.44.44_AM.txt
    
    day    = string[0:22]
    month  = string[3:5]
    year   = string[6:10]
    hour   = string[11:13]
    minute = string[14:16]
    second = string[17:19]
    half   = string[20:22]  # AM or PM
    

    #II) Convert each time of day to the 24 hour clock
    if half == "PM":
        hour = str(12 + int(hour))
        
    return(month + "-" + day + "-" + year + "_" + hour + "." +
           minute + "." + second + "_" + half)

def openFileData(fileName):
    totalFile = []
    
    #III) Open the first file
    salesFile = open(fileName, "r")

    #IV) If the first file has successfully open in read mode
    if salesFile.mode == 'r': 
        
        #A) Read the contents of the first file
        fileContents = salesFile.readlines()

        #B) Skip the first 3 lines as they contain date info, a blank line,
        #       and the first X
        lineNumber = 3
        
        while lineNumber < len(fileContents):
            result = sectionProcess(fileContents, lineNumber)
            totalFile.append(result[0])
            lineNumber = result[1] + 1
    
    salesFile.close()
    return totalFile           

def sectionProcess(fileContents, lineNumber):
    #C) Set the sales total to 0
    totalFile = 0

    #D) While the current line doesn't start with "X"
    while fileContents[lineNumber][0] != "X":

        #1) Add the current line's sales total to the first sales total
        totalFile += int(fileContents[lineNumber])

        #2) Move to the next line
        lineNumber += 1
    
    return(totalFile, lineNumber)
    
if __name__ == '__main__':
    combine_files(sys.argv[1], sys.argv[2])

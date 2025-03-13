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

    # I) Capture the relevant date/time components for each file name
    #
    # 0         1         2
    # 01234567890123456789012345
    # 08-21-1980_04.44.44_AM.txt
    
    day1    = fileName1[0:2]
    day2    = fileName2[0:2]
    month1  = fileName1[3:5]
    month2  = fileName2[3:5]
    year1   = fileName1[6:10]
    year2   = fileName2[6:10]
    hour1   = fileName1[11:13]
    hour2   = fileName2[11:13]
    minute1 = fileName1[14:16]
    minute2 = fileName2[14:16]
    second1 = fileName1[17:19]
    second2 = fileName2[17:19]
    half1   = fileName1[20:22]  # AM or PM
    half2   = fileName2[20:22]  # AM or PM

    #II) Convert each time of day to the 24 hour clock
    if half1 == "PM":
        hour1 = str(12 + int(hour1))

    if half2 == "PM":
        hour2 = str(12 + int(hour1))

    #III) Open the first file
    salesFile1 = open(fileName1, "r")

    #IV) If the first file has successfully open in read mode
    if salesFile1.mode == 'r': 
        
        #A) Read the contents of the first file
        file1Contents = salesFile1.readlines()

        #B) Skip the first 3 lines as they contain date info, a blank line,
        #       and the first X
        lineNumber = 3

        #C) Set the first sales total to 0
        total1File1 = 0

        #D) While the current line doesn't start with "X"
        while file1Contents[lineNumber][0] != "X":

            #1) Add the current line's sales total to the first sales total
            total1File1 += int(file1Contents[lineNumber])

            #2) Move to the next line
            lineNumber += 1

        #E) Skip the current line with an X
        lineNumber += 1

        #F) Set the second sales total to 0
        total2File1 = 0

        #G) While the current line doesn't start with "X"
        while file1Contents[lineNumber][0] != "X":

            #1) Add the current line's sales total to the second sales total
            total2File1 += int(file1Contents[lineNumber])

            #2) Move to the next line
            lineNumber += 1

        #H) Skip the current line with an X
        lineNumber += 1

        #I) Set the third sales total to 0
        total3File1 = 0

        #J) While the current line doesn't start with "X"
        while file1Contents[lineNumber][0] != "X":

            #1) Add the current line's sales total to the second sales total
            total3File1 += int(file1Contents[lineNumber])

            #2) Move to the next line
            lineNumber += 1

    #V) Close the first file
    salesFile1.close()

    #VI) Open the second file
    salesFile2 = open(fileName2, "r")

    #VII) If the second file has successfully open in read mode
    if salesFile2.mode == 'r': 
        
        #A) Read the contents of the second file
        file2Contents = salesFile2.readlines()

        #B) Skip the first 3 lines as they contain date info, a blank line,
        #       and the first X
        lineNumber = 3

        #C) Set the first sales total to 0
        total1File2 = 0

        #D) While the current line doesn't start with "X"
        while file2Contents[lineNumber][0] != "X":

            #1) Add the current line's sales total to the first sales total
            total1File2 += int(file2Contents[lineNumber])

            #2) Move to the next line
            lineNumber += 1

        #E) Skip the current line with an X
        lineNumber += 1

        #F) Set the second sales total to 0
        total2File2 = 0

        #G) While the current line doesn't start with "X"
        while file2Contents[lineNumber][0] != "X":

            #1) Add the current line's sales total to the second sales total
            total2File2 += int(file2Contents[lineNumber])

            #2) Move to the next line
            lineNumber += 1

        #H) Skip the current line with an X
        lineNumber += 1

        #I) Set the third sales total to 0
        total3File2 = 0

        #J) While the current line doesn't start with "X"
        while file2Contents[lineNumber][0] != "X":

            #1) Add the current line's sales total to the second sales total
            total3File2 += int(file2Contents[lineNumber])

            #2) Move to the next line
            lineNumber += 1

    #VIII) Close the second file
    salesFile2.close()

    #IX) Sum up the sales totals
    salesTotal1 = total1File1 + total1File2
    salesTotal2 = total2File1 + total2File2
    salesTotal3 = total3File1 + total3File2

    #X) Open up a file for writing called combined.txt
    combinedFile = open("combined.txt", "w")

    #XI) If the combined file has successfully open in write mode
    if combinedFile.mode == 'w':

        #1) Write the date of the first file to the first line in the format
        #       yyyy/mm/dd hh:mm:ss
        combinedFile.write("Date 1: ")
        combinedFile.write(year1)
        combinedFile.write("/")
        combinedFile.write(month1)
        combinedFile.write("/")
        combinedFile.write(day1)
        combinedFile.write(" ")
        combinedFile.write(hour1)
        combinedFile.write(":")
        combinedFile.write(minute1)
        combinedFile.write(":")
        combinedFile.write(second1)
        combinedFile.write("\n")

        #2) Write the date of the second file to the second line in the format 
        #       yyyy/mm/dd hh:mm:ss
        combinedFile.write("Date 2: ")
        combinedFile.write(year2)
        combinedFile.write("/")
        combinedFile.write(month2)
        combinedFile.write("/")
        combinedFile.write(day2)
        combinedFile.write(" ")
        combinedFile.write(hour2)
        combinedFile.write(":")
        combinedFile.write(minute2)
        combinedFile.write(":")
        combinedFile.write(second2)
        combinedFile.write("\n")

        #3) Write a blank line then a line with a single X
        combinedFile.write("\n")
        combinedFile.write("X\n")

        #4) Write the first sales totals on one line followed by a line with
        #       a single X
        combinedFile.write(str(salesTotal1) + "\n")
        combinedFile.write("X\n")

        #4) Write the second sales totals on one line followed by a line with
        #       a single X
        combinedFile.write(str(salesTotal2) + "\n")
        combinedFile.write("X\n")

        #4) Write the third sales totals on one line followed by a line with
        #       a single X
        combinedFile.write(str(salesTotal3) + "\n")
        combinedFile.write("X\n")
        
    #XII) Close the combined file
    combinedFile.close()

if __name__ == '__main__':
    combine_files(sys.argv[1], sys.argv[2])

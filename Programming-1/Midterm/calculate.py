import stdio
import stdarray
import sys

#sets up variables for loops and output
total = 0.0
r = 0
i = 0
average = 'Average'
finalGrades = 'Grades'

#creates 2D array grades and placeholder 1D array a
grades = stdarray.create2D(0, 0, 0.0)
a = stdarray.create1D(0, 0.0)

#pulls top line from input and then outputs it on write statement
heading = stdio.readLine()
stdio.writeln('Student	Hw1	Quiz1	HW2	HW3	Midterm	HW4	Quiz2	HW5	HW6	Final	Grades')

#while loop to run until input file is empty
while not stdio.isEmpty():
	#pulls student name from file
	students = stdio.readString()
	
	for i in range(10):
		#pull number from document and adds it onto array a then add the number onto total
		aGrades = stdio.readFloat()
		a += [aGrades]
		total += aGrades
		i += 1
		
		#if columns is 10 then it finds the average of the line, appends a onto 
		#grades then wipes a and total
		if i == 10:
			a += [(round(total/10,1))]
			grades.append(a)
			a = stdarray.create1D(0, 0.0)
			total = 0
	
	#writes out format for student line in output then prints that output
	format = '%s	%.1f	%.1f	%.1f	%.1f	%.1f	%.1f	%.1f	%.1f	%.1f	%.1f	%.1f\n'
	stdio.writef(format, students, grades[r][0], grades[r][1], grades[r][2], grades[r][3], 
	grades[r][4], grades[r][5], grades[r][6], grades[r][7], grades[r][8], grades[r][9], grades[r][10])
	r += 1

#calculates average of columns
for j in range(len(grades[0])):
	total = 0.0
	for i in range(r):
		total += grades[i][j]
	a += [total / r]
grades.append(a)

#writes average line in output
average = 'Average'
stdio.writef(format, average, grades[r][0], grades[r][1], grades[r][2], grades[r][3], grades[r][4], 
grades[r][5], grades[r][6], grades[r][7], grades[r][8], grades[r][9], grades[r][10])
import stdio
import random
import sys

#input
n = int(sys.argv[1])
evenN = True
square = 0
steps = 0

#Determines if input is even
if (n % 2 == 0):
	evenN=True
else:
	evenN=False

#Defines square if true, stops program if false
if (evenN==True):
	square = 2 * n
else:
	stdio.write('Try an even Number')

#Defines variables for loop
x = 0
y = 0
direction = 0

#Loop checks if either x or y is equal to square
while ((x != square) and (y != square)):
	direction = random.randrange(1,4)
	if (direction == 1):
		y += 1
		steps += 1
	elif (direction == 2):
		y -= 1
		steps += 1
	elif (direction == 3):
		x += 1
		steps += 1
	elif (direction == 4):
		x -= 1
		steps += 1

if (evenN==True):
	stdio.write('The walker took ')
	stdio.write(steps)
	stdio.writeln(' steps.')
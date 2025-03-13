import stdio
import random
import sys

n = int(sys.argv[1])

#number of simulations
m = int(sys.argv[2])

#iterator for counting loop
i = 0

#total steps over all runs
total_steps = 0

while i < m:
	evenN = True
	square = 0
	steps = 0

	#Determines if input is even
	if (n % 2 == 0):
		evenN=True
	else:
		evenN=False

	#Defines sqare if n is true
	if (evenN==True):
		square = 2 * n

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
	total_steps += steps
	i += 1

average_steps = total_steps / m
stdio.write('The average number of steps was:\t')
stdio.writeln(average_steps)
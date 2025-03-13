import random
import sys
import stdarray
import stdio

#sample size
m = int(sys.argv[1])

#range
n = int(sys.argv[2])

i = 0
lastName = 0
while not stdio.isEmpty():
	name = stdio.readAllLines()
	r = random.randrange(0, m)
	while i<n:
		if lastName != name[r]:
			stdio.writeln(str(name[r]) + ' ')
			lastName = name[r]
			r = random.randrange(0, m)
			i+=1
		else:
			r= random.randrange(0,m)

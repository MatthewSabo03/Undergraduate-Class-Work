import stdio
import sys
import random

# number of runs
n = int(sys.argv[1])

i = 0
p = 0
person2 = random.randrange(0,364)
m = [person2]

while i < n:
	person1 = random.randrange(0,364)	
	if person1 == m:
		p += len(m)
		m = [person2]
	#else:
		#m += [person1]	
	i += 1

average= i/p
stdio.write(average)
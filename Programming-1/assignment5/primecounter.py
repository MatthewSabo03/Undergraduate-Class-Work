import stdio
import math
import sys

n = int(sys.argv[1])
ctr = 0
primeCounter = 0
i = 0 
p=0

if (n<=10000000):
	for ctr in range(n):
		if (ctr <= 1):
			p += 1
		else:
			for i in range(2, ctr):
				if (ctr % i == 0):
					break
			else:
				primeCounter += 1

	stdio.write(primeCounter)

else:
	stdio.write('Input number below 10 million')
	

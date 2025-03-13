import stdio
import sys
import math

n = float(sys.argv[1])
i = 0 
power = 1

if (n<0):
	stdio.write(' ')
else:
	while power <= n:
		stdio.write(str(power) + ' ')
		power *= 2
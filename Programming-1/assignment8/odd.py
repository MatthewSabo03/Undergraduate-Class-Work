import sys
import stdio

def odd(a, b, c):
	i=0
	if a == True:
		i+=1
	if b == True:
		i+=1
	if c == True:
		i+=1
	if i==2:
		return True
	else:
		return False
first = bool(sys.argv[1])
second = bool(sys.argv[2])
third = bool(sys.argv[3])

biggest = odd(first, second, third)
stdio.write(biggest)
import sys
import stdio

def max3(a, b, c):
	if a>b and a>c:
		return a
	elif b>a and b>c:
		return b
	elif c>a and c>b:
		return c
	

first = float(sys.argv[1])
second = float(sys.argv[2])
third = float(sys.argv[3])

biggest = max3(first, second, third)
stdio.writef("The largest number is: %.1f\n", biggest)

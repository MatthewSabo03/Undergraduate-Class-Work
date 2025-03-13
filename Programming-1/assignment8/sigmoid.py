import sys
import stdio
import math

def sigmoid(a):
	return 1/(1+math.exp(-a))

x = float(sys.argv[1])

value = sigmoid(x)
stdio.writef("%.3f\n", value)
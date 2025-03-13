import math
import sys
import stdio


def sinh(x):
	s = (math.exp(x) - math.exp(-x))/2
	return s

def cosh(x):
	c = (math.exp(x) + math.exp(-x))/2
	return c

def tanh(x):
	t = ((math.exp(x) - math.exp(-x))/2) / ((math.exp(x) + math.exp(-x))/2)
	return t

def coth(x):
	ct = 1 / (((math.exp(x) - math.exp(-x))/2) / ((math.exp(x) + math.exp(-x))/2))
	return ct

def sech(x):
	sc = 1 / ((math.exp(x) + math.exp(-x))/2)
	return sc

def csch(x):
	cs = 1 / ((math.exp(x) - math.exp(-x))/2)
	return cs

def main():
	x = float(sys.argv[1])
	stdio.writeln(sinh(x))

if __name__ == '__main__':
	main()
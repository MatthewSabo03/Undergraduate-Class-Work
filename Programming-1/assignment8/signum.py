import sys
import stdio

def signum(a):
	if n<0:
		return -1
	elif n==0:
		return 0
	elif n>0:
		return 1

n = float(sys.argv[1])

sM = signum(n)
stdio.write(sM)
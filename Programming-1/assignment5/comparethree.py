import stdio
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

if (a==b==c):
	stdio.write('equal')
else:
	stdio.write('not equal')
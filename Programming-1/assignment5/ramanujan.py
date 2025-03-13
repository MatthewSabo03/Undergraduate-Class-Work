import stdio
import math
import sys

n = int(sys.argv[1])

for a in range(1, n+1):
	a3 = a*a*a
	if (a3>n):
		break
	for b in range(a, n+1):
		b3 = b*b*b
		if (a3+b3>n):
			break
		for c in range(a+1, n+1):
			c3= c*c*c
			if (a3+b3<c3):
				break
			for d in range(c, n+1):
				d3 = d*d*d
				if (a3+b3<c3+d3):
					break
				if((a3+b3)==(c3+d3)):
					stdio.write(str(a3+b3) + ' = ')
					stdio.write(str(a) + '^3 + ' + str(b) + '^3 = ')
					stdio.write(str(c) + '^3 + ' + str(d) + '^3')
					stdio.writeln()
	
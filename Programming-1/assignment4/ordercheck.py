import stdio
import math
import sys

x = float(sys.argv[1])
y = float(sys.argv[2])
z = float(sys.argv[3])

a = (x < y < z) or (x > y > z)

stdio.writeln(a)

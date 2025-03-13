import stdio
import math
import sys

a = int(sys.argv[1])
b = int(sys.argv[2]) 


c = (a % b == 0) or (b % a == 0)

stdio.writeln(c)


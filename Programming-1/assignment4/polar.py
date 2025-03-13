import stdio
import math
import sys

x = float(sys.argv[1])
y = float(sys.argv[2])

r = math.sqrt(x**2 + y**2)
theta = math.atan2(y, x)

stdio.write("r = ")
stdio.writeln(r)
stdio.write('theta = ')
stdio.write(math.degrees(theta))
 
import stdio
import math
import sys

lamda_0 = float(sys.argv[1])
longitude = float(sys.argv[2])
latitude = float(sys.argv[3])

x = longitude - lamda_0
y = 1/2 * (math.log((1 + math.sin(latitude)) / (1 - math.sin(latitude))))

stdio.write('x = ')
stdio.writeln(x)
stdio.write('y = ')
stdio.write(y)
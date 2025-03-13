import stdio
import math
import sys

x1 = float(sys.argv[1])
y1 = float(sys.argv[2])
x2 = float(sys.argv[3])
y2 = float(sys.argv[4])

d = 60*math.acos((math.sin(math.radians(x1))*math.sin(math.radians(x2))) + (math.cos(math.radians(x1))*math.cos(math.radians(x2))*math.cos(math.radians(y1)-math.radians(y2))))

stdio.write(math.degrees(d))
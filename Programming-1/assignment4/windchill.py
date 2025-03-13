import stdio
import math
import sys

temp = float(sys.argv[1])
windSpeed = float(sys.argv[2])

windChill = 35.74 + (0.6215*temp) + ((0.4275*temp)-35.75)*windSpeed**0.16

stdio.writeln(windChill)
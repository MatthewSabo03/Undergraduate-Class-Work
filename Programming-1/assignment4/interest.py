import stdio
import math
import sys

principle = float(sys.argv[1])
time = float(sys.argv[2])
rate = float(sys.argv[3])

totalAmount = principle*math.exp(time*rate)

stdio.writeln(totalAmount)
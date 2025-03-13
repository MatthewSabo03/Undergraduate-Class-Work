import sys
import stdio
import math
import stdarray
import stddraw

def fourier(n):
	x = stdarray.create1D(n+1, 0.0)
	y = stdarray.create1D(n+1, 0.0)
	for i in range(n+1):
		x[i] = math.pi * i/n
		y[i] = function
	stddraw.setXscale(0, math.pi)
	stddraw.setYscale(-10.0, +10.0)
	for i in range(n):
		stddraw.line(x[i], y[i], x[i+1], y[i+1])


n = int(sys.argv[1])

stddraw.show(fourier(n))

i=0
	while i<=n:
		spikes = cos(it)
		total += spikes
	function = total/n
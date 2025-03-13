import stddraw

xBottom = .25
yBottom = .25
xTop = .75
yTop = .75
v1 = 0.01
v2 = 0.01 
while True:
	stddraw.clear()

	#center line
	stddraw.line(0.5,1,0.5,0)

	#Horizontal Line
	stddraw.line(0,0.5,1,0.5)

	#bottom left
	stddraw.line(0.5,0,0,0)
	stddraw.line(0,0,0,0.5)
	stddraw.point(xBottom,yBottom)

	#top right
	stddraw.line(0.5,1,1,1)
	stddraw.line(1,1,1,0.5)
	stddraw.point(xTop,yTop)

	stddraw.show(10)
	if (yTop+v1) >= 1 or (yTop+v1) <= .5:
		v1 = -v1
	if (xBottom+v2) >= .5 or (xBottom+v2) <= 0:
		v2 = -v2 
	yTop+=v1
	xBottom+=v2
import stddraw

x = .5
y = .5
v = .01
while True:
	stddraw.clear()
	stddraw.line(.25,.25,.5,.75)
	stddraw.line(.5,.75,.75,.25)
	stddraw.line(.25,.25,.75,.25)
	stddraw.point(x,y)
	stddraw.show(10)
	if (y+v) >= .75 or (y+v) <= .25:
		v = -v

	y+=v

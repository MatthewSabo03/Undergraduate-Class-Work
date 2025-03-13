import stddraw

x=0
y=.5
velocity=.01

while True:
	stddraw.clear()
	stddraw.line(0,0,x, y)
	stddraw.show(10)
	if (x + velocity) >= 1 or (x + velocity) <= 0:
		velocity = -velocity
	x += velocity
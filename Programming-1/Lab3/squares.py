import stddraw

#center line
stddraw.line(0.5,1,0.5,0)

#Horizontal Line
stddraw.line(0,0.5,1,0.5)

#bottom left
stddraw.line(0.5,0,0,0)
stddraw.line(0,0,0,0.5)
stddraw.point(0.25,0.25)

#top right
stddraw.line(0.5,1,1,1)
stddraw.line(1,1,1,0.5)
stddraw.point(0.75,0.75)

stddraw.show()
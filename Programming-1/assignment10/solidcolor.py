import stddraw
import sys
from color import Color

red = int(sys.argv[1])
blue = int(sys.argv[2])
green = int(sys.argv[3])

c = Color(red, green, blue)

stddraw.setPenColor(c)
stddraw.filledSquare(256,256,256)
stddraw.show()
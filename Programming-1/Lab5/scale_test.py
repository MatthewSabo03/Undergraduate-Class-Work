import sys
import stddraw
from picture import Picture

def scale(image, scale_factor):
		
	colT = 0.0
	rowT = 0.0

	source = Picture(image)
	scaleWidth = source.width()*scale_factor
	scaleHeight = source.height()*scale_factor
	target = Picture(scaleWidth, scaleHeight)
	
	#changes scaleWidth and scaleHeight to integers for range functions in for loop
	wT = int(scaleWidth)
	hT = int(scaleHeight)

	for colT in range(wT):
		for rowT in range(hT):
			colS = colT * source.width() // wT
			rowS = rowT * source.height() // hT
			target.set(colT, rowT, source.get(colS, rowS))
	return target

def main():
	image = sys.argv[1]
	scale_factor = float(sys.argv[2])
	final = scale(image, scale_factor)
	stddraw.setCanvasSize(final.width(), final.height())
	stddraw.picture(final)
	stddraw.show()

if __name__ == '__main__':
	main()
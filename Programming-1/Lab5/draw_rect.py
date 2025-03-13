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
	x = float(sys.argv[3])
	y = float(sys.argv[4])
	origImage = Picture(image)
	final = scale(image, scale_factor)
	stddraw.setXscale(0, final.width())
	stddraw.setYscale(0, final.height())
	stddraw.setCanvasSize(final.width(), final.height())
	rectCenterX = final.width()*x
	rectCenterY = final.height()*y
	stddraw.picture(final)
	#stddraw.point(rectCenterX, rectCenterY)
	rectLowerLeftX = rectCenterX - (origImage.width()*.5)
	rectLowerLeftY = rectCenterY - (origImage.height()*.5)
	stddraw.rectangle(rectLowerLeftX, rectLowerLeftY, origImage.width(), origImage.height())
	stddraw.show()

if __name__ == '__main__':
	main()
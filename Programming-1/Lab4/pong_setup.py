import stddraw
import stdio
import math
import random

def draw_objects():
	#Defining paddle height and width
	pdl_w = .05
	pdl_h = .5	

	#left paddle
	p1_pdl_x = .15
	p1_pdl_y = .2
	stddraw.filledRectangle(p1_pdl_x, p1_pdl_y, pdl_w, pdl_h)
	
	#right paddle
	p2_pdl_x = .85
	p2_pdl_y = .2
	stddraw.filledRectangle(p2_pdl_x, p2_pdl_y, pdl_w, pdl_h)
	
	#ball
	cir_x = .5
	cir_y = .5
	cir_r = .00975
	stddraw.filledCircle(cir_x, cir_y, cir_r)

def user_input():
	pass

def animation():
	pass

def collision_detection():
	pass

def main():
	while True:
		draw_objects()
		stddraw.show()
		user_input()
		animation()
		collision_detection()
		stddraw.clear()
if __name__ == '__main__':
	main()
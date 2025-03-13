import stddraw
import stdio
import math
import random

def draw_objects(p1_pdl_y, p2_pdl_y):
	#Defining paddle height and width
	pdl_w = .05
	pdl_h = .5	

	#left paddle
	p1_pdl_x = .15
	stddraw.filledRectangle(p1_pdl_x, p1_pdl_y, pdl_w, pdl_h)
	
	#right paddle
	p2_pdl_x = .85
	stddraw.filledRectangle(p2_pdl_x, p2_pdl_y, pdl_w, pdl_h)
	
	#ball
	cir_x = .5
	cir_y = .5
	cir_r = .00975
	stddraw.filledCircle(cir_x, cir_y, cir_r)

def user_input():
	while True:
		stddraw.show(0)
		if stddraw.hasNextKeyTyped():
			input = stddraw.nextKeyTyped()
			if input == 'w':
				p1_up = input
				return p1_up
			if input == 's':
				p1_down = input
				return p1_down
			if input == 'o':
				p2_up = input
				return p2_up
			if input == 'l':
				p2_down = input
				return p2_down
			else:
				return None

def animation():
	pass

def collision_detection():
	pass

def main():
	p1_pdl_y = .2
	p2_pdl_y = .2
	draw_objects(p1_pdl_y, p2_pdl_y)
	while True:
		gameInput = user_input()
		if gameInput == 'w':
			p1_pdl_y +=.05
		if gameInput == 's':
			p1_pdl_y -=.05
		if gameInput == 'o':
			p2_pdl_y +=.05
		if gameInput == 'l':
			p2_pdl_y -=.05
		animation()
		collision_detection()
		stddraw.clear()
		draw_objects(p1_pdl_y, p2_pdl_y)
	
if __name__ == '__main__':
	main()
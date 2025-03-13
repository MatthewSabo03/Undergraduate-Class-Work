import stddraw
import stdio
import math
import random

def draw_objects(p1_pdl_y, p2_pdl_y):
	#Defining paddle height and width
	pdl_w = .05
	pdl_h = .25	

	#left paddle
	p1_pdl_x = .0025
	stddraw.filledRectangle(p1_pdl_x, p1_pdl_y, pdl_w, pdl_h)
	
	#right paddle
	p2_pdl_x = .95
	stddraw.filledRectangle(p2_pdl_x, p2_pdl_y, pdl_w, pdl_h)

def user_input():
	stddraw.show(0)
	if stddraw.hasNextKeyTyped()==True:
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

def main():
	p1_pdl_y = .2
	p2_pdl_y = .2
	cir_x = .5
	cir_y = .5
	cir_r = .00975
	ball_vel_y = (random.randrange(1,3))/75
	ball_vel_x = (random.randrange(1,3))/75
	draw_objects(p1_pdl_y, p2_pdl_y)
	while True:
		cir_x += ball_vel_x
		cir_y += ball_vel_y
		#checks if the ball has hit the sides of the screen
		if cir_y >= 1 or cir_y <= 0:
			ball_vel_y = -ball_vel_y
		if (cir_x > 0.95):
			if (cir_y > p2_pdl_y - 0.025):
				ball_vel_x = -ball_vel_x
		if (cir_x < 0.05):
			if (cir_y > p1_pdl_y - 0.025):
				ball_vel_x = -ball_vel_x
		if cir_x >= 1:
			stdio.write("Player 1 has won")
			break
		if cir_x <= 0:
			stdio.write("Player 2 has won")
			break
		stddraw.clear()
		ball = stddraw.filledCircle(cir_x, cir_y, cir_r)
		paddles = draw_objects(p1_pdl_y, p2_pdl_y)
		stddraw.show(50)
		
	#sets output of user_input as variable gameInput
		gameInput = user_input()
	
	#Checks if the keyboard input is w,s,o, or l and changes the paddles y value as such
		if gameInput == 'w':
			p1_pdl_y +=.05
		if gameInput == 's':
			p1_pdl_y -=.05
		if gameInput == 'o':	
			p2_pdl_y +=.05
		if gameInput == 'l':
			p2_pdl_y -=.05

		
		
if __name__ == '__main__':
	main()
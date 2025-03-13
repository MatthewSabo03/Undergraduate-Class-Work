import stdio
import sys
import stdarray

direction_north = ['North', 'north', 'n', 'N']
direction_south = ['South', 'south', 's', 'S']
direction_east = ['East', 'east', 'e', 'E']
direction_west = ['West', 'west', 'w', 'W']

def firstRoom():
	return stdio.writeln('You wake up in a room dimly lit by torches. You dont know how you got here but while looking around you see a door to the north and to the west.')

def secondRoom():
	return stdio.writeln('You find yourself in an empty room with a bit of cobwebs and find yourself looking at 2 doors. One to the west and one to the north.') 	
	
def swordRoom():
	return stdio.writeln('You walk into the north door and find a sword on the ground and you pick it up. You have to shake off some of the cobwebs and blood off of it but looking at your surroundings you see 2 doors on the east and west side of the room.')

def fourthRoom():
	return stdio.writeln('You walk through the door and see cobwebs and egg sacs everywhere. You also feel a presence through the door to the east.')

def fifthRoom():
	return stdio.writeln('You walk into the door and see a massive spider.')

def escapeShield():
	return stdio.writeln('You fight the spider and lose both legs from the battle. While on the ground bleeding you look around and see the exit. Using your arms you drag youself to the exit. ENDING - NEAR DEATH ESCAPE')

def escapeChestplate():
	return stdio.writeln('You fight the spider and lose an arm in the process. With the spider defeated, you look around and see the light of the sun. You walk towards it while clutching your arm. ENDING - LOST ARM ESCAPE')

def escapeCompletion():
	return stdio.writeln('You fight the spider and are completly fine other than the spider guts coving you. Looking around the room you see the light of the outside. You toss your equipment while walking up the stairs and live to tell another day. ENDING - COMPLETIONIST')

def shieldRoom():
	return stdio.writeln('Walking into the room you see a shield against the wall. You picked up the shield and see a door to the south, north, and east.')

def death():
	return stdio.writeln('You feel a presence behind you and you get stabbed in the heart, instantly killing you. ENDING - DEATH')

def lost():
	return stdio.writeln('You walk into a room that looks alot like the first room but there is no exits and a wall forms behind you. You will never escape. ENDING - TRAPPED')

def walkintoWall():
	return stdio.writeln('You walk into the wall hitting your head in the process.')

def firstroomwestLamp():
	return stdio.writeln('As you walk into the room you notice a chestpiece on a manaquinn. You decide to take the chestpiece and see a door to the north.')

def help():
	stdio.writeln('The valid commands are:')
	stdio.writeln('<direction>')
	stdio.writeln('look')
	stdio.writeln('quit')
	return None

def validateMove(nextpositionX, nextpositionY):
	room_layout = stdarray.create2D(0,0,0)
	a = [1,2,3,4]
	b = [5,6,0,0]
	c = [7,8,0,0]
	room_layout.append(a)
	room_layout.append(b)
	room_layout.append(c)
	if nextpositionX>2 or nextpositionY>3 or nextpositionX<0 or nextpositionY<0:
		return 0
	else:
		return room_layout[nextpositionX][nextpositionY]
	

def main():
	lamp = False
	shield = False
	chestpiece = False
	positionX = 2
	positionY = 1
	firstRoom()
	while True:
		userInput = input('What will you do? : ')

		if userInput == 'quit':
			stdio.writeln('Quitting game')
			break

		elif userInput == 'help':
			help()
		
		elif userInput in direction_north:
			nextpositionX = positionX - 1
			nextpositionY = positionY
			roomNumber = validateMove(nextpositionX, nextpositionY)
			if roomNumber == 0:
				walkintoWall()
			else:
				positionX = nextpositionX
				positionY = nextpositionY
				if roomNumber == 6:
					secondRoom()
				if roomNumber == 2:
					swordRoom()
				if roomNumber == 1:
					lost()
					break
				if roomNumber == 3:
					fourthRoom()
				if roomNumber == 4:
					fifthRoom()
					if shield == False and chestpiece == False:
						death()
						break
					if shield == True and chestpiece == False:
						escapeShield()
						break
					if shield == False and chestpiece == True:
						escapeChestplate()
						break 
					if shield == True and chestpiece == True:
						escapeCompletion()
						break
				if roomNumber == 5:
					shieldRoom()
					shield = True
				if roomNumber == 7:
					firstroomwestLamp()
					chestpiece = True
				if roomNumber == 8:
					firstRoom()

		elif userInput in direction_south:
			nextpositionX = positionX + 1
			nextpositionY = positionY
			roomNumber = validateMove(nextpositionX, nextpositionY)
			if roomNumber == 0:
				walkintoWall()
			else:
				positionX = nextpositionX
				positionY = nextpositionY
				if roomNumber == 6:
					secondRoom()
				if roomNumber == 2:
					swordRoom()
				if roomNumber == 1:
					lost()
					break
				if roomNumber == 3:
					fourthRoom()
				if roomNumber == 4:
					fifthRoom()
					if shield == False and chestpiece == False:
						death()
						break
					if shield == True and chestpiece == False:
						escapeShield()
						break
					if shield == False and chestpiece == True:
						escapeChestplate()
						break 
					if shield == True and chestpiece == True:
						escapeCompletion()
						break
				if roomNumber == 5:
					shieldRoom()
					shield = True
				if roomNumber == 7:
					firstroomwestLamp()
					chestpiece = True
				if roomNumber == 8:
					firstRoom()

		elif userInput in direction_east:
			nextpositionX = positionX
			nextpositionY = positionY + 1
			roomNumber = validateMove(nextpositionX, nextpositionY)
			if roomNumber == 0:
				walkintoWall()
			else:
				positionX = nextpositionX
				positionY = nextpositionY
				if roomNumber == 6:
					secondRoom()
				if roomNumber == 2:
					swordRoom()
				if roomNumber == 1:
					lost()
					break
				if roomNumber == 3:
					fourthRoom()
				if roomNumber == 4:
					fifthRoom()
					if shield == False and chestpiece == False:
						death()
						break
					if shield == True and chestpiece == False:
						escapeShield()
						break
					if shield == False and chestpiece == True:
						escapeChestplate()
						break 
					if shield == True and chestpiece == True:
						escapeCompletion()
						break
				if roomNumber == 5:
					shieldRoom()
					shield = True
				if roomNumber == 7:
					firstroomwestLamp()
					chestpiece = True
				if roomNumber == 8:
					firstRoom()
		
		elif userInput in direction_west:
			nextpositionX = positionX
			nextpositionY = positionY - 1
			roomNumber = validateMove(nextpositionX, nextpositionY)
			if roomNumber == 0:
				walkintoWall()
			else:
				positionX = nextpositionX
				positionY = nextpositionY
				if roomNumber == 6:
					secondRoom()
				if roomNumber == 2:
					swordRoom()
				if roomNumber == 1:
					lost()
					break
				if roomNumber == 3:
					fourthRoom()
				if roomNumber == 4:
					fifthRoom()
					if shield == False and chestpiece == False:
						death()
						break
					if shield == True and chestpiece == False:
						escapeShield()
						break
					if shield == False and chestpiece == True:
						escapeChestplate()
						break 
					if shield == True and chestpiece == True:
						escapeCompletion()
						break
				if roomNumber == 5:
					shieldRoom()
					shield = True
				if roomNumber == 7:
					firstroomwestLamp()
					chestpiece = True
				if roomNumber == 8:
					firstRoom()
		else:
			stdio.writeln('Unrecongized Command. Try Again or use help for list of commands.')

if __name__ == '__main__':
	main()


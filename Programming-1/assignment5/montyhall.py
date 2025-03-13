import stdio
import random
import sys

#number of simulations
n = int(sys.argv[1])

#iterator for counting loop
i = 0

#counter for staying
stayCounter=0

#counter for switching doors
switchCounter=0

#winning door
winningDoor= random.randrange(0,3)

#Chosen door
chosenDoor= random.randrange(0,3)


#stay

while i <= n:
	if (winningDoor == chosenDoor):			
		stayCounter+=1
	else:
		switchCounter+=1
			
	i+=1
	chosenDoor = random.randrange(0,3) 
	winningDoor = random.randrange(0,3)

#Switch
	
stayAverage = stayCounter / n
switchAverage = switchCounter / n

stdio.write('Stay -- ')
stdio.writeln(stayAverage)
stdio.write('Switch -- ')
stdio.write(switchAverage)
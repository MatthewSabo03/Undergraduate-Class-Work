import stdio
import random
import sys
import stdarray

n = int(sys.argv[1])

#number of simulations
m = int(sys.argv[2])

#iterator for counting loop
p = 0
prP=0
tpH=0
tnoP=0

while p < m:
	#random value
	rndm = random.randrange(0,n)
	lastRndm = -1

	#input to array
	guests = stdarray.create1D(n, False)

	#beginning of simulation
	i = 0
	while i<n:
		if lastRndm!=rndm:
			if guests[rndm]==False:
				guests[rndm]=True
				lastRndm=rndm
				rndm = random.randrange(0,n)
				i+=1
			else:
				break
		else:
			rndm = random.randrange(0,n)
	#end of simulation
	if i==n:
		prP+=1
	tpH+=i
	p+=1
	tnoP+=n
stdio.write('How often did rumor fully spread : %')
averageSpread = (prP/m)*100
stdio.writeln(averageSpread)

averageHeard = (tpH/tnoP)*100
stdio.write('Average percent who heard rumor : %')
stdio.write(averageHeard)
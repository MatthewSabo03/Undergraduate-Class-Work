import stdio
import random
import sys
import stdarray

#input
n = int(sys.argv[1])

#random value
rndm = random.randrange(0,n)
lastRndm = -1

#input to array
guests = stdarray.create1D(n, False)

#logic
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

stdio.write('Did rumor fully spread : ')

if i==n:
	stdio.writeln('True')
else:
	stdio.writeln('False')

average = (i/n)*100
stdio.write('Percent who heard rumor : ')
stdio.write(average)
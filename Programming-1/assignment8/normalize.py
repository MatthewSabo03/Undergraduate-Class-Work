import sys
import stdio
import stdarray

def normalize(a):
	i=0
	while i< len(a):
		value = a[i]
		a[i] = (value - min(a))/(max(a) - min(a))
		i+=1 
	return a
		
a = stdio.readAllFloats()

stdio.write(normalize(a))

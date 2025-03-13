import stdio
import sys
import stdarray

peaks = 0
i = 0
rows = stdio.readInt()

while not stdio.isEmpty():
	value = stdio.readAllLines()
	while i<=len(value):
		if value[i]==' ':
			value[i]=0
		if value[i-1] < value[i]:
			if value[i+1] < value[i]:
				if value[i-11] < value[i]:
					if value[i+11] < value[i]:
						peaks+=1
		i+=1
stdio.write(peaks)

#Assumed that edges = 0
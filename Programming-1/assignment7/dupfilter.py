import sys
import stdio
import stdarray

lastValue = 0
while not stdio.isEmpty():
	value = stdio.readInt()
	if value != lastValue:
		stdio.write(str(value) + ' ')
		lastValue = value
stdio.writeln()
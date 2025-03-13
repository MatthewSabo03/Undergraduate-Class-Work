import stdio
import sys

while not stdio.isEmpty():
	names = stdio.readString()
	firstValue = stdio.readInt()
	secondValue = stdio.readInt()
	divisionValue = firstValue/secondValue
	format = '%s	%d	%d	%.3f\n'
	stdio.writef(format, names, firstValue, secondValue, divisionValue)

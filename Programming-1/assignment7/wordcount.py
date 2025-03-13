import stdio
import sys

wordCount = 0
while not stdio.isEmpty():
	word = stdio.readString()
	wordCount += 1
stdio.write(wordCount)
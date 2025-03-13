import sys
import stdio


def isValidPassword(input):
	i = 0
	p = 0 
	isUpper = False
	isLower = False
	isLength = False
	isDigit = False
	isSpecial = False

	for i in input:
		if i.isupper():
			isUpper = True
		if i.islower():
			isLower = True
		if i.isdigit():
			isDigit = True
		if isUpper == False or isLower == False or isDigit == False:
			isSpecial = True
		p += 1
	
	if p>=8:
			isLength = True
	
	
	if isUpper == True and isLower == True and isDigit == True and isLength == True and isSpecial == True:
		return True
	
	else:
		return False 	



def main():
	input = str(sys.argv[1])
	answer = isValidPassword(input)
	stdio.write(answer)

if __name__ == '__main__':
	main()
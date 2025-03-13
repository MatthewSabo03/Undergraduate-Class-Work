import sys
import stdio


def isValidDNA(input):
	i = 0
	p = 0
	length = 0
	array = []
	for i in input:
		array.append(i)
	while p <= len(array):
		if array[p] == 'A' or array[p] == 'C' or array[p] == 'T' or array[p] == 'G':
			p+=1
			if p == len(array):
				return True
		else:
			return False
			break



def main():
	input = str(sys.argv[1])
	answer = isValidDNA(input)
	stdio.write(answer)

if __name__ == '__main__':
	main()
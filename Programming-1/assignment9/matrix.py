import stdio
import random
import math
import stddraw
import stdarray
import sys

def rand(m, n):
	i = 0
	r = 0
	rand = stdarray.create2D(0, 0, 0.0)
	a = stdarray.create1D(0, 0.0)
	while i<=m and r<=n:
		if i<m:
			b = random.randrange(100)/100
			a += [b]
			i += 1
		if i==m:
			if r<n:
				rand.append(a)
			a = stdarray.create1D(0, 0.0)
			i = 0
			r += 1
			
	return rand

def identity(n):
	i = 0
	r = 0
	x = 0
	matrix = stdarray.create2D(0, 0, 0)
	a = stdarray.create1D(0, 0)
	while x<=n and r<=n:
		if x==i:
			a += [1]
			x+=1
			i+=1
		if x!=n:
			a += [0]
			x+=1
		if x==n:
			if r<n:
				matrix.append(a)
			a = stdarray.create1D(0,0)
			x = 0
			r += 1
	return matrix

def dot(v1, v2):
	i = 0
	dot = stdarray.create1D(0, 0)
	if len(v1)==len(v2):
		while i <= len(v1):
			dot += [v1[i] * v2[i]]
			i += 1
	return dot

def transpose(m):
	x = 0
	y = 0
	rows = len(m)
	columns = len(m[0])
	trans = stdarray.create2D(rows, columns, 0)
	while x<= rows:
		while y<= columns:
			for x in range(columns):
				for y in range(rows):
					trans[x][y] = m[y][x]
			y += 1
			
		y = 0
		x += 1
	
	return trans

def add(m1, m2):
	add = stdarray.create
	for i in range(m1):
		for j in range(m2):
			add = m1[i][j] + m2[i][j]
	return add

def subtract(m1, m2):
	sub = sum(m1)-sum(m2)
	return sub

def multiplyMM(m1, m2):
	mult = sum(m1) * sum(m2)
	return mult

def multiplyMV(m, v):
	mul = 0
	pass

def multiplyVM(v, m):
	pass

def main():
	m = [[4, 3, 9],[6, 2, 9]]
	#m = int(sys.argv[1])
	#n = int(sys.argv[2])
	stdio.write(transpose(m))

if __name__ == '__main__':
	main()
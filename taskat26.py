#Написать программу, которая находит количество взаимо простых чисел с n
#непревышающих n^2.
n = int(input())
m = n**2
r = 0
while 1 < m:
	x = n
	y = m
	while  x != y:
		if x > y :
			x = x - y
		elif y > x:
			y = y - x
	if  x < 2:
			 r = r + 1
	m = m - 1
print('колличество:', r)

#Напишите программу, которая находит во входном потоке простые числа.
#Входной поток заканчивается символом ‘!’.
A = input()
r = 0
while A != '!':
	if A.isdigit() != True:
		if A[i] == 1: 
			print(A,': unit')
		if int(A) > 1:
			for i in range(2, int(A)):
				if (int(A)%i) == 0: 
					print(A,': composite')
					r = r+  1
					break 
		if r == 0 and A != 1:
			print(A,': prime')
	else:
		print(A,': not a number')
	A = input()


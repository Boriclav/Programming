#Напишите программу, которая удаляет из массива все простые числа,
#встречающиеся больше одного раза.
#Я не знаю, как нормально вырезать.
n = int(input())
A = [0]*n
B = []
r = 0 
for i in range (n):
	A[i] = int(input())
for i in range (len(A)):
	if A[i] <= 1:
		B.append(A[i])
	if A[i] > 1:
		k = A[i]
		for x in range (2,A[i]):
			if (k%x) == 0:
				r = r+1
				B.append(k)
				break 
		if r > 1: 
			for y in range(len(B)):
				if k == B[y]:
					B.pop()
				B.append(k)
print(B) 

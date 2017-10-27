#Напишите программу которая изменяет данный массив следующим образом:
#- увеличивает нечетные элементы массива втрое
#- уменьшает четные вдвое.
A = []
n = int(input())
for i in range(n):
    A.append(int(input()))
print(A)
for i in range(n):
	if A[i]%2 == 0:
		A[i] = A[i]/2
	else:
		A[i] = A[i] * 3
print ("new massiv:",A)

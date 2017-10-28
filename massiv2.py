#Напишите программу вычисляющую минимум, максимум и 
#среднее арифметическое элементов массива, введенного из консоли
A = []
n = int(input())
min = 0
max = 0
sum = 0 
for i in range(n):
	A.append(int(input()))
	if A[i]<min:
		min = A[i]
	if A[i]>max:
		max = A[i]
	sum = sum + A[i]
print(A)
print ('min=',min,'max=',max,'avg=', sum/len(A))

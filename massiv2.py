#Напишите программу вычисляющую минимум, максимум и 
#среднее арифметическое элементов массива, введенного из консоли
A = []
n = int(input())
min = 0
max = 0
sum = 0
avg = float
for i in range(n):
	A.append(int(input()))
	if A[i]<min:
		min = A[i]
	if(i==0):
		min=A[i]
		min=A[i]
	if A[i]>max:
		max = A[i]
	sum = sum + A[i]
	avg= sum/len(A)
print(A)
print ('min=',min,'max=',max,'avg=', avg)

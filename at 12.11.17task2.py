#Напишите программу, которая подсчитывает, 
#сколько раз в строке встретился символ ‘w’.
A = 'Wshdfggweewhwvwvw'
A = A.split()
A=list(''.join(A))
r = 0
for i in range(len(A)):
	if A[i] == 'w':
		r += 1
print(r)
print(A)

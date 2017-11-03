#Напишите программу, которая считывает текст состоящий одной строки 
#и вычисляет сумму тех слов, которые являются числами.
A = 'There were 3 mice, 7 cats and 1 dog in room!'
B = []
print(A)
for i in range(len(A)):
	 x = A[i].isdigit()
	 if x != False:
		 B.append(int(A[i])) 
print(sum(B))


#Реализуйте в виде рекурсивной функции алгоритм 
#Быстрой Сортировки для массива чисел.
def V(A):
	m = []
	r = []
	b = []
	if len(A) > 1:
		n = A[0]
		for i in range (len(A)):
			if n < A[i]:
				b.append(A[i])
			elif n == A[i]:
				r.append(A[i])
			else:
				m.append(A[i])
		return V(m) + V(r) + V(b)
	else:
		return (A)
A = []
n = int(input('enter massivs V'))
for i in range(n):
	A.append(int(input()))
print(V(A))

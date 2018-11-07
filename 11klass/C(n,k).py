#Биноминиальный коэффициент. Создать k n.
n = int(input())
k = int(input())
A = [] #Матрица
cl = 1 #colon
for i in range (n+1): # добавить строку
	A.append([])
	if cl == k + 2:
		A[i].append(1)
		for j in range (1, k + 2):
			A[i].append(-1)
	else:
		A[i].append(1)
		for k in range(1, cl):
			A[i].append(-1)
		cl += 1

def Non(n,k):
	if n == k - 1:
		print("0")
	if A[n][k] == -1:
		A[n][k] = Non(n - 1, k - 1) + Non(n-1, k)
	return A[n][k]
Non(n,k)
return A[n][k]

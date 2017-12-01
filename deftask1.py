#Напишите программу содержащую логическую функцию проверки списка чисел, 
#на то составные ли они. 
#Программа должна применять эту функцию к списку считанному с файла.
A = []
B = []
def pime(n):
	a = 0
	if n == 1:
		print('Unit')
	if n>1:
		for i in range(2, n):
			if (n%i) == 0:
				print(n,'is Composite')
				a = a + 1
				break
	if (a != 1) and (n != 1):
		print(n, 'is prime')
f = open("2.txt")
F = f.readlines()
for line in F:
	A.append(line)
A = ' '.join(A)
for i in range(len(A)):
	x = A[i].isdigit()
	if x != False:
		B.append(int(A[i])) 
print(B)
for i in range(len(B)):
	 a = pime (B[i])
	

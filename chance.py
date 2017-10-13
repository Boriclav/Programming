# Напишите программу проверяющую является ли число составным.
# В программе гарантируется, что число - натуральное.
n = int(input())
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

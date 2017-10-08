# Напишите программу проверяющую является ли число составным.
# В программе гарантируется, что число - натуральное.
n = int(input())
if n>1:
	for i in range(2,n):
		if (n%i) == 0:
			print(n,'is Composite')
			break
		else:
			print(n,'is Prime')
else:
	 print(1,'is Unit')

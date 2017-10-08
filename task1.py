# Напишите программу проверяющую N чисел на четность.
# В программе гарантируется,что все числа целые и их не менее одного.
n = int(input()) #Enter amount
for i in range(n):
	a = int(input()) #Enter number
	if(a%2==0):
		print('Even')
	else:
			print('Odd')

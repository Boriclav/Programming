#Напишите программу вычисляющую произведение двух целых чисел. 
#В программе гарантируется, что числа - целые. 
#В программе запрещается использовать операцию *(умножить).
a = int(input())
b = int(input())
res = 0
while b != 0:
	if b > 0:
		res = res+a
		b = b-1
	else:
		res = res-a
		b = b+1
print('a*b=', res)

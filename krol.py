#Написать программу, моделюрующую популяцию кролей. Данные кол-ва сезоно
#взросления, кол-во потомков у пары, длительность жизни в сезонах,
#вероятность быть съеденым.
print("взросление в сезонах")
A = int(input()) #взросление в сезонах
print("жизнь в сезонах")
C = int(input()) #жизнь в сезонах
print("кол-во пар в потомках")
B = int(input()) #кол-во пар в потомках
print("вероятность быть съедeным")
P = int(input()) # вероятность быть съедeным
print("")
D = 10**11 		 #лимит популяции
print("начальная популяция")
S = int(input()) #начальная популяция
print("длительность жизни мира")
E = int(input()) # длительность жизни мира
Q = []
import random
if A > C:
	print("Популяция умирает")
elif S > D:
	print("Кролики умерли от голода") 
else:
	while E > 0:
		if len(Q) <= A:
			Q.append(1)
		elif C > len(Q) > A:
			S += (len(Q)-A)*B
			Q = Q + [(len(Q)-A)*B]
		else:
			S = (len(Q)-A)*B - Q[0]
			Q = Q[1:] + [(len(Q)-A)*B]
		E -= 1
		print("популяция=", S)
S = S - E
print("популяцияEnd=", S)	

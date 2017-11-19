#Напишите программу, которая обрабатывает результаты IQ-теста из файла “2-in.txt". В файле лежат несколько строк со значениями(не менее 4-х). Программа должна вывести в консоль среднее арифметическое по лучшим трем в каждой строке результатам(одно число).
f = open('2-in.txt')
B = [] 
d = 3
s = 0 
m = 0
u = 0
A = [line.strip() for line in f]
for i in range(len(A)):
  A[i] = A[i].split()
  k = A[i]
  for a in range(len(k)):
   k[a] = int(k[a])
  while l > 0:
   for z in range(len(k)):
     if k[z] > s:
        s = k[z]
   B.append(s)
   while d < len(k):
     if k[d] == s:
         del k[d]
     else:
         u += 1
   d -= 1
   s = 0
  l = 3
for r in range(len(B)):
    s += B[r]
s/ = len(B)
print(s)
f.close()

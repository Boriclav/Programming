A = []
g = 0
c = 0
a = 0
t = 0
u = 0
f = open("3-in.txt")
F = f.readlines()
F.pop(0)
for line in F:
	A.append(line)
A = ' '.join(A)
print(A)
for i in range(len(A)):
	if (A[i] == 'G') or (A[i] =='g'):
		g = g + 1
	if (A[i] == 'C') or (A[i] =='c'):
		c = c + 1
	if (A[i] == 'A') or (A[i] =='a'):
		a = a + 1
	if (A[i] == 'T')or (A[i] =='t'):
		t = t + 1
	if (A[i] == 'U') or (A[i] =='u'):
		u = u + 1
if u != 0:
	print('RNA:', 'U:', u, 'T:', t, 'G:', g, 'C:', c)
else:
	 print('DNA:', 'A:', a, 'T:', t, 'G:', g, 'C:', c)
f.close		


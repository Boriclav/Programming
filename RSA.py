print ('geben eine Primzahl')
p = int(input())
print ('geben eine Primzahl')
q = int(input())
n = p * q
F = (p-1) * (q-1) #Das ist Function von Eiler
Er = [2] # Tabelle von Eratothenes
i = 3 
while i < F:
	a = 0
	for j in Er:
		if i % j == 0:
			a = 1
			break
	if a == 0:
		Er.append(i)
	a = 0
	i += 1
s = len(Er) // 2
e = Er[s]
v = 2
while v < n:
	if (v * e) % F == 1:
		d = v
		break
	v += 1		
print(' ofnenn Schlussel ist e=', e)
print(' geschlossen Schlussel ist d=', d)
print('geben einen Text') # Text ist zahlle	
T = int(input())
C = T**e % n
N = C**d % n
print(' T ist normal:', T)
print(' C ist coded:', C)
print(' N ist auscoded:', N)


'''
for i in len(T):
	j = i**e % n
	C.append(j)
for
''' 

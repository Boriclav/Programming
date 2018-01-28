from collections import Counter
file = open ('text-in.txt', 'r') # We open the file with text
Dic = {} # We create a Dictionary for storing letters and their numbers
Nod = {}
D = {}
def N(x): # This function creats new nodes between lettes 
	global Nod
	n = {}
	mass = []
	for value in x.values():
		mass.append(value)
	mass.sort() # min -- max
	if (len(mass)) != 1: # The least nembers
		eins = mass[0]
		zwei = mass[1]
		for key in x.keys():
			if eins == x[key]:
				key1 = str(key)
				del x[key]
				break
		for key in x.keys():
			if zwei == x[key]:
				key2 = str(key)     # Find Keys for nembers
				del x[key]          # New Dictionary without eins und zwei
				break
		x[(key1 + key2)] = (eins + zwei)   # Download new nember (eins + zwei)
		n[(key1 + key2)] = {key1: eins, key2: zwei}
		Nod.update(n)   # Creat new Node
		N(x)    # recursion

def K(x):
	global D
	k = []
	for key in x.keys():
		k.append(key)
	if k[0] in Nod:  # if there is this node 
		k2 = []
		for key in Nod[k[0]].keys():
			k2.append(key)  # Find number in node
		if len(k2[0]) >= len(k2[1]):  # Compare the links
			K({k2[0]: (x[k[0]] + '0')})
			K({k2[1]: (x[k[0]] + '1')})
		else:
			K({k2[1]: (x[k[0]] + '0')})
			K({k2[0]: (x[k[0]] + '1')})
	else:  # This is link
		D.update(x)
	
		

for line in file:
	for i in line:
		if i in Dic.keys():
			Dic[i] += 1
		else:
			Dic[i] = 1 
N(Dic)
nk = ""
Key = []
for key in Nod.keys(): # Find the biggest Nod
	if len(key) > len(nk):
		nk = key
for key in Nod[nk].keys(): #Download new Nod
	Key.append(key)
if len(Key[0]) >= len(Key[1]):   # Bigger is "0"
	K({Key[0]: '0'})  # Smaller is "1"
	K({Key[1]: '1'})
else:
    K({Key[1]: '0'})
    K({Key[0]: '1'})
mf = open('text-in.txt')
of = open('text-out.txt', 'w')  # Create new file for writting
for line in mf:
	for i in line:
		for key in D.keys():
			if i == key:
				of.write(str(D[key])) # Download sumbol's code in file
				break

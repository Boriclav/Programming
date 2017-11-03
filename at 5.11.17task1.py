#Напишите программу, которая считывает текст состоящий одной строки и все слова с нечетным номером переводит в верхний регистр(заглавные буквы), а с четным - в нижний(прописные).
A = 'The tkan gave me the message in a few moments. It was possible to do this, because we had not yet been civilized and were still using our ancestral language instead of the cultivated English.'
A = A.split(' ')
for i in range(len(A)):
	if i%2 == 0:
		A[i] = A[i].upper()
	else:
		A[i] = A[i].lower()
A=' '.join(A) 
print (A)


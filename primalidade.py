n = int(input("Digite um número inteiro: "))

i = 2
x = 1

while x != 0 and i < n:
	x = n % i
	i = i + 1
if x == 0:
	print("não primo")
else:
	print("primo")

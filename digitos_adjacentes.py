numero = input("Digite um número inteiro: ")
n = int(numero)

x = -1
y = -2
i = 0

while x != y and i < len(numero):
	y = x
	x = n % 10
	n = n // 10
	i = i + 1
if x == y:
	print("sim")
else:
	print("não")

		
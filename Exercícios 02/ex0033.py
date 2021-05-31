numeros = []
for i in range(0, 3):
    num = int(input('Digite um número inteiro: '))
    numeros.append(num)

maxi = max(numeros)
min = min(numeros)

print('O maior número é {} e o menor número é {}'.format(maxi, min))



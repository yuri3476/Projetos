import random

lista = []

while len(lista) < 10:
    x = random.randint(1, 6)
    lista.append(x)

print(lista)
print('Quantidade de vezes cada valor foi obtido:')
print('Valor 1: ', lista.count(1))
print('Valor 2: ', lista.count(2))
print('Valor 3: ', lista.count(3))
print('Valor 4: ', lista.count(4))
print('Valor 5: ', lista.count(5))
print('Valor 6: ', lista.count(6))



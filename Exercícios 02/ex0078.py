lista = []
for cont in range(0, 5):
    lista.append(int(input(f'Digite um valor para a Posição {cont}: ')))
maior = max(lista)
menor = min(lista)
print('=-' * 30)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} que está nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {menor} que está nas posições ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}... ', end='')
print()


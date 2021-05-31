dados = []
par = 0
maior = []
for i in range(0, 9):
    num = int(input('Digite um valor: '))
    dados.append(num)
    if num % 2 == 0:
        par += num

soma = dados[2] + dados[5] + dados[8]
maior.append(dados[3])
maior.append(dados[4])
maior.append(dados[5])

print('=-' * 30)
print(f'[  {dados[0]}  ] [  {dados[1]}  ] [  {dados[2]}  ]')
print(f'[  {dados[3]}  ] [  {dados[4]}  ] [  {dados[5]}  ]')
print(f'[  {dados[6]}  ] [  {dados[7]}  ] [  {dados[8]}  ]')
print('=-' * 30)
print(f'A soma dos valores pares é: {par}.')
print(f'A soma dos valores da terceira coluna é: {soma}.')
print(f'O maior valor da segunda linha é: {max(maior)}.')




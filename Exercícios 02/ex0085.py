num = [[], []]

for i in range(1, 8):
    dado = int(input(f'Digite o {i}ª valor: '))
    if dado % 2 == 0:
        num[0].append(dado)
    else:
        num[1].append(dado)
print('-=' * 30)
print('Os valores pares digitados foram: {} '.format(sorted(num[0])))
print('Os valores ímpares digitados foram: {}'.format(sorted(num[1])))

qnt = 0
idades = 0
while True:
    idade = int(input('Informe a sua idade: '))
    if idade == 0:
        break
    idades = idades + idade
    qnt += 1


media = idades / qnt
print('-='*25)
print(f'A idade média deste grupo de indivíduos é {media}.')
print('-='*25)

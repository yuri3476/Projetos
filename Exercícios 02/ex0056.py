med = 0
velho = 0
menos20 = 0
nomevelho = ''

for i in range(0, 4):
    print('-=-' * 5)
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    med += idade
    sexo = input('Digite o sexo [H] ou [M]: ').lower()
    if sexo == 'h' and idade > velho:
        velho = idade
        nomevelho += nome
    if sexo == 'm' and idade < 20:
        menos20 += 1

media = med / 4
print('-=-' * 10)
print('A média do grupo é {}'.format(media))
print('O homem mais velho é {} com {} anos.'.format(nomevelho, velho))
print('{} mulheres tem menos de 20 anos.'.format(menos20))


import random
from time import sleep

x = random.randint(1, 3)

print('''SUAS OPÇÕES: 
[1] PEDRA
[2] PAPEL
[3] TESOURA''')
sorteio = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

print('\033[33m-=-\033[m' * 10)
if x == 1:
    print('Computador jogou Pedra')
elif x == 2:
    print('Computador jogou Papel')
elif x == 3:
    print('Computador jogou Tesoura')

if sorteio == 1:
    print('Jogador jogou Pedra')
elif sorteio == 2:
    print('Jogador jogou Papel')
elif sorteio == 3:
    print('Jogador jogou Tesoura')
print('\033[33m-=-\033[33m' * 10)

if x == 1 and sorteio == 1 or x == 2 and sorteio == 2 or x == 3 and sorteio == 3:
    print('EMPATE')
elif x == 1 and sorteio == 2 or x == 2 and sorteio == 3 or x == 3 and sorteio == 1:
    print('Jogador vence')
elif x == 1 and sorteio == 3 or x == 2 and sorteio == 1 or x == 3 and sorteio == 2:
    print('Computador vence')


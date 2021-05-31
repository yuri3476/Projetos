from random import randint
from time import sleep
from operator import itemgetter
ranking = []
num = {'O jogador1': randint(1, 6),
       'O jogador2': randint(1, 6),
       'O jogador3': randint(1, 6),
       'O jogador4': randint(1, 6)}
print('Valores sorteados: ')
for k, v in num.items():
    print(f'   {k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(num.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('  == Ranking dos jogadores ==')
for i, v in enumerate(ranking):
    print(f'   {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)




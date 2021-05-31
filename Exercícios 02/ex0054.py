maior = 0
menor = 0

from datetime import datetime
now = datetime.now()
aa = now.year


for i in range(0, 7):
     ano = int(input('Ano de nascimento: '))
     idade = aa - ano
     if idade >= 21:
         maior = maior + 1
     else:
         menor = menor + 1


print('{} pessoas são de maiores! '.format(maior))
print('{} pessoas são de menores!'.format(menor))









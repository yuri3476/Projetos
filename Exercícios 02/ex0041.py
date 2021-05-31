from datetime import datetime

now = datetime.now()
aa = now.year

ano = int(input('Digite o ano de nascimento: '))
idade = aa - ano

if idade >= 0 and idade <= 9:
    print('MIRIM')
elif idade > 9 and idade <= 14:
    print('INFANTIL')
elif idade > 14 and idade <= 19:
    print('JUNIOR')
elif idade > 19 and idade <= 20:
    print('SÊNIOR')
else:
    print('MASTER')





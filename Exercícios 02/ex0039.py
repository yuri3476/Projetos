from datetime import datetime
now = datetime.now()
aa = now.year

ano = int(input('Digite o ano de nascimento: '))

alist = aa - ano
if alist < 18:
    qnt = 18 - alist
    print('Ainda vai se alistar! Falta {} ano(s) para o alistamento! '.format(qnt))
elif alist == 18:
    print('Está na hora de se alistar! ')
elif alist > 18:
    qnt1 = alist - 18
    print('Já passou do tempo do alistamento! Passou exatamente {} ano(s)! '.format(qnt1))


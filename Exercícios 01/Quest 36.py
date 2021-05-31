
print('\033[36m-=\033[m'*30)
qnt = int(input('Qual é a quantidade total de veículos da empresa: '))
print('\033[36m-=\033[m'*30)
ult = []
seg = 0
tec = 0
quart = 0
quint = 0
sext = 0
print()
for i in range(qnt):
    placa = (input('Qual é o número da placa do veículo: '))
    ult.append(placa[-1])
    if placa[-1] == '1' or placa[-1] == '2':
        seg += 1
    elif placa[-1] == '3' or placa[-1] == '4':
        tec += 1
    elif placa[-1] == '5' or placa[-1] == '6':
        quart += 1
    elif placa[-1] == '7' or placa[-1] == '8':
        quint += 1
    elif placa[-1] == '9' or placa[-1] == '0':
        sext += 1


soma = quint + sext
soma1 = seg + tec + quart + quint + sext
perc = (quart * 100) / soma1
print()
print('\033[36m-=\033[m'*40)
print(f'A quantidade de veículos com restrição de saída nas quintas e sextas foi de {soma}.')
print('\033[36m-=\033[m'*40)
print(f'O percentual de veículos com permissão de saída às quartas foi {perc:.2f}%.')
print('\033[36m-=\033[m'*40)
if seg > tec and seg > quart and seg > quint and seg > sext:
    print('O dia da semana com maior quantidade de veículos com restrição de saída foi segunda.')
elif tec > seg and tec > quart and tec > quint and tec > sext:
    print('O dia da semana com maior quantidade de veículos com restrição de saída foi terça.')
elif quart > seg and quart > tec and quart > quint and quart > sext:
    print('O dia da semana com maior quantidade de veículos com restrição de saída foi quarta.')
elif quint > seg and quint > tec and quint > quart and quint > sext:
    print('O dia da semana com maior quantidade de veículos com restrição de saída foi quinta.')
elif sext > seg and sext > tec and sext > quart and sext > quint:
    print('O dia da semana com maior quantidade de veículos com restrição de saída foi sexta.')
print('\033[36m-=\033[m'*40)

















pessoas = []
qnt_S = 0
cumplice = []
assassino = []
while True:
    num_rg = int(input('Informe o número de RG (-1 para finalizar): '))
    if num_rg == -1:
        break
    nome = input('Informe o nome completo: ')
    print('Responda as 5 perguntas: ')
    print()
    primeira_pergunta = input('1. |"Telefonou para a vítima?"| Digite (S=Sim ou N=Não): ').upper()
    if primeira_pergunta == 'S':
        qnt_S += 1
    segunda_pergunta = input('2. |"Esteve no local do crime?"| Digite (S=Sim ou N=Não): ').upper()
    if segunda_pergunta == 'S':
        qnt_S += 1
    terceira_pergunta = input('3. |"Mora perto da vítima?"| Digite (S=Sim ou N=Não): ').upper()
    if terceira_pergunta == 'S':
        qnt_S += 1
    quarta_pergunta = input('4. |"Devia para a vítima?"| Digite (S=Sim ou N=Não): ').upper()
    if quarta_pergunta == 'S':
        qnt_S += 1
    quinta_pergunta = input('5. |"Já trabalhou com a vítima?"| Digite (S=Sim ou N=Não): ').upper()
    if quinta_pergunta == 'S':
        qnt_S += 1
    print()
    if qnt_S == 0 or qnt_S == 1:
        pessoas += [f'Nome: {nome} -> INOCENTE']
    if qnt_S == 2:
        pessoas += [f'Nome: {nome} -> SUSPEITA']
    if qnt_S == 3 or qnt_S == 4:
        cumplice += [f'Nome: {nome} -> CÚMPLICE']
        pessoas += [f'Nome: {nome} -> CÚMPLICE']
    if qnt_S == 5:
        assassino += [f'Nome: {nome} -> ASSASSINO']
        pessoas += [f'Nome: {nome} -> ASSASSINO']
    qnt_S = 0

print()
print('\033[36m-=\033[m'*25)
print(f'LISTA DE PARTICIPAÇÃO DE CADA PESSOA NO CRIME')
print()
for k in range(0, len(pessoas)):
    print(pessoas[k])
print('\033[36m-=\033[m'*15)
print()
print('\033[36m-=\033[m'*15)
print(f'CÚMPLICES DO CRIME')
for k in range(0, len(cumplice)):
    print(cumplice[k])
print('\033[36m-=\033[m'*15)
print(f'ASSSASSINOS DO CRIME')
for k in range(0, len(assassino)):
    print(assassino[k])
print('\033[36m-=\033[m'*15)
print() 




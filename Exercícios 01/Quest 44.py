qntdAti = 0
MenorDist = 1
SexoMenor = ''
NomeMenor = ''
MaiorDist = 0
SexoMaior = ''
NomeMaior = ''
Macertou = 0
qntF = 0
MediaF = 0
print('\033[31m*\033[m'*25)
print('\033[31m  ☠ATIRADORES COPE☠\033[m')
print('\033[31m*\033[m'*25)
qnt = int(input('\nDigite a quantidade de atiradores: '))
print('\033[36m-=\033[m'*25)
for i in range(qnt):
    nome = str(input('\nInforme o nome do(a) atirador(a): '))
    sexo = str(input('Informe o sexo do atirador [M/F]: ')).upper()
    dist = float(input('Informe a distância [em cm] em relação ao alvo: '))
    if dist < 1:
        qntdAti += 1
    if dist < MenorDist:
        MenorDist = 0
        MenorDist += dist
        SexoMenor = ''
        SexoMenor += sexo
        NomeMenor = ''
        NomeMenor += nome
    if dist > MaiorDist:
        MaiorDist = 0
        MaiorDist += dist
        SexoMaior = ''
        SexoMaior += sexo
        NomeMaior = ''
        NomeMaior += nome
    if dist == 0 and sexo == 'M':
        Macertou += 1
    if sexo == 'F':
        qntF += 1
        MediaF = dist

perc = (qntdAti * 100) / qnt
media = MediaF / qntF
print()
print('\033[36m-=\033[m'*25)
print(f'O percentual de policiais que receberam o título de atirador de elite foi {perc:.2f}%')
print('\033[36m-=\033[m'*25)
print('\033[32m        ---------MELHOR DISPARO---------\033[m')
print('\033[36m-=\033[m'*25)
print(f'Nome: {NomeMenor} | sexo: {SexoMenor} | Distância do tiro do(a) policial: {MenorDist}')
print('\033[36m-=\033[m'*25)
print('\033[32m        -----------PIOR DISPARO----------\033[m')
print('\033[36m-=\033[m'*25)
print(f'Nome: {NomeMaior} | sexo: {SexoMaior} | Distância do tiro do(a) policial: {MaiorDist}')
print('\033[36m-=\033[m'*25)
print(f'A quantidade de policiais, do sexo [M], que acertaram o alvo foi {Macertou}.')
print('\033[36m-=\033[m'*25)
print(f'A média da distância ao alvo obtida pelas atiradoras foi de {media:.2f}.')
print('\033[36m-=\033[m'*25)

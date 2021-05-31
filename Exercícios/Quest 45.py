
cand1 = 0
cand2 = 0
cand3 = 0
cand4 = 0
branco = 0
nulo = 0
print('\033[36m-=\033[m'*20)
print('\033[36m        ElEIÇÃO PRESIDENCIAL\033[m')
print('\033[36m-=\033[m'*20)
print()
cod1 = int(input('Informe o código do(a) 1º Candidato(a): '))
nome1 = str(input('Infome o nome do(a) candidato(a) 1º: '))
print()
cod2 = int(input('Informe o código do(a) 2º Candidato(a): '))
nome2 = str(input('Infome o nome do(a) candidato(a) 2º: '))
print()
cod3 = int(input('Informe o código do(a) 3º Candidato(a): '))
nome3 = str(input('Infome o nome do(a) candidato(a) 3º: '))
print()
cod4 = int(input('Informe o código do(a) 4º Candidato(a): '))
nome4 = str(input('Infome o nome do(a) candidato(a) 4º: '))
print()
print('\033[36m-=\033[m'*20)
print('\033[36m               VOTAÇÃO\033[m')
print('\033[36m-=\033[m'*20)
while True:
    print()
    tit = int(input('Informe o título do eleitor: ([-1] finaliza o programa!) '))
    if tit == -1:
        break
    nome = str(input('Informe o nome do eleitor: '))
    voto = int(input('\nCandidato(a) {:^8} -> 1'
                     '\nCandidato(a) {:^8} -> 2'
                     '\nCandidato(a) {:^8} -> 3'
                     '\nCandidato(a) {:^8} -> 4'
                     '\nVoto em Branco  -> 0'
                     '\nNulo (Valor acima de 4)'
                     '\nDigite o voto do Eleitor: '.format(nome1, nome2, nome3, nome4)))
    if voto == 1:
        cand1 += 1
    elif voto == 2:
        cand2 += 1
    elif voto == 3:
        cand3 += 1
    elif voto == 4:
        cand4 += 1
    elif voto == 0:
        branco += 1
    else:
        nulo += 1

print()
print('\033[36m-=\033[m'*30)
print(f'CÓDIGO        NOME DO CANDIDATO       QUANTIDADE DE VOTOS'
      '\n{:^6}           {:^8}                 {:^14} '.format(cod1, nome1, cand1))
print('{:^6}           {:^8}                 {:^14} '.format(cod2, nome2, cand2))
print('{:^6}           {:^8}                 {:^14} '.format(cod3, nome3, cand3))
print('{:^6}           {:^8}                 {:^14} '.format(cod4, nome4, cand4))

print('\033[36m-=\033[m'*30)
print('\033[32m       =-=-=-=-=-=-CANDIDATO(a) VENCEDOR=-=-=-=-=-=-\033[m')
print('\033[36m-=\033[m'*30)

if cand1 > cand2 and cand1 > cand3 and cand1 > cand4:
    soma = cand1 + cand2 + cand3 + cand4 + branco
    perc1 = (cand1 * 100) / soma
    print(f'\nCódigo: {cod1} | O Candidato(a) {nome1} Venceu com o percentual de {perc1:.2f}% votos.')

elif cand2 > cand1 and cand2 > cand3 and cand2 > cand4:
    soma = cand1 + cand2 + cand3 + cand4 + branco
    perc2 = (cand2 * 100) / soma
    print(f'\nCódigo: {cod2} | O Candidato(a) {nome2} Venceu com o percentual de {perc2:.2f}% votos.')

elif cand3 > cand1 and cand3 > cand2 and cand3 > cand4:
    soma = cand1 + cand2 + cand3 + cand4 + branco
    perc3 = (cand3 * 100) / soma
    print(f'\nCódigo: {cod3} | O Candidato(a) {nome3} Venceu com o percentual de {perc3:.2f}% votos.')

elif cand4 > cand1 and cand4 > cand2 and cand4 > cand3:
    soma = cand1 + cand2 + cand3 + cand4 + branco
    perc4 = (cand4 * 100) / soma
    print(f'\nCódigo: {cod4} | O Candidato(a) {nome4} Venceu com o percentual de {perc4:.2f}% votos.')

print()
print('\033[36m-=\033[m'*30)
print('\033[31m     =-=-=-CANDIDATO(a) COM MENOR NÚMERO DE VOTOS=-=-=-=-\033[m')
print('\033[36m-=\033[m'*30)
print()
if cand1 < cand2 and cand1 < cand3 and cand1 < cand4:
    print(f'Código: {cod1} | O Candidato(a) {nome1} teve {cand1} votos.')

elif cand2 < cand1 and cand2 < cand3 and cand2 < cand4:
    print(f'Código: {cod2} | O Candidato(a) {nome2} teve {cand2} votos.')

elif cand3 < cand1 and cand3 < cand2 and cand3 < cand4:
    print(f'Código: {cod3} | O Candidato(a) {nome3} teve {cand3} votos.')

elif cand4 < cand1 and cand4 < cand2 and cand4 < cand3:
    print(f'Código: {cod4} | O Candidato(a) {nome4} teve {cand4} votos.')
print()
print('\033[36m-=\033[m'*40)
totalV = cand1 + cand2 + cand3 + cand4 + branco + nulo
percNulo = (nulo * 100) / totalV

print(f'O percentual de Votos Nulos em relação ao Total de Votos  foi de {percNulo:.2f}%')
print('\033[36m-=\033[m'*40)


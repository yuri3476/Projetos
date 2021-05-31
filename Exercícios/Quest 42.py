gabarito = []
resp_aluno = []
acertos = 0
reprovados = []
menor_nota = 999999999999
maior_nota = 0
nome_aluno_maiornota = []
nome_aluno_menornota = []
total_reprovados = 0
notastotal_reprovados = 0
qnt_aprovados = 0
for i in range(6):
    gabarito.append(input(f'Informe o Gabarito da Questão {i+1}: '))
print()
qnt = int(input('Informe a quantidade de alunos que realizaram a prova: '))
print()
for i in range(qnt):
    matricula = int(input('Informe a matrícula do aluno: '))
    nome_do_aluno = str(input('Informe o nome do aluno: '))
    for k in range(6):
        resp_aluno.append(input(f'Informe a resposta do aluno da questão {k+1}: '))
    if resp_aluno[0] == gabarito[0]:
        acertos += 1.5
    if resp_aluno[1] == gabarito[1]:
        acertos += 1.5
    if resp_aluno[2] == gabarito[2]:
        acertos += 1.5
    if resp_aluno[3] == gabarito[3]:
        acertos += 1.5
    if resp_aluno[4] == gabarito[4]:
        acertos += 2.0
    if resp_aluno[5] == gabarito[5]:
        acertos += 2.0
    if acertos < 6.0:
        reprovados += [f'Matrícula: {matricula} \nNome: {nome_do_aluno} \nRespostas: {resp_aluno} \nNota: {acertos}']
        total_reprovados += 1
        notastotal_reprovados += acertos
    if acertos > 6.0:
        qnt_aprovados += 1
    print()
    if acertos > maior_nota:
        maior_nota = 0
        maior_nota += acertos
        nome_aluno_maiornota.clear()
        nome_aluno_maiornota.append(nome_do_aluno)
    if acertos < menor_nota:
        menor_nota = 0
        menor_nota += acertos
        nome_aluno_menornota.clear()
        nome_aluno_menornota.append(nome_do_aluno)
    acertos = 0
    resp_aluno.clear()
media_alunos_reprovados = notastotal_reprovados / total_reprovados
perc_aprovados = ((qnt_aprovados * 100) / qnt)
print()
print('\033[36m-=\033[m'*25)
print('GABARITO DA PROVA: ')
print(f'Questão 01: {gabarito[0]}'
      f'\nQuestão 02: {gabarito[1]}'
      f'\nQuestão 03: {gabarito[2]}'
      f'\nQuestão 04: {gabarito[3]}'
      f'\nQuestão 05: {gabarito[4]}'
      f'\nQuestão 06: {gabarito[5]}')
print('\033[36m-=\033[m'*25)
print()

print('RELATÓRIO DE ALUNOS REPROVADOS: ')
for k in range(0, len(reprovados)):
    print(reprovados[k])
    print()

print('\033[36m-=\033[m'*25)
print(f'Aluno com maior nota: {nome_aluno_maiornota[0]} | Nota: {maior_nota} ')
print(f'Aluno com menor nota: {nome_aluno_menornota[0]} | Nota: {menor_nota} ')
print('\033[36m-=\033[m'*25)
print(f'A média das notas dos alunos reprovados foi {media_alunos_reprovados}')
print('\033[36m-=\033[m'*25)
print(f'O percentual de alunos que obtiveram nota acima da média da turma foi de {perc_aprovados:.2f}%')
print('\033[36m-=\033[m'*25)

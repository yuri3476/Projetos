import funcoes

while True:
    print('\033[36m-=\033[m' * 25)
    try:
        menu = int(input('''1 - Cadastro de Professores\n2 - Cadastro de Alunos\n3 - Cadastro de Disciplinas
4 - Cadastro de Notas\n5 - Relatório de Notas\n0 - Para finalizar o programa
\nEscolha uma opção: '''))
    except ValueError:
        print(f'O valor informado está incorreto!')
    if menu == 0:
        print('Programa finalizado com sucesso! Volte Sempre!')
        break
    if menu == 1:
        funcoes.cadastro_professor()
    if menu == 2:
        funcoes.cadastro_aluno()
    if menu == 3:
        funcoes.cadastro_disciplina()
    if menu == 4:
        funcoes.cadastro_notas()
    if menu == 5:
        funcoes.relatorio()


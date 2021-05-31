import pandas as pd
import funcoes1

dados = {'Matricula': [], 'Nome': [], 'Data de nascimento': []}
try:
    dados = funcoes1.Carregamento_Excel('Professores_Cadastrados.xlsx', 'Matricula')
except FileNotFoundError or KeyError:
    pass

aluno = {'Matricula': [], 'Nome': [], 'Data de nascimento': []}
try:
    aluno = funcoes1.Carregamento_Excel('Alunos_Cadastrados.xlsx', 'Matricula')
except FileNotFoundError or KeyError:
    pass

nota = {'Cod_disci': [], 'Disciplina': [], 'Aluno': [],
        'Professor': [], 'Nota 1': [], 'Nota 2': [], 'Nota Final': []}

try:
    nota = funcoes1.Carregamento_Excel('Notas_Alunos.xlsx', 'Cod_disci')
except FileNotFoundError or KeyError:
    pass

dados_disc = {'Codigo_Disciplina': [], 'Nome_Disciplina': [], 'Matricula_Professor_Disciplina': []}
try:
    dados_disc = funcoes1.Carregamento_Excel('Disciplina_Cadastradas.xlsx', 'Codigo_Disciplina')
except FileNotFoundError or KeyError:
    pass

Matriculas_Professores = list(dados.values())
Matricula_Alunos = list(aluno.values())
Codigos_Disciplinas = list(dados_disc.values())


def cadastro_professor():
    while True:
        matricula_prof = int(input('\nInforme a matricula do professor ([0] para sair): '))
        if matricula_prof == 0:
            break
        elif int(matricula_prof) in Matriculas_Professores[0]:
            print("Esta matrícula já está cadastrada.")
            break
        nome_prof = str(input('Informe o nome do professor: ')).title().strip()
        print('Informe a data no formato DiaMesAno EX: 11122001 sem ultilizar / ou outros caracters')
        data_prof = input('\ninforme a data da consulta [0 para sair]: ')
        funcoes1.Cadastro_Professor_Aluno(dados, matricula_prof, nome_prof, data_prof,
                                          'Professores_Cadastrados.xlsx')
        print('\nProfessor Cadastrado com sucesso!')


def cadastro_aluno():
    while True:
        matricula_aluno = int(input('\nInforme a matricula do aluno ([0] para sair): '))
        if matricula_aluno == 0:
            break
        elif int(matricula_aluno) in Matricula_Alunos[0]:
            print("\nEsta matricula já está cadastrada!")
            break
        nome_aluno = str(input('Informe o nome do aluno: '))
        print('Informe a data no formato DiaMesAno EX: 11122001 sem ultilizar / ou outros caracters')
        data_aluno = input('\ninforme a data da consulta [0 para sair]: ')
        funcoes1.Cadastro_Professor_Aluno(aluno, matricula_aluno, nome_aluno, data_aluno,
                                          'Alunos_Cadastrados.xlsx')
        print('\nAluno Cadastrado com sucesso!')


def cadastro_disciplina():
    while True:
        codigo_dic = int(input('\nInforme o código da disciplina ([0] para sair): '))
        if codigo_dic == 0:
            break
        elif codigo_dic in Codigos_Disciplinas[0]:
            print('Esta disciplina já está cadastrada!')
            break
        nome_dic = input('Informe o nome da disciplina: ').title()

        matricula_dic = int(input('Informe a matricula do professor: '))
        if matricula_dic not in Matriculas_Professores[0]:
            print('Professor não cadastrado!')
            break
        funcoes1.Cadastro_Disciplina(dados_disc, codigo_dic, nome_dic, matricula_dic)
        print('\nDisciplina cadastrada com sucesso!')


def cadastro_notas():
    while True:
        codigo = int(input('Informe o código da disciplina ([0] para sair): '))
        if codigo == 0:
            break
        elif codigo not in Codigos_Disciplinas[0]:
            print('Esta disciplina não está cadastrada!')
            break
        nome_dici = input('Informe o nome da disciplina: ').title().strip()
        if nome_dici not in Codigos_Disciplinas[1]:
            print('\nDisciplina não cadastrada!')
            break
        nome_profnot = input('Informe o nome do professor: ').title().strip()
        if nome_profnot not in Matriculas_Professores[1]:
            print('\nProfessor não cadastrado!')
            break
        matricula_alu = input('Informe a matricula do aluno: ')
        if int(matricula_alu) not in Matricula_Alunos[0]:
            print('\nAluno não está cadastrado!')
            break
        nota1 = float(input('Informe a primeira nota: '))
        nota2 = float(input('Informe a segunda nota: '))
        funcoes1.Cadastro_Notas(nota, codigo, nome_dici, nome_profnot, matricula_alu, nota1, nota2)
        print('\nNotas cadastradas com sucesso!')


def relatorio():
    try:
        print(pd.read_excel('Notas_Alunos.xlsx'))
    except FileNotFoundError:
        print("\nNão há notas cadastradas")











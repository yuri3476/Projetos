import funcoes1
cadastro_dentista = {}
cadastro_paciente = {}
relatorio = {}
cadastramento_consulta = {}
dict = {'contador': 0}

try:
    funcoes1.cadastro_D(cadastro_dentista, 'Cadastro_Dentista')
except FileNotFoundError:
    open("Cadastro_Dentista.txt", "w")

try:
    funcoes1.cadastro_C(cadastro_paciente)
except FileNotFoundError:
    open("Cadastro_Paciente.txt", "w")

try:
    funcoes1.cadastro_D(relatorio, 'Relatorio_dentista_ativo')
except FileNotFoundError:
    open("Relatorio_dentista_ativo.txt", "w")

try:
    funcoes1.cadastro_R(cadastramento_consulta)
except FileNotFoundError:
    open("Registro_Consulta.txt", "w")

try:
    funcoes1.carregar(dict)
except FileNotFoundError:
    open("carregar.txt", "w")

while True:
    print()
    print('\033[36m-=\033[m' * 25)
    print('\033[31m ===============DENTISTA GODZILLA===============\033[m')
    print('\033[36m-=\033[m' * 25)
    try:
        menu = int(input('''1 - Cadastro de Dentistas\n2 - Inativação do Cadastro do Dentista
3 - Cadastro de Pacientes\n4 - Registrar Consulta\n5 - Cancelar Consulta\n6 - Relatório de Pacientes
7 - Relatório de Dentistas Ativos\n8 - Relatório de Consultas por Data\n0 - Sair
        \nEscolha uma opção: '''))

    except ValueError:
        print(f'O valor informado está incorreto!')
    if menu == 0:
        print()
        print('''\033[31m⠀⠀⠀⠀⠀ ⢀⠀⠀⢠⣠⡭⠈⠈⠉⠀⠀⠀⠒⠐⠂⠂⠀⠴⢀⠀⠔⢠⢀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀ ⠊⠄⠒⠀⠄⣈⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⢀⠀⠠⣀⠀⠈⢑⠀⠌⠄⠁⠀⠀⠀⠀
⠀⠀⠀⠀ ⠐⠀⠤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢄⠀⠀⠠⠀⠀⠀⠀⠀⠀⠈⠀⠰⡔⠀⠀⢸⠀⢄⢀⠈
             ⠈⠂⡀⢄⠀⠀⠀⠀⠀⠈⠀⠠⢀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠘⠁⠐⡔⢀⠀⠀
⠀⠀⠀⠀⠀ ⢀⣁⠂⠀⠤⠀⠑⡁⠀⠀⠀⠀⠄⠁⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀
⠀⠀⠀ ⠀⠈⠀⠀⠀⢀⠠⠄⠤⢀⠄⠀⠀⠄⠀⠀⠀⠀⠐⠀⠀⡀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⢀⠘⠀⠀⢀⠐⠈⠀⠄⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠠⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠈⠂⠀⠀⠀⠀⠀⠀⠀⠀⠈⡀⠀⠀⠀
⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣆⣀⠀⠀⠀⠀⢨⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⠀⠀⠀⠀⠀⠀⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠨⡠⠨⡁⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠸⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢀⠃⠀⠀⠀⡀⠡⠀⠀⠀⠀⠀⠀⡬⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠢⢂⠃⠀⢀⠠⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀\033[m''''')
        break
    elif menu == 1:
        print('\033[36m-=\033[m' * 15)
        print('\n<<<Cadastro de Dentistas>>>')
        funcoes1.cadastro_de_dentistas(cadastro_dentista, relatorio)
    elif menu == 2:
        print('\033[36m-=\033[m' * 15)
        print('\n<<<Inativação do Cadastro do Dentista>>>')
        funcoes1.inativacao_dentista(cadastro_dentista, relatorio)
    elif menu == 3:
        print('\033[36m-=\033[m' * 15)
        print('\n<<<Cadastro de Pacientes>>>')
        funcoes1.cadastro_de_paciente(cadastro_paciente)
    elif menu == 4:
        print('\033[36m-=\033[m' * 15)
        print('\n<<<Registrar Consulta>>>')
        funcoes1.registrar_consulta(cadastro_dentista, cadastramento_consulta, dict)
    elif menu == 5:
        print('\033[36m-=\033[m' * 15)
        print('\n<<<Cancelar Consulta>>>')
        funcoes1.cancelar_consulta(cadastramento_consulta)
    elif menu == 6:
        print('\033[36m-=\033[m' * 15)
        print('\n<<<Relatório de Pacientes>>>')
        with open('Cadastro_Paciente.txt', 'r')as doc:
            for k in doc:
                k = k.strip()
                print(k)
    elif menu == 7:
        print('\033[36m-=\033[m' * 15)
        print('\n<<<Relatório de Dentistas Ativos>>>')
        with open('Relatorio_dentista_ativo.txt', 'r')as doc:
            for k in doc:
                k = k.strip()
                print(k)
    elif menu == 8:
        print('\033[36m-=\033[m' * 15)
        print('\n<<<Relatório de Consultas por Data>>>')
        lista1 = list(cadastramento_consulta.values())
        lista2 = []
        lista3 = []
        digite = str(input('Informe uma data: '))
        for k in range(0, len(lista1)):
            if lista1[k][0] == digite:
                lista2 += [lista1[k]]
        for k in range(0, len(lista2)):
            lista3 += [int(lista2[k][3])]
            print(lista2[k])
        print(f'Total arrecado na data: {lista2[0][0]} foi de R${(sum(lista3))}')
        input()











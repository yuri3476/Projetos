

def cadastro_D(dentista, nome_arquivo):
    with open(f'{nome_arquivo}.txt') as documento:
        for linha in documento:
            (crm, status, nome, cpf, sexo) = linha.split()
            dentista[crm] = [status, nome, cpf, sexo]


def cadastro_R(dentista):
    with open('Cadastro_Dentista.txt') as documento:
        for linha in documento:
            (crm, status, nome, cpf) = linha.split()
            dentista[crm] = [status, nome, cpf]


def cadastro_de_dentistas(dentista, relatorio):
    while True:
        sair = input('\nDeseja sair? [S/N]: ').upper()
        if sair == 'S':
            break
        else:
            pass
        while True:
                print()
                print('\033[36m-=\033[m' * 30)
                crm = input('Digite o Número do seu CRM [Digite 0 para sair]: ')
                if crm == '0':
                    break
                while len(crm) != 4 or crm.isalpha():
                    print('Digite somente os 4 números do CRM!')
                    crm = input('\nDigite o Número do seu CRM: ')
                nome = input('Informe o nome: ').title()
                while True:
                    cpf = str(input('Informe o CPF do funcionário (11 números): '))
                    if len(cpf) == 11 and cpf.isnumeric():
                        break
                sexo = input('Informe o sexo: [M/F]: ').capitalize()
                while True:
                    status = str(input('Informe o status do dentista [ativo/inativo]: ')).lower()
                    if status == 'ativo' or status == 'inativo':
                        break
                if status == 'ativo' and crm not in dentista.keys():
                    dentista[crm] = [status, nome, cpf, sexo]
                    relatorio[crm] = [status, nome, cpf, sexo]
                    with open('Cadastro_Dentista.txt', 'a') as doc:
                        doc.write(str(crm))
                        doc.write(str(' '))
                        doc.write(str(status))
                        doc.write(str(' '))
                        doc.write(str(nome))
                        doc.write(str(' '))
                        doc.write(str(cpf))
                        doc.write(str(' '))
                        doc.write(str(sexo))
                        doc.write(str('\n'))
                    with open('Relatorio_dentista_ativo.txt', 'a') as doc:
                        doc.write(str(crm))
                        doc.write(str(' '))
                        doc.write(str(status))
                        doc.write(str(' '))
                        doc.write(str(nome))
                        doc.write(str(' '))
                        doc.write(str(cpf))
                        doc.write(str(' '))
                        doc.write(str(sexo))
                        doc.write(str('\n'))
                    print('Dentista cadastrado com sucesso!')
                    print('\033[36m-=\033[m' * 30)
                    break


def inativacao_dentista(dentista, relatorio):
    while True:
        for k, v in relatorio.items():
            print(f'CRM: {k} | Dados: {v}')
        sair = input('\nDeseja sair? [S/N]: ').upper()
        if sair == 'S':
            break
        else:
            pass
        while True:
            print()
            print('\033[36m-=\033[m' * 30)
            crm = str(input('Informe o CRM do dentista que deseja inativar [0 para sair]:  '))
            if crm == '0':
                break
            if dentista[crm][0] == 'ativo':
                print()
                dentista[crm][0] = 'inativo'
                lista1 = list(dentista.keys())
                lista2 = list(dentista.values())
                del relatorio[crm]
                lista3 = list(relatorio.keys())
                lista4 = list(relatorio.values())
                with open('Cadastro_Dentista.txt', 'w') as documento:
                    for k in range(0, len(lista1)):
                        documento.write(str(lista1[k]))
                        documento.write(" ")
                        documento.write(str(lista2[k]).strip("[]'").replace("'", "").replace(",", ""))
                        documento.write('\n')
                with open('Relatorio_dentista_ativo.txt', 'w') as documento:
                    for k in range(0, len(lista3)):
                        documento.write(str(lista3[k]))
                        documento.write(" ")
                        documento.write(str(lista4[k]).strip("[]'").replace("'", "").replace(",", ""))
                        documento.write('\n')
                print('Status mudado com sucesso!')
                print()
                break
            elif dentista[crm] == 'inativo':
                print('Este CRM já está inativo!')


def cadastro_C(cliente):
    with open(f'Cadastro_Paciente.txt') as documento:
        for linha in documento:
            (nome, cpf, nomes) = linha.split()
            cliente[cpf] = nome, nomes


def cadastro_de_paciente(paciente):
    while True:
        sair = input('\nDeseja sair? [S/N]: ').upper()
        if sair == 'S':
            break
        else:
            pass
        while True:
                print()
                print('\033[36m-=\033[m' * 30)
                nome = input('Informe o nome: ').title()
                while True:
                    cpf = str(input('Informe o CPF do cliente (11 números): '))
                    if len(cpf) == 11 and cpf.isnumeric():
                        break
                sexo = input('Informe o sexo: [M/F]: ').capitalize()
                with open('Cadastro_Paciente.txt', 'a') as doc:
                    doc.write(str(nome))
                    doc.write(str(' '))
                    doc.write(str(cpf))
                    doc.write(str(' '))
                    doc.write(str(sexo))
                    doc.write(str('\n'))
                print('Paciente cadastrado com sucesso!')
                break


def cadastro_R(dentista):
    with open('Registro_Consulta.txt') as documento:
        for linha in documento:
            (numero, data, status, nome, nomes, cpf) = linha.split()
            dentista[numero] = [data, status, nome, nomes, cpf]


def carregar(dict):
    with open('carregar.txt') as doc:
        for line in doc:
            (contador, numero) = line.split()
            dict[contador] = int(numero)


def registrar_consulta(dentista, paciente, dict):
    while True:
        sair = input('\nDeseja sair? [S/N]: ').upper()
        if sair == 'S':
            break
        else:
            pass
        while True:
            try:
                print()
                print('\033[36m-=\033[m' * 43)
                print('Informe a data no formato DiaMesAno EX: 11122001 sem ultilizar / ou outros caracters')
                data = input('\ninforme a data da consulta [0 para sair]: ')
                if data == '0':
                    break
                else:
                    crm = input('Digite o CRM do dentista: ')
                    while dentista.get(crm)[0] != 'ativo':
                        print('\nO Dentista está Indisponível, Digite outro crm!')
                        crm = input('Digite o CRM do dentista: ')
                        if crm in dentista.keys() and dentista.get(crm)[0] == 'ativo':
                            print('\nO dentista está disponível')
                    while True:
                        cpf = str(input('Informe o CPF do cliente (11 números): '))
                        if len(cpf) == 11 and cpf.isnumeric():
                            break
                    while True:
                        status = int(input('Escolha 1- primeira consulta ou 2- retorno? [1/2]: '))
                        if status == 1 or status == 2:
                            break
                    lista_vazia = []
                    lista8 = list(paciente.values())
                    try:
                        for i in range(0, len(lista8)):
                            lista_vazia.append(lista8[i][4])
                    except IndexError:
                        pass
                    if status == 1 and cpf not in lista_vazia:
                        print('\nSua primeira Consulta! Será cobrado R$ 200,00!')
                        dict['contador'] += 1
                        lista = list(dict.values())
                        paciente[str(lista[0])] = [data, 'ativo', crm, '200', cpf]
                        with open('carregar.txt', 'w') as doc:
                            doc.write('contador')
                            doc.write(str(' '))
                            doc.write(str(lista[0]))
                            doc.write(str('\n'))
                        lista1 = list(paciente.keys())
                        lista2 = list(paciente.values())
                        with open('Registro_Consulta.txt', 'w') as documento:
                            for k in range(0, len(lista1)):
                                documento.write(str(lista1[k]))
                                documento.write(" ")
                                documento.write(str(lista2[k]).strip("[]'").replace("'", "").replace(",", ""))
                                documento.write('\n')
                        print('Consulta realizada com sucesso!')

                    elif status == 2 and cpf not in lista_vazia:
                        print('\nConsulta de retorno! Não será cobrado!')
                        dict['contador'] += 1
                        lista = list(dict.values())
                        paciente[str(lista[0])] = [data, 'ativo', crm, '0', cpf]
                        with open('carregar.txt', 'w') as doc:
                            doc.write('contador')
                            doc.write(str(' '))
                            doc.write(str(lista[0]))
                            doc.write(str('\n'))
                        with open('Registro_Consulta.txt', 'a') as doc:
                            doc.write(str(str(lista[0])))
                            doc.write(str(' '))
                            doc.write(str(data))
                            doc.write(str(' '))
                            doc.write(str('ativo'))
                            doc.write(str(' '))
                            doc.write(str(crm))
                            doc.write(str(' '))
                            doc.write(str('0'))
                            doc.write(str(' '))
                            doc.write(str(cpf))
                            doc.write(str('\n'))
                        print('Consulta realizada com sucesso!')
                    else:
                        print('\nNão é a primeira consulta ou não é retorno! Escolha opção novamente!')
            except ValueError:
                print('Digite Novamente')


def cancelar_consulta(cadastro_consulta):
    while True:
        sair = input('\nDeseja sair? [S/N]: ').upper()
        if sair == 'S':
            break
        else:
            pass
        while True:
            print()
            for k, v in cadastro_consulta.items():
                print(f'{k} | {v}')
            print()
            codigo = str(input('Informe o código da sua consulta: '))
            data_consulta = input('Informe a data da consulta: ')
            crm = str(input('Informe o crm: '))
            while True:
                cpf = str(input('Informe o CPF do cliente (11 números): '))
                if len(cpf) == 11 and cpf.isnumeric():
                    break
            if cadastro_consulta.get(codigo)[4] == cpf and cadastro_consulta.get(codigo)[2] == crm:
                cadastro_consulta[codigo][1] = 'inativo'
                cadastro_consulta[codigo][3] = '0'
                print()
                for k, v in cadastro_consulta.items():
                    print(f'{k} | {v}')
                print()
                lista1 = list(cadastro_consulta.keys())
                lista2 = list(cadastro_consulta.values())
                with open('Registro_Consulta.txt', 'w') as documento:
                    for k in range(0, len(lista1)):
                        documento.write(str(lista1[k]))
                        documento.write(" ")
                        documento.write(str(lista2[k]).strip("[]'").replace("'", "").replace(",", ""))
                        documento.write('\n')
                print('Consulta cancelada com sucesso!')
                print('\033[36m-=\033[m' * 25)
                break
























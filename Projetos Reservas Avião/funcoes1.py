import pprint

#mostra todas as vagas do avião
def vagas_aviao():
    matriz = []
    #criando a matriz com todas as posições
    for i in range(20):
        linha = []
        for j in range(4):
            linha.append('X')
        matriz.append(linha)
    return matriz


#trás do .txt para o dicionário, o cpf e o nome
def cadastro_C(cliente):
    with open('cadastro.txt') as documento:
        for linha in documento:
            (cpf, nome) = linha.split()
            cliente[cpf] = nome


#irá fazer o cadastro dos clientes pelo nome e cpf com suas validações e jogar no .txt
def cadastro_de_cliente(cliente):
    while True:
        sair = input('\nDeseja sair? [S/N]: ').upper()
        if sair == 'S':
            break
        else:
            pass
        nome = input('\nInforme o seu nome: ').capitalize()
        while True:
            try:
                while True:
                    cpf = str(input('\nInforme o CPF do cliente (11 números): '))
                    if len(cpf) == 11 and cpf.isnumeric():
                        break
                if cpf in cliente.keys():
                    print(f'Este CPF já está cadastrado!')
                if cpf not in cliente.keys():
                    cliente[cpf] = nome
                    with open('cadastro.txt', 'a') as documento:
                        documento.write(str(cpf))
                        documento.write(str(' '))
                        documento.write(str(nome))
                        documento.write(str('\n'))
                    print('Cliente cadastrado com sucesso!')
                    break
            except ValueError:
                print('Informe apenas números válidos!')
        else:
            pass

#trás do .txt para o dicionário , o cpf, a fileira e a cadeira
def cadastro_dic(cliente):
    with open('reservas.txt') as documento:
        for linha in documento:
            (cpf, nome, nomes) = linha.split()
            cliente[cpf] = [int(nome), int(nomes)]


#verificar se pelo cpf, o cliente está ou não cadastrado
def consulta_cliente_pelo_cpf(cliente):
    while True:
        sair = input('\nDeseja sair? [S/N]: ').upper()
        if sair == 'S':
            break
        else:
            pass
        try:
            while True:
                consulta_cliente_cpf = str(input('\nInforme o CPF do cliente (11 números): '))
                if len(consulta_cliente_cpf) == 11 and consulta_cliente_cpf.isnumeric():
                    break
        except ValueError:
            print('Informe apenas números!')
        if consulta_cliente_cpf in cliente.keys():
            print(f'O cliente {cliente[consulta_cliente_cpf]} já foi cadastrado!')
        else:
            print('O número de CPF informado não está cadastrado!')


#imprimir as reservas do avião
def reservas_acento(carregar_as_reservas_do_aviao):
    for i in range(len(carregar_as_reservas_do_aviao)):
        print(carregar_as_reservas_do_aviao[i])


#a partir das posições do acento, carrega as posições salvas na matriz
def tabela(vagas_do_aviao, carregar_as_reservas_do_aviao):
    contador2 = 0
    lista = []
    lista += carregar_as_reservas_do_aviao.values()
    while True:
        vagas_do_aviao[(lista[contador2][0])-1][(lista[contador2][1])-1] = '&'
        contador2 += 1
        if contador2 == len(lista):
            break


#cancelamento de reservas por meio do cpf do cliente
def cancelamento_reserva(vagas_do_aviao, cadastro_cliente, carregar_as_reservas_do_aviao):
    while True:
        sair = input('\nDeseja sair? [S/N]: ').upper()
        if sair == 'S':
            break
        else:
            pass
        for k in range(len(vagas_do_aviao)):
            print(vagas_do_aviao[k])
        while True:
            cpf_cliente = str(input('\nInforme o CPF do cliente (11 números): '))
            if len(cpf_cliente) == 11 and cpf_cliente.isnumeric():
                break

        if cpf_cliente in cadastro_cliente.keys() and cpf_cliente not in carregar_as_reservas_do_aviao.keys():
            print('Este CPF não efetuou nenhuma reserva!')
        elif cpf_cliente not in cadastro_cliente.keys():
            print('Este CPF não está cadastrado!')
        elif cpf_cliente in cadastro_cliente.keys() and cpf_cliente in carregar_as_reservas_do_aviao.keys():
            try:
                fileira = int(input('Informe a fileira que deseja cancelar: '))
                while fileira > 19 or fileira < -1:
                    print('Número de fileira inválida!')
                    fileira = int(input('\nInforme a fileira que deseja cancelar: '))
            except ValueError:
                print('\nDigite somente números')
            try:
                cadeira = int(input('Informe a cadeira que deseja cancelar: '))
                while cadeira > 19 or cadeira < -1:
                    print('Número da cadeira inválida!')
                    cadeira = int(input('\nInforme a cadeira que deseja cancelar: '))
            except ValueError:
                print('\nDigite somente números')
            if carregar_as_reservas_do_aviao[cpf_cliente] == [fileira, cadeira]:
                print('\nCancelamento de reserva concluido com sucesso!')
                with open('cancelamento.txt', 'a') as doc:
                    doc.write(f'CPF: {cpf_cliente} Cadeira: {cadeira} Fileira: {fileira}\n')
                del carregar_as_reservas_do_aviao[cpf_cliente]
                lista1 = list(carregar_as_reservas_do_aviao.keys())
                lista2 = list(carregar_as_reservas_do_aviao.values())
                with open('reservas.txt', 'w') as doc:
                    for k in range(0, len(carregar_as_reservas_do_aviao)):
                        doc.write(f'{str(lista1[k])} {str(lista2[k]).strip("][")[0:1]}'
                                  f' {str(lista2[k]).strip("][")[-1]}\n')

                vagas_do_aviao[fileira-1][cadeira-1] = 'X'
                for k in range(len(vagas_do_aviao)):
                    print(vagas_do_aviao[k])
            else:
                print(f'A cadeira e Fileira informada, não foi reservada pelo CPF informado!')

# vai fazer as reservas de assento por meio do cpf cadastrado e jogar o cpf , a fileira e a cadeira reservada em
# outro .txt
def reserva_de_assento(vagas_do_aviao, cadastro_cliente, carregar_as_reservas_do_aviao):
    while True:
        sair = input('\nDeseja sair? [S/N]: ').upper()
        if sair == 'S':
            break
        else:
            pass
        for k in range(len(vagas_do_aviao)):
            print(vagas_do_aviao[k])
        fileira = 0
        cadeira = 0
        while True:
            cpf = str(input('\nInforme o CPF do cliente (11 números): '))
            if len(cpf) == 11 and cpf.isnumeric():
                break
        if cpf in carregar_as_reservas_do_aviao.keys():
            print('Este CPF já realizou uma reserva!')
        elif cpf in cadastro_cliente.keys():
            try:
                fileira = 0
                while fileira > 20 or fileira < 1:
                    fileira = int(input('Digite a fileira que deseja reservar: '))
                    if fileira > 20 or fileira < 1:
                        print(f'\nA fileira informada não existe!\n')
                    else:
                        break
            except ValueError:
                print('Digite somente Números!')
            try:
                cadeira = 0
                while cadeira > 4 or cadeira < 1:
                    cadeira = int(input('Digite a cadeira que deseja reservar: '))
                    if cadeira > 4 or cadeira < 1:
                        print('\nA cadeira informada não existe!\n')
                    else:
                        break
            except ValueError:
                print('Digite somente Números!')
            if vagas_do_aviao[fileira-1][cadeira-1] == '&':
                print('A cadeira escolhida já está reservada!')
            else:
                vagas_do_aviao[fileira-1][cadeira-1] = '&'
                carregar_as_reservas_do_aviao[cpf] = [fileira, cadeira]
                with open('reservas.txt', 'a') as documento:
                    documento.write(str(cpf))
                    documento.write(str(' '))
                    documento.write(str(fileira))
                    documento.write(' ')
                    documento.write(str(cadeira))
                    documento.write(str('\n'))
                print('Vaga reservada com sucesso!')
                for k in range(len(vagas_do_aviao)):
                    print(vagas_do_aviao[k])
        elif cpf not in cadastro_cliente.keys():
            print('Este CPF não está cadastrado!')


#faz o relatório de reservas
def relatorio_reservas(carregar_as_reservas_do_aviao):
    pprint.pprint(carregar_as_reservas_do_aviao)


#faz o relatório dos acentos livres
def relatorio_acentos_livres(matriz):
    disponiveis = []
    for i in range(len(matriz)):
        for k in range(len(matriz[i])):
            if matriz[i][k] == '&':
                disponiveis.append(k+1)
        print(f'Fila {i+1}: {disponiveis}')
        disponiveis = []


#faz o relatório dos cancelamentos das reservas
def relatorio_cancelamento_reserva():
    x = open('cancelamento.txt', 'r')
    print(x.read())


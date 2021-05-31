

def cadastro_C(cliente):
    with open('Cadastro_Cliente.txt') as documento:
        for linha in documento:
            (cpf, nome) = linha.split()
            cliente[cpf] = nome


def cadastro_dic(cliente):
    with open('Cadastro_de_Carros.txt') as documento:
        for linha in documento:
            (cpf, nome) = linha.split()
            cliente[cpf] = [str(nome)]


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
                    with open('Cadastro_Cliente.txt', 'a') as documento:
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


def cadastro_de_carros(carregar_carros_para_aluguel):
    while True:
        sair = input('\nDeseja sair? [S/N]: ').upper()
        if sair == 'S':
            break
        else:
            pass
        while True:
            try:
                while True:
                    placa = str(input('\nInforme a placa do carro (7 dígitos): '))
                    if len(placa) == 7:
                        break
                    if len(carregar_carros_para_aluguel) >= 20:
                        print('Quantidade de carros excedido! Digite qualquer tecla para continuar!')
                        input()
                        break
                if len(carregar_carros_para_aluguel) >= 20:
                    print('Quantidade de carros excedido! Digite qualquer tecla para continuar!')
                    input()
                    break
                if placa in carregar_carros_para_aluguel.keys():
                    print(f'Este carro já foi cadastrado!')
                if placa not in carregar_carros_para_aluguel.keys():
                    marca = str(input('Informe a marca do carro: '))
                    modelo = str(input('Informe o modelo do carro: '))
                    while True:
                        ano = input('Informe o ano do carro(4 dígitos): ')
                        if len(ano) == 4 and ano.isnumeric():
                            break
                    while True:
                        status = str(input('Informe o status do carro [Alugado|Disponível]: ')).lower()
                        if status == 'alugado' or status == 'disponivel':
                            break
                    carregar_carros_para_aluguel[placa] = [status]
                    with open('Cadastro_de_Carros.txt', 'a') as documento:
                        documento.write(str(placa))
                        documento.write(str(' '))
                        documento.write(str(status))
                        documento.write(str('\n'))
                    print('Carro cadastrado com sucesso!')
                    break
            except ValueError:
                print('Informe apenas números válidos!')
        else:
            pass


def reserva_do_carro(cadastro_clientes, carregar_carros_para_aluguel, relatorio_cliente_carro ):
    for k, i in carregar_carros_para_aluguel.items():
        print(f'Placa: {k} | Status: {i}')

    while True:
        sair = input('\nDeseja sair? [S/N]: ').upper()
        if sair == 'S':
            break
        else:
            pass
        while True:
            cpf = str(input('\nInforme o CPF do Cliente (11 números): '))
            if len(cpf) == 11 and cpf.isnumeric() and cpf in cadastro_clientes.keys():
                break
            if cpf in carregar_carros_para_aluguel.keys():
                print('Este CPF já realizou uma reserva de carro!')
        for k, i in carregar_carros_para_aluguel.items():
            print(f'Placa: {k} | Status: {i}')

        while True:
            placa = str(input('\nInforme a placa do carro (7 dígitos): '))
            if placa in relatorio_cliente_carro.keys() and relatorio_cliente_carro.get(placa) == ['alugado']:
                print('O veículo já está alugado!')
                break
            if placa in carregar_carros_para_aluguel.keys() and carregar_carros_para_aluguel.get(placa)\
                    == ['disponivel']:
                carregar_carros_para_aluguel[placa] = ['alugado']
                for k, i in carregar_carros_para_aluguel.items():
                    print(f'Placa: {k} | Status: {i}')
                lista1 = list(carregar_carros_para_aluguel.keys())
                lista2 = list(carregar_carros_para_aluguel.values())
                with open('Cadastro_de_Carros.txt', 'w') as documento:
                    for k in range(0, len(lista1)):
                        documento.write(f'{str(lista1[k])} {str(lista2[k][0])}\n')
                print('Carro Reservado com sucesso!')
                relatorio_cliente_carro[placa] = ['alugado']
                with open('Relatorio_clientes_carro.txt', 'a') as documento:
                    documento.write(str(cadastro_clientes.get(cpf)))
                    documento.write(str(' '))
                    documento.write(str(placa))
                    documento.write(str('\n'))
                break









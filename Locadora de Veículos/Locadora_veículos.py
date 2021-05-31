import funcoes


cadastro_clientes = {}
carregar_carros_para_aluguel = {}
relatorio_cliente_carro = {}

try:
    funcoes.cadastro_C(cadastro_clientes)
except FileNotFoundError:
    open("Cadastro_Cliente.txt", "w")

try:
    funcoes.cadastro_dic(carregar_carros_para_aluguel)
except FileNotFoundError:
    open("Cadastro_de_Carros.txt", "w")

while True:
    print('\033[36m-=\033[m' * 25)
    try:
        menu = int(input('''1 - Cadastro de Clientes\n2 - Cadastro de Carros para Aluguel
3 - Registro de Aluguel de Carro\n4 - Relatório de Clientes\n5 - Relatório de Alugueis\n0 - Sair
        \nEscolha uma opção: '''))

    except ValueError:
        print(f'O valor informado está incorreto!')
    if menu == 0:
        print('\n<<<FIM DO PROGRAMA>>>')
        break
    elif menu == 1:
        print('\033[36m-=\033[m' * 15)
        print('\n<<<Cadastro de Clientes>>>')
        funcoes.cadastro_de_cliente(cadastro_clientes)
    elif menu == 2:
        print('\033[36m-=\033[m' * 15)
        print('\n<<<Cadastro de Carros para Aluguel>>>')
        funcoes.cadastro_de_carros(carregar_carros_para_aluguel)
    elif menu == 3:
        print('\033[36m-=\033[m' * 15)
        print('\n<<<Registro de Aluguel de Carro>>>')
        funcoes.reserva_do_carro(cadastro_clientes, carregar_carros_para_aluguel, relatorio_cliente_carro)
    elif menu == 4:
        print('\033[36m-=\033[m' * 15)
        print('\n<<<Relatório de Clientes>>>')
        for k, i in cadastro_clientes.items():
            print(f'Nome: {i}| CPF: {k}')
        print()
    elif menu == 5:
        print('\033[36m-=\033[m' * 15)
        print('\n<<<Relatório de Alugueis>>>')
        with open('Relatorio_clientes_carro.txt', 'r')as doc:
            for k in doc:
                k = k.strip()
                print(k)











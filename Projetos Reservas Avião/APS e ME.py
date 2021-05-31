import funcoes1


vagas_do_aviao = funcoes1.vagas_aviao()
cadastro_clientes = {}
carregar_as_reservas_do_aviao = {}

try:
    funcoes1.cadastro_C(cadastro_clientes)
except FileNotFoundError:
    open("cadastro.txt", "w")
try:
    funcoes1.cadastro_dic(carregar_as_reservas_do_aviao)
except FileNotFoundError:
    open("reservas.txt", "w")
try:
    funcoes1.tabela(vagas_do_aviao, carregar_as_reservas_do_aviao)
except IndexError:
    pass

while True:
    print('\033[36m-=\033[m' * 25)
    try:
        menu = int(input('''1 - Cadastro de cliente\n2 - Consulta de clientes pelo CPF\n3 - Reserva de assento
4 - Cancelamento de Reserva de Assento\n5 - Relatório de Reservas\n6 - Relatório de Assentos Livres
7 - Relatório de Cancelamento de Reservas de Assento\n0 - Para finalizar o programa
\nEscolha uma opção: '''))
    except ValueError:
        print(f'O valor informado está incorreto!')
    if menu == 0:
        print('Programa finalizado com sucesso! Volte Sempre!')
        break
    elif menu == 1:
        print('\033[36m-=\033[m' * 15)
        print('\n<<<Cadastro de Cliente>>>')
        funcoes1.cadastro_de_cliente(cadastro_clientes)
    elif menu == 2:
        print('\033[36m-=\033[m' * 15)
        print('\n<<<Consulta de clientes pelo CPF>>>')
        funcoes1.consulta_cliente_pelo_cpf(cadastro_clientes)
    elif menu == 3:
        print('\033[36m-=\033[m' * 15)
        print('\n<<<Reserva de assento>>>')
        funcoes1.reserva_de_assento(vagas_do_aviao, cadastro_clientes, carregar_as_reservas_do_aviao)
    elif menu == 4:
        print('\033[36m-=\033[m' * 15)
        print('\n<<<Cancelamento de Reserva de Assento>>>')
        funcoes1.cancelamento_reserva(vagas_do_aviao, cadastro_clientes, carregar_as_reservas_do_aviao)
    elif menu == 5:
        print('\033[36m-=\033[m' * 15)
        print('\n<<<Relatório de Reservas>>>')
        funcoes1.relatorio_reservas(carregar_as_reservas_do_aviao)
    elif menu == 6:
        print('\033[36m-=\033[m' * 15)
        print('<<<Relatório de Assentos Livres>>>')
        funcoes1.relatorio_acentos_livres(vagas_do_aviao)
    elif menu == 7:
        print('\033[36m-=\033[m' * 15)
        print('<<<Relatório de Cancelamento de Reservas de Assento>>>')
        funcoes1.relatorio_cancelamento_reserva()
        print()















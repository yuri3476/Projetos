import funcoes3

while True:
    print('\033[36m-=\033[m' * 25)
    try:
        menu = int(input('''1 - Cadastrar Proprietário\n2 - Cadastrar Imóvel\n3 - Cadastrar Inquilino
4 - Registrar Aluguel\n5 - Finalizar Aluguel\n6 - Relatório de Proprietários\n7 - Relatório de Imóveis
8 - Relatório de Inquilinos\n9 - Relatório de Aluguéis\n10 - Relatório de Comissões\n0 - Finalizar o Programa
    \nEscolha uma opção: '''))
    except ValueError:
        print(f'O valor informado está incorreto!')
    if menu == 0:
        print('Programa finalizado com sucesso! Volte Sempre!')
        break
    if menu == 1:
        print('\033[36m-=\033[m' * 15)
        funcoes3.cadastro_proprietario()
    if menu == 2:
        print('\033[36m-=\033[m' * 15)
        funcoes3.cadastro_imovel()
    if menu == 3:
        print('\033[36m-=\033[m' * 15)
        funcoes3.cadastro_inq()
    if menu == 4:
        print('\033[36m-=\033[m' * 15)
        funcoes3.registro_aluguel()
    if menu == 5:
        print('\033[36m-=\033[m' * 15)
        funcoes3.finalizar_aluguel()
    if menu == 6:
        print('\033[36m-=\033[m' * 15)
        funcoes3.relatorio_prop()
    if menu == 7:
        print('\033[36m-=\033[m' * 15)
        funcoes3.relatorio_imovel()
    if menu == 8:
        print('\033[36m-=\033[m' * 15)
        funcoes3.relatorio_inquilino()
    if menu == 9:
        print('\033[36m-=\033[m' * 15)
        funcoes3.relatorio_alugueis()
    if menu == 10:
        print('\033[36m-=\033[m' * 15)
        funcoes3.relatorio_comissoes()









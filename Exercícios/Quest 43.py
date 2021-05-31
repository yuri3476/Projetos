
print('\033[36m-=\033[m'*25)
print('\033[36m     =-=-=-=-EMPRÉSTIMOS DE LIVROS=-=-=-=-\033[m')
print('\033[36m-=\033[m'*25)
Livros_cadastrados = []
qnt_exemplares = 0
total_exemplares = 0
Alunos_cadastrados = []
livros = []
valores = []
numeros_x = []
x = []

while True:
    opcao = int(input('''
[1] Cadastrar exemplar 
[2] Registrar empréstimo 
[3] Emitir relatório de empréstimos 
[4] Indicar livro mais solicitado 
[5] Indicar livro menos solicitado 
[6] Indicar livros não solicitados
\nEscolha um número para o que deseja: '''))
    print()
    print('\033[36m-=\033[m'*25)
    if opcao == 1:
        while True:
            codigo = input('Informe o Cadastro do Código [Digite 0 para sair]: ')
            if codigo == '0':
                break
            titulo = input('Informe o Título: ')
            qnt_Livros = int(input('Quantidade de exemplares dos livros disponíveis na biblioteca para empréstimo: '))
            Livros_cadastrados += [f'Código {codigo} Título {titulo} Quantidade de exemplares: {qnt_Livros}']
            x += [[codigo, titulo, 0]]
            numeros_x += [0]  # Numero de exemplares comprados
            livros.append(codigo)
            print()

    elif opcao == 2:
        while True:
            matricula = int(input('Informe o cadastro da matrícula: [Digite 0 para sair]'))
            if matricula == 0:
                break
            while qnt_exemplares < 3:
                codigo_livro = input('Informe o código do livro[Máximo 3 exemplares]: (Digite 0 para sair)')
                if int(codigo_livro) > 0 and codigo_livro in livros:
                    for k in range(0, len(x)):
                        if codigo_livro in x[k]:
                            x[k][2] += 1
                            numeros_x[k] += 1
                    qnt_exemplares += 1
                    total_exemplares += 1
                if codigo_livro == '0' or qnt_exemplares == 3:
                    Alunos_cadastrados += [f'{matricula} 	          {qnt_exemplares}']
                    qnt_exemplares = 0
                    break
                if codigo_livro not in livros:
                    print('Livro Indisponível. Escolha outro livro! ')

    elif opcao == 3:
        print('MATRÍCULA 	QUANTIDADE DE EXEMPLARES')
        for k in range(0, len(Alunos_cadastrados)):
            print(Alunos_cadastrados[k])
        print('\033[36m-=\033[m'*25)
        print('TOTAL: ', total_exemplares, 'EXEMPLARES EMPRESTADOS.')
        print()

    elif opcao == 4:
        maximo = max(numeros_x)
        for i in range(len(x)):
            if maximo == x[i][2]:
                print(f"Livro mais solicitado foi: {x[i][0]} do código {x[i][1]} com {x[i][2]} solicitações.")
                print('\033[36m-=\033[m'*25)
                print()

    elif opcao == 5:
        lista = []
        lista += numeros_x
        menor = min(lista)
        while 0 in lista:
            lista.remove(menor)
        menor2 = min(lista)
        for i in range(len(x)):
            if menor2 == x[i][2]:
                print(f"Livro menos solicitado foi {x[i][0]} do código {x[i][1]} com {x[i][2]} solicitações.")
                print('\033[36m-=\033[m'*25)
                print()
        lista = []
    elif opcao == 6:
        zero = 0
        for i in range(len(x)):
            if zero == x[i][2]:
                print(f"Livro sem solicitação foi {x[i][0]} do código {x[i][1]} com {x[i][2]} solicitações.")
                print('\033[36m-=\033[m'*25)
                print()







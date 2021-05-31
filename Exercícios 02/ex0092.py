from datetime import datetime
now = datetime.now()
aa = now.year
dados = {}

for i in range(0, 1):
    dados['Nome'] = str(input('Nome: '))
    b = int(input('Ano de Nascimento: '))
    idade = aa - b
    dados['Idade'] = idade
    dados['Carteira de Trabalho'] = int(input('Carteira de Trabalho (0 não tem): '))
    if dados['Carteira de Trabalho'] == 0:
        print('-=' * 30)
        print(dados)
        print(f'nome tem o valor {dados["Nome"]}')
        print(f'idade tem o valor {dados["Idade"]}')
        print(f'ctps tem o valor {dados["Carteira de Trabalho"]}')
        break
    else:
        dados['Ano de contratação'] = int(input('Ano de contratação: '))
        dados['Salário'] = int(input('Salário: '))
        print('-=' * 30)
        print(dados)
        print(f'nome tem o valor {dados["Nome"]}')
        print(f'idade tem o valor {dados["Idade"]}')
        print(f'ctps tem o valor {dados["Carteira de Trabalho"]}')
        print(f'contratação tem o valor {dados["Ano de contratação"]}')
        print(f'Salário tem o valor {dados["Salário"]}')
        aps = aa - dados["Ano de contratação"]
        s = 35 + aps
        print(f'aposentadoria tem o valor {s}')



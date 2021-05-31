nome = str(input('Digite o seu nome completo: ')).strip()
print('Maiúscula: ', nome.upper())
print('Minúscula: ', nome.lower())
print('Quantidade de letras: ', len(nome) - nome.count(' '))
contagem = nome.split()
print('Quantas de letras tem o primeiro nome: ', len(contagem[0]))



sexo = input('Digite o seu sexo [M] ou [F]: ').strip().upper()[0]
while sexo not in 'MnFm':
    sexo = str(input('Dados inválidos.Por favor, informe seu sexo [M/F]: ')).strip().upper()[0]


print(f'Sexo {sexo} registrado com sucesso! ')




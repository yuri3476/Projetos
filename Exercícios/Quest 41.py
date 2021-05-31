salario_maior = 0
pessoas_salario_maior = []
qnt_homens = 0
qnt_mulheres = 0
media_salario = 0
salario_homem = 0
menor_salario = 99999999
nome_mulher_menor_salario = []
qnt = int(input('Informe a quantidade de entrevistados: '))
print()
for i in range(qnt):
    nome = input('Informe o seu nome: ')
    salario = int(input('Informe o seu salário: '))
    sexo = input('Informe o seu sexo (M - Masculino / F - Feminino): ').upper()
    if sexo == 'M':
        qnt_homens += 1
        salario_homem += salario
    if sexo == 'F':
        qnt_mulheres += 1
    if salario < menor_salario:
        menor_salario = 0
        menor_salario += salario
        nome_mulher_menor_salario.clear()
        nome_mulher_menor_salario.append(nome)
    idade = int(input('Informe a sua idade: '))
    habitantes_lar = int(input('Informe o número de habitantes em seu lar: '))
    print()
    if salario > 1.500:
        pessoas_salario_maior += [f'Nome: {nome} | Salário: {salario} | Sexo: {sexo} | Idade: {idade} | '
                                  f'Habitantes por lar: {habitantes_lar}']
if salario_homem != 0:
    media_salario = salario_homem / qnt_homens
pec = (qnt_mulheres * 100) / qnt
print('\033[36m-=\033[m'*40)
for k in range(0, len(pessoas_salario_maior)):
    print(pessoas_salario_maior[k])
print('\033[36m-=\033[m'*40)
print(f'A média de salário nas residências que os homens são responsáveis foi de {media_salario}. ')
print('\033[36m-=\033[m'*40)
print(f'O percentual de mulheres que são responsáveis pela sua residência é de {pec:.2f}%')
print('\033[36m-=\033[m'*40)
print(f'O nome da mulher com menor salário dentre os entrevistados é {nome_mulher_menor_salario[0]}.')
print('\033[36m-=\033[m'*40)

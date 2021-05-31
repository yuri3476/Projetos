maior18 = 0
homens = 0
qntf = 0
while True:
    print('   CADASTRE UMA PESSOA')
    print('-' * 26)
    idade = int(input('Digite a idade: '))
    if idade > 18:
        maior18 += 1
    sexo = input('Digite o sexo [M/F]: ').upper()
    while sexo != 'M' and sexo != 'F':
        sexo = input('Digite o sexo [M/F]: ').upper()
    if sexo == 'M':
        homens += 1
    print('-' * 26)
    if idade < 20 and sexo == 'F':
        qntf += 1
    n = input('Quer continuar: [S/N] ').upper()
    while n != 'S' and n != 'N':
        n = input('Quer continuar: [S/N] ').upper()
    print('-' * 26)
    if n == 'N':
        break
    else:
        continue
print('=====FIM DO PROGRAMA=====')
print(f'Total de pessoas com mais de 18 anos: {maior18}.')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {qntf} mulheres com menos de 20 anos.')





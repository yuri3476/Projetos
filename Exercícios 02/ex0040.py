print('\033[34m-=-\033[m' * 15)
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
print('\033[34m-=-\033[m' * 15)

media = (n1 + n2) / 2

if media < 5.0:
    print('\033[31mREPROVADO\033[m')

elif media >= 5.0 and media <= 6.9:
    print('\033[31mRECUPERAÇÃO\033[m')

elif media >= 7.0:
    print('\033[33mAPROVADO\033[m')




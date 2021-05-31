import random
qntv = 0

print('\033[31m-=-\033[m' * 10)
print('\033[32mVAMOS JOGAR PAR OU ÍMPAR\033[m')
print('\033[31m-=-\033[m' * 10)

while True:

    x = random.randint(0, 10)
    v = int(input('Digite um valor: '))
    p = str(input('Par ou Ímpar? [P/I] ')).upper()
    soma = x + v
    resto = soma % 2
    if resto == 0 and p == 'P':
        print('\033[31m-=-\033[m' * 10)
        print(f'Você jogou {v} e o computador {x}.Total de {soma} DEU PAR')
        print('\033[31m-=-\033[m' * 10)
        print('Você Venceu!')
        print('Vamos jogar novamente...')
        qntv += 1

    elif resto == 0 and p == 'I':
        print('\033[31m-=-\033[m' * 10)
        print(f'Você jogou {v} e o computador {x}.Total de {soma} DEU ÍMPAR')
        print('\033[31m-=-\033[m' * 10)
        print('Você Perdeu!')
        print(f'GAME OVER! Você venceu {qntv} vezes.')
        break
    elif resto != 0 and p == 'P':
        print('\033[31m-=-\033[m' * 10)
        print(f'Você jogou {v} e o computador {x}.Total de {soma} DEU ÍMPAR')
        print('\033[31m-=-\033[m' * 10)
        print('Você Perdeu!')
        print(f'GAME OVER! Você venceu {qntv} vezes.')
        break
    elif resto != 0 and p == 'I':
        print('\033[31m-=-\033[m' * 10)
        print(f'Você jogou {v} e o computador {x}.Total de {soma} DEU ÍMPAR')
        print('\033[31m-=-\033[m' * 10)
        print('Você Venceu!')
        print('Vamos jogar novamente...')
        qntv += 1







n = 0
maior = []
while n != 5:
    valor1 = int(input('\nDigite um valor: '))
    maior.append(valor1)
    valor2 = int(input('Digite outro valor: '))
    maior.append(valor2)
    n = int(input('\n[1] Somar \n[2] Multiplicar \n[3] maior  \n[4] novos números \n[5] sair do programa\nEscolha um valor:'))

    if n == 1:
        soma = valor1 + valor2
        print('A soma dos valores é {}! '.format(soma))
    elif n == 2:
        mult = valor1 * valor2
        print('A multiplicação dos valores é {}! '.format(mult))
    elif n == 3:
        mai = max(maior)
        print('O maior números entre os valores digitados é {}!'.format(mai))
    elif n == 5:
        break
    elif n == 4:
        continue

print('FIM')



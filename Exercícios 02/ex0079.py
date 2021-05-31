lista = []
while True:
    n = (int(input('Digite um valor: ')))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')



    cont = str(input('Deseja continuar? [S/N] ')).upper()
    if cont == 'N':
        break
print('-=' * 30)
print('Você digitou os valores',  sorted(lista))


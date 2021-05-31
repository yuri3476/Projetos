n1 = float(input('Digite o comprimento pra primeira reta: '))
n2 = float(input('Digite o comprimento pra segunda reta: '))
n3 = float(input('Digite o comprimento pra terceira reta: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('É possivel formar um triângulo!')
else:
    print('Não é possivel formar um triângulo!')

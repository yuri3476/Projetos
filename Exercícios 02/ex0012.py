preco = float(input('Qual é o valor do produto? '))

novo = preco * 0.05
novop = preco - novo

print('\nO novo valor do produto com o desconto será: ', novop)
print('O novo valor do produto com o desconto será {:.2f}'.format(novop))

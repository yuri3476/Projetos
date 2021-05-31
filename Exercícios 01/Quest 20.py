maior = soma = 0
menor = 9999999999
produto = 1
qtde = int(input("Quantos números você deseja informar: "))
while qtde > 0:
   numero = int(input("Digite um número: "))
   if numero > maior:
       maior = numero
   if numero < menor:
       menor = numero
   soma = soma + numero
   produto = produto * numero
   qtde = qtde - 1
print('-='*30)
print(f'O menor valor digitado foi {menor}.')
print(f'O maior valor digitado foi {maior}.')
print(f'A soma entre os valores digitados é {soma}.')
print(f'O produto entre os valores digitados é {produto}.')
print('-='*30)


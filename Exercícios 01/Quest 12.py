a = 0
b = 0

num1 = int(input('Informe um número: '))
num2 = int(input('Informe outro número: '))

if num1 > num2:
    b += num1
    a += num2
else:
    a += num1
    b += num2
print('-='*30)
print(f'Variável A: {a}')
print(f'Variável B: {b}')
print('-='*30)



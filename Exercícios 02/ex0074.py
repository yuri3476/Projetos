import random
x = random.randint(0, 10)
y = random.randint(0, 10)
z = random.randint(0, 10)
w = random.randint(0, 10)
l = random.randint(0, 10)
tupla = (x, y, z, w, l)

print('Os valores sorteados foram: ', tupla)
f = max(tupla)
h = min(tupla)
print('O maior valor sorteado foi: ', f)
print('O menor valor sorteado foi: ', h)



parenaberto = parenfechado = 0

expressao = input('Digite a expressão: ')
for c in expressao:
    if c == '(':
        parenaberto += 1
    elif c == ')':
        parenfechado += 1

if parenaberto == parenfechado:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')
    
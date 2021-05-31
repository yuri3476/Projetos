cmd = str(input('Digite C(crescente) e D(decrescente): ')).upper()
if cmd == 'C':
    for i in range(30, 50):
        print(i)
    print('FIM')
elif cmd == 'D':
    for i in range(49, 29, -1):
        print(i)
    print('FIM')




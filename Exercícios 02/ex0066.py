qnt = 0
s = 0
while True:
    num = int(input('Digite um valor: '))
    if num == 999:
        break
    qnt += 1
    s += num

print(f'A quantidade de números digitados foi {qnt} e a soma deles é {s}!')


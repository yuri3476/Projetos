s = 0
for i in range(0, 500):
    n = (i % 2)

    if n == 0:
        continue
    else:
        print(i)
        if i % 3 == 0:
            s = s + i

print('Soma: ', s)






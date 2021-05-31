list1 = []
list2 = []
for i in range(500, 800):
    list1.append(i)
for t in range(800, 500, -1):
    list2.append(t)

print(f'A soma dos números pares são: {sum(list1)}')
print(f'A soma dos números ímpares são: {sum(list2)}')


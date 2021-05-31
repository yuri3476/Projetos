import random
from time import sleep

x = random.randint(0, 5)

print('\033[31m-=-\033[m' * 20)
print('\033[32mVou pensar em um número entre 0 e 5! Tente adivinhar...\033[m')
print('\033[31m-=-\033[m' * 20)
num = int(input('\033[36mEm que número eu pensei?\033[m '))
print('\033[33mProcessando...\033[m')
sleep(2)
if num == x:
    print('\033[35mParabéns! Você conseguiu me vencer!\033[m')
else:
    print('\033[35mGANHEI! Eu pensei no número {} e não no {}!\033[m '.format(x, num))



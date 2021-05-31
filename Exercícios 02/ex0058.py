import random
from time import sleep
tent = 1
x = random.randint(0, 10)

print('\033[31m-=-\033[m' * 20)
print('\033[32mVou pensar em um número entre 0 e 10! Tente adivinhar...\033[m')
print('\033[31m-=-\033[m' * 20)


num = int(input('\033[36mEm que número eu pensei?\033[m '))
print('\033[33mProcessando...\033[m')
sleep(2)


while num != x:
    num1 = int(input('\033[36mVocê errou.Tente adivinhar novamente:\033[m '))
    tent += 1
    print('\033[33mProcessando...\033[m')
    sleep(2)
    if num1 == x:
        print('\033[32mParabéns! Você acertou o número. Teve que usar {} tentativas!\033[m'.format(tent))
        break










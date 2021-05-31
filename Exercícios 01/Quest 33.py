qnt_C = 0
tempos = 0
num_V = 0
nome_V = ''
tempo_V = 9999999999
while True:
    num = int(input('Informe o número do carro: '))
    if num < 0:
        break
    nome = str(input('Informe o nome do piloto: '))
    qnt_C += 1
    tempo = int(input('Informe o tempo (em segundos) registrado no cronômetro: '))
    tempos += tempo
    qnt_P = int(input('Informe a quantidade de punições: '))
    if tempo < tempo_V:
        tempo_V = 0
        tempo_V += tempo
        num_V = 0
        num_V += num
        nome_V = ''
        nome_V += nome

    print()

media = tempos / qnt_C
horas = (media / 3600)
minutos = (media // 60)
segundos = (media % 60)
print()
print(f'A quantidade de carros participantes foi de {qnt_C}.')
print(f'O tempo médio da prova foi de: {horas:.0f}:{minutos:.0f}:{segundos:.0f}. ')
print(f'O número do carro: {num_V} | Nome do piloto: {nome_V} | Tempo (em segundos) no vencedor: {tempo_V}')
print(f'O número do carro, o nome de piloto e o tempo (em segundos) do segundo colocado na competição.')

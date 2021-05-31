dados = {}
gols = []

dados['Nome'] = str(input('Nome do jogador: '))
d = int(input(f'Quantas partidas {dados["Nome"]} jogou: '))
for i in range(d):
    g = int(input(f'Quantos gols na partida {i+1}? '))
    gols.append(g)
totgol = sum(gols)
dados['gols'] = gols
dados['Total'] = totgol

print('-=' * 30)
print(dados)

print('-=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')

print('-=' * 30)
print(f'O jogador {dados["Nome"]} jogou {d} partidas.')
for c in range(len(dados["gols"])):
    print(f' ► Na partida {c+1}, fez {dados["gols"][c]} gol(s).')
print(f'No total ele fez {dados["Total"]} gols.')








times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico Paranaense', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')

print('Times do Brasileirão: ', times)
print('=' * 150)
print('Os 5 primeiros colocados foram: ', (times[0], times[1], times[2], times[3], times[4]))
print('=' * 150)
print('Os 4 últimos colocados foram: ', (times[16], times[17], times[18], times[19]))
print('=' * 150)
print('Os times em ordem alfabética: ', sorted(times))
print('=' * 150)
col = times.index('Chapecoense')
co = col + 1
print(f'A chapecoense está na {co}ª colocação!')

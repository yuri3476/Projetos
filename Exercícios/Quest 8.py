ganho = float(input('Ganho por hora: ').replace(',', '.'))
horas = float(input('Horas trabalhadas no mes: ').replace(',', '.'))

ganhototal = ganho*horas
print('Salario total do mes R$ %.2f' % ganhototal)


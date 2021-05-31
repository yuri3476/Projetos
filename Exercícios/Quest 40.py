
Cand_Masculino = 0
Cand_Feminino = 0
Homens_exp = 0
total_homens_exp = 0
relacao_homens = []
relacao_mulheres = []
while True:
    print('\033[36m-=\033[m' * 40)
    num_inscricao = int(input('Informe o número de inscrição -> [Digite número negativo para sair]: '))
    if num_inscricao < 0:
        break
    nome = str(input('Informe o nome do candidato: '))
    idade = int(input('Informe a idade: '))
    sexo = int(input('Informe  o sexo -> [1 = masculino ou 2 = feminino]: '))
    if sexo == 1:
        Cand_Masculino += 1
    if sexo == 2:
        Cand_Feminino += 1
    exp_servico = int(input('Informe se possui experiência no serviço -> (1 = sim ou 0 = não): '))
    print()
    if sexo == 1 and exp_servico == 1:
        total_homens_exp += 1
        Homens_exp += idade
    if sexo == 1 and exp_servico == 0 and idade > 40:
        relacao_homens += [f'Nome: {nome}  | idade: {idade} | sexo: Masculino ']
    if sexo == 2 and exp_servico == 1:
        relacao_mulheres += [f'Nome: {nome} | idade: {idade} | sexo: Feminino ']
media = 0
if total_homens_exp > 1:
    media = Homens_exp/total_homens_exp
print()
print()
print('\033[31m-=\033[m'*42)
print(f'O número de candidatos do sexo feminino foi {Cand_Feminino} e do sexo masculino foi {Cand_Masculino}.')
print('\033[31m-=\033[m'*42)
print(f'A idade média dos homens que já possuem experiência no serviço é {media:.2f}.')
print('\033[31m-=\033[m'*42)
print(f'A relação dos homens com mais de 40 anos que não possuem experiência no serviço: ')
for k in range(0, len(relacao_homens)):
    print(relacao_homens[k])
print('\033[31m-=\033[m'*42)
print(f'A relação das mulheres que já possuem experiência no serviço: ')
for k in range(0, len(relacao_mulheres)):
    print(relacao_mulheres[k])
print('\033[31m-=\033[m'*42)






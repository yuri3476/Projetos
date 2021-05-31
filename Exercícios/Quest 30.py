listaNotas = []
notasAluno = []
print ('Notas dos Alunos')
for i in range(10):
    media = 0
    notasAluno = []
    print ('Aluno: ' + str(i + 1))
    for j in range(4):
        notasAluno.append(float(input('Nota: ' + str(j + 1) + '\n')))
        media += notasAluno[j]
        print (media)
    media = media/4
    listaNotas.append(media)

print(listaNotas)

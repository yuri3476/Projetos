import pandas as pd


def Cadastro_Professor_Aluno(dados, matricula_prof, nome_prof, data_prof,
                             arquivos):
    dados['Matricula'] += [matricula_prof]
    dados['Nome'] += [nome_prof]
    dados['Data de nascimento'] += [data_prof]
    excel = pd.DataFrame(data=dados)
    with pd.ExcelWriter(arquivos) as writer:
        excel.to_excel(writer, index=False)


def Carregamento_Excel(arquivo_excel, index_coluna):
    df = pd.read_excel(arquivo_excel)
    df.set_index(index_coluna).T.to_dict('list')
    return df.to_dict(orient='list')


def Cadastro_Notas(nota, codigo, nome_disci, nome_profnot, matricula_alu, nota1, nota2):
    nota['Cod_disci'] += [codigo]
    nota['Disciplina'] += [nome_disci]
    nota['Aluno'] += [matricula_alu]
    nota['Professor'] += [nome_profnot]
    nota['Nota 1'] += [nota1]
    nota['Nota 2'] += [nota2]
    nota['Nota Final'] += [(nota1 + nota2)/2]
    excel = pd.DataFrame(data=nota)
    with pd.ExcelWriter('Notas_Alunos.xlsx') as writer:
        excel.to_excel(writer, index=False)


def Cadastro_Disciplina(dados_disc, codigo_dic, nome_dic, matricula_dic):
    dados_disc['Codigo_Disciplina'] += [codigo_dic]
    dados_disc['Nome_Disciplina'] += [nome_dic]
    dados_disc['Matricula_Professor_Disciplina'] += [matricula_dic]
    excel = pd.DataFrame(data=dados_disc)
    with pd.ExcelWriter('Disciplina_Cadastradas.xlsx') as writer:
        excel.to_excel(writer, index=False)

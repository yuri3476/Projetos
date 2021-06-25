import pandas as pd

def carregar_excel(arquivo_excel, index_coluna):
    df = pd.read_excel(arquivo_excel)
    df.set_index(index_coluna).T.to_dict('list')
    return df.to_dict(orient='list')


cadastro_prop = {'Nome': [], 'CPF': [], 'data_nasc_inq': []}

try:
    cadastro_prop = carregar_excel('Proprietarios.xlsx', 'Nome')
except FileNotFoundError:
    pass

Imoveis_Cadastrados = {'Codigo': [], 'CPF_PROP': [], 'Tipo': [], 'Endereço': [], 'Valor_Aluguel': [],
                       'Status': [], 'Data_inicio': [], 'Data_f': []}
try:
    Imoveis_Cadastrados = carregar_excel('Imoveis_Cadastrados.xlsx', 'Codigo')
except FileNotFoundError:
    pass

Alugueis_Registrados = {'Codigo': [], 'CPF_INQ': [], 'Tipo': [], 'Endereço': [], 'Aluguel': [],
                        'Status': [], 'Data_i': [], 'Data_f': []}
try:
    Alugueis_Registrados = carregar_excel('Alugueis_Registrados.xlsx', 'Codigo')
except FileNotFoundError:
    pass

comissoes = {'Codigo': [], 'Arrecadacao': []}

try:
    comissoes = carregar_excel('Arrecadacao.xlsx', 'Codigo')
except FileNotFoundError:
    pass

inquilino_cadastro = {'Nome': [], 'CPF': [], 'Data de Nascimento': []}

try:
    inquilino_cadastro = carregar_excel('Inquilinos.xlsx', 'Nome')
except FileNotFoundError:
    pass

registro_alug = {'CPF': [], 'Codigo': [], 'Data de Inicio': [], 'Data do Fim': []}

try:
    registro_alug = carregar_excel('Registro Aluguel.xlsx', 'CPF')
except FileNotFoundError:
    pass

#Listas

CPF_TEMP = list(cadastro_prop.values())
comissoes_t = list(comissoes.values())
imoveis_t = list(Imoveis_Cadastrados.values())
cpf_inq = list(inquilino_cadastro.values())
stts = list()


class proprietario:
    def __init__(self, nome, cpf_prop, data_nasc):
        self.nome = nome
        self.cpf_prop = cpf_prop
        self.data_nasc = data_nasc

    def Armazenar_Nome(self):
        return self.nome

    def Armazenar_CPF(self):
        return self.cpf_prop

    def Armazenar_Data(self):
        return self.data_nasc

class Imovel:
    # Classe para cadastro de imoveis
    def __init__(self, Codigo_Imovel, Cpf_Propr, Tipo, Endereco,
                 Valor_Aluguel, Status, Data_inicio, Data_fim):
        self.Codigo_Imovel = Codigo_Imovel
        self.Cpf_Propr = Cpf_Propr
        self.Tipo = Tipo
        self.Endereco = Endereco
        self.Valor_Aluguel = Valor_Aluguel
        self.Status = Status
        self.Data_inicio = Data_inicio
        self.Data_fim = Data_fim

    def Armazenar_Codigo(self):
        return self.Codigo_Imovel

    def Armazenar_Cpf_Propr(self):
        return self.Cpf_Propr

    def Armazenar_Tipo(self):
        return self.Tipo

    def Armazenar_Endereco(self):
        return self.Endereco

    def Armazenar_Aluguel(self):
        return self.Valor_Aluguel

    def Armazenar_Status(self):
        return self.Status

    def Armazenar_data_i(self):
        return self.Data_inicio

    def Armazenar_data_f(self):
        return self.Data_fim

class inquilino:
    def __init__(self, nome_inquilino, cpf_inq, data_nasc_inq):
        self.nome_inquilino = nome_inquilino
        self.cpf_inq = cpf_inq
        self.data_nasc_inq = data_nasc_inq

    def Armazenar_Nome_inq(self):
        return self.nome_inquilino

    def Armazenar_CPF_inq(self):
        return self.cpf_inq

    def Armazenar_Data_inq(self):
        return self.data_nasc_inq

class aluguel:
    def __init__(self, cpf_inq, codigo, data_inicio, data_fim):
        self.cpf_inq = cpf_inq
        self.codigo = codigo
        self.data_inicio = data_inicio
        self.data_fim = data_fim

    def Armazenar_Cpf_Inq(self):
        return self.cpf_inq

    def Armazenar_Codigo(self):
        return self.codigo

    def Armazenar_Data_Inicio(self):
        return self.data_inicio

    def Armazenar_Data_Fim(self):
        return self.data_fim

def w_excel(Cadastro_Proprietario, arquivo):
    excel = pd.DataFrame(data=Cadastro_Proprietario)
    with pd.ExcelWriter(arquivo) as writer:
        excel.to_excel(writer, index=False)

def arrecada(Cadastro_Proprietario, codigo, arrecada, arquivo):
    # função para cadastrar os imoveis no dicionario e excel

    Cadastro_Proprietario['Codigo'] += [codigo]
    Cadastro_Proprietario['Arrecadacao'] += [arrecada]
    excel = pd.DataFrame(data=Cadastro_Proprietario)
    with pd.ExcelWriter(arquivo) as writer:
        excel.to_excel(writer, index=False)

#EXCEL

def Cadastro(Cadastro_Proprietario, dados, arquivo):

    Cadastro_Proprietario['Nome'] += [dados.Armazenar_Nome()]
    Cadastro_Proprietario['CPF'] += [dados.Armazenar_CPF()]
    Cadastro_Proprietario['data_nasc_inq'] += [dados.Armazenar_Data()]
    excel = pd.DataFrame(data=Cadastro_Proprietario)
    with pd.ExcelWriter(arquivo) as writer:
        excel.to_excel(writer, index=False)


def Cadastro_imovel(Cadastro_Proprietario, dados, arquivo):
    Cadastro_Proprietario['Codigo'] += [dados.Armazenar_Codigo()]
    Cadastro_Proprietario['CPF_PROP'] += [dados.Armazenar_Cpf_Propr()]
    Cadastro_Proprietario['Tipo'] += [dados.Armazenar_Tipo()]
    Cadastro_Proprietario['Endereço'] += [dados.Armazenar_Endereco()]
    Cadastro_Proprietario['Valor_Aluguel'] += [dados.Armazenar_Aluguel()]
    Cadastro_Proprietario['Status'] += [dados.Armazenar_Status()]
    Cadastro_Proprietario['Data_inicio'] += [dados.Armazenar_data_i()]
    Cadastro_Proprietario['Data_f'] += [0]
    excel = pd.DataFrame(data=Cadastro_Proprietario)
    with pd.ExcelWriter(arquivo) as writer:
        excel.to_excel(writer, index=False)


def Cadastro_aluguel(Cadastro_Proprietario, dados, arquivo):
    Cadastro_Proprietario['Codigo'] += [dados.Armazenar_Codigo()]
    Cadastro_Proprietario['CPF_INQ'] += [dados.Armazenar_Cpf_Propr()]
    Cadastro_Proprietario['Tipo'] += [dados.Armazenar_Tipo()]
    Cadastro_Proprietario['Endereço'] += [dados.Armazenar_Endereco()]
    Cadastro_Proprietario['Aluguel'] += [dados.Armazenar_Aluguel()]
    Cadastro_Proprietario['Status'] += [dados.Armazenar_Status()]
    Cadastro_Proprietario['Data_i'] += [0]
    Cadastro_Proprietario['Data_f'] += [0]
    excel = pd.DataFrame(data=Cadastro_Proprietario)
    with pd.ExcelWriter(arquivo) as writer:
        excel.to_excel(writer, index=False)

def Cadastro_inquilino(Cadastro_Inquilino, dados, arquivo):

    Cadastro_Inquilino['Nome'] += [dados.Armazenar_Nome_inq()]
    Cadastro_Inquilino['CPF'] += [dados.Armazenar_CPF_inq()]
    Cadastro_Inquilino['Data de Nascimento'] += [dados.Armazenar_Data_inq()]
    excel = pd.DataFrame(data=Cadastro_Inquilino)
    with pd.ExcelWriter(arquivo) as writer:
        excel.to_excel(writer, index=False)

def Registro_Alugueis(Reg_Aluguel, dados, arquivo):
    Reg_Aluguel['CPF'] += [dados.Armazenar_Cpf_Inq()]
    Reg_Aluguel['Codigo'] += [dados.Armazenar_Codigo()]
    Reg_Aluguel['Data de Inicio'] += [dados.Armazenar_Data_Inicio()]
    Reg_Aluguel['Data do Fim'] += [dados.Armazenar_Data_Fim()]
    excel = pd.DataFrame(data=Reg_Aluguel)
    with pd.ExcelWriter(arquivo) as writer:
        excel.to_excel(writer, index=False)

#CODIGO

#PROPRIETARIO
def cadastro_proprietario():
    print('\033[1;34m♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦Setor de Cadastro a Proprietário♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦')
    while True:
        sair = input('\nDeseja sair? [S/N]: ').upper()
        if sair == 'S':
            break
        else:
            pass
        while True:
            nome = input('Informe o nome do proprietário: ')
            while True:
                cpf_prop = input('Informe o CPF do proprietário (11 números): ')
                if len(cpf_prop) == 11 and cpf_prop.isnumeric():
                    break
            while True:
                data_nasc = str(input('Informe a data de nascimento: '))
                if len(data_nasc) == 8 and data_nasc.isnumeric():
                    break
            dados = proprietario(nome, cpf_prop, data_nasc)
            Cadastro(cadastro_prop, dados, 'Proprietarios.xlsx')
            print('\nProprietário Cadastrado com Sucesso!')
            break

#IMOVEIS
def cadastro_imovel():
    print('\033[1;34m♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦Setor de Cadastro de Imóvel♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦')
    while True:
        sair = input('\nDeseja sair? [S/N]: ').upper()
        if sair == 'S':
            break
        else:
            pass
        codigo = ''
        while type(codigo) != int or codigo in imoveis_t[0]:
            try:
                codigo = int(input('\nDigite o código do imóvel: '))
            except ValueError:
                print('\nCódigo Inválido!')
            if codigo in imoveis_t[0]:
                print('\nImóvel já cadastrado!')
        while True:
            cpf_prop = input('Informe o CPF do proprietário (11 números): ')
            if len(cpf_prop) == 11 and cpf_prop.isnumeric():
                break
        tipo = ''
        while tipo not in ['CASA', 'APARTAMENTO']:
            tipo = input('\nDigite o tipo do imóvel [CASA/APARTAMENTO]: ').upper()
            if tipo not in ['CASA', 'APARTAMENTO']:
                print('\nDigito Inválido!')
        endereco = input('Digite o endereço do imóvel: ')
        valor_aluguel = float(input('Digite o valor do aluguel: '))
        status = ''
        while status not in ['S', 'N']:
            status = input('\nA propriedade encontra-se alugado? [S/N]: ').upper()
            if status not in ['S', 'N']:
                print('\nDigito Inválido!')
        data_inicio = 0
        data_fim = 0
        dados_imovel = Imovel(codigo, cpf_prop, tipo, endereco, valor_aluguel,
                                      status, data_inicio, data_fim)
        Cadastro_imovel(Imoveis_Cadastrados, dados_imovel, 'Imoveis_Cadastrados.xlsx')
        print('\nImóvel cadastrado com sucesso!')

#INQUILINOS
def cadastro_inq():
    print('\033[1;34m♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦Setor de Cadastro a Inquilino♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦')
    while True:
        sair = input('\nDeseja sair? [S/N]: ').upper()
        if sair == 'S':
            break
        else:
            pass
        while True:
            nome_inquilino = input('Informe o nome do inquilino: ')
            while True:
                cpf_inq = input('Informe o CPF do inquilino (11 números): ')
                if len(cpf_inq) == 11 and cpf_inq.isnumeric():
                    break
            while True:
                data_nasc_inq = str(input('Informe a data de nascimento: '))
                if len(data_nasc_inq) == 8 and data_nasc_inq.isnumeric():
                    break
            dados_inq = inquilino(nome_inquilino, cpf_inq, data_nasc_inq)
            Cadastro_inquilino(inquilino_cadastro, dados_inq, 'Inquilinos.xlsx')
            print('\nInquilino Cadastrado com Sucesso!')
            break


#REGISTRO
def registro_aluguel():
    print('\033[1;34m♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦Setor de Registro de Aluguel♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦')
    data_fim = '-'
    while True:
        sair = input('\nDeseja sair? [S/N]: ').upper()
        if sair == 'S':
            break
        else:
            pass
        while True:
            cpf_in = input('Informe o CPF do inquilino (11 números): ')
            codigo_im = int(input('Digite o código do imóvel: '))
            if cpf_in in cpf_inq[1] and codigo_im in imoveis_t[0]:
                local = Imoveis_Cadastrados['Codigo'].index(codigo_im)
                if Imoveis_Cadastrados['Status'][local] == 'N':
                    while True:
                        data = input('Digite a data de finalização do aluguel: ').strip()
                        if len(data) == 8 and data.isnumeric():
                            break
                    Imoveis_Cadastrados['Status'][local] = 'S'
                    Imoveis_Cadastrados['Data_inicio'][local] = data
                    w_excel(Imoveis_Cadastrados, 'Imoveis_Cadastrados.xlsx')
                    print('\nAluguel Realizado com sucesso! ')
                    imovel_Aluguel = Imovel(codigo_im, cpf_in, Imoveis_Cadastrados['Tipo'][local],
                                                    Imoveis_Cadastrados['Endereço'][local],
                                                    Imoveis_Cadastrados['Valor_Aluguel'][local],
                                                    Imoveis_Cadastrados['Status'][local], data, data_fim)

                    Cadastro_aluguel(Alugueis_Registrados, imovel_Aluguel, 'Alugueis_Registrados.xlsx')

                    if codigo_im not in comissoes_t[0]:
                        arrecada(comissoes, codigo_im, Imoveis_Cadastrados['Valor_Aluguel'][local], 'Arrecadacao.xlsx')
                    else:
                        x = comissoes['Codigo'].index(codigo_im)
                        comissoes['Arrecadacao'][x] += Imoveis_Cadastrados['Valor_Aluguel'][local]
                        w_excel(comissoes, 'Arrecadacao.xlsx')
                    break
                else:
                    print('\nImóvel já está alugado!')
            else:
                print('\nO cpf do inquilino ou código do imovel não está cadastrado!')
                break


def finalizar_aluguel():
    print('\033[1;34m♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦Setor de Finalizar Aluguel♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦')
    while True:
        sair = input('\nDeseja sair? [S/N]: ').upper()
        if sair == 'S':
            break
        else:
            pass
        while True:
            cpf_in = input('Digite o CPF do inquilino (11 números) |Digite [0] para sair|: ')
            if cpf_in == '0':
                break
            codigo_im = int(input('Digite o código do imóvel: '))
            if cpf_in in cpf_inq[1] and codigo_im in imoveis_t[0]:
                local_f = Imoveis_Cadastrados['Codigo'].index(codigo_im)
                if cpf_in in cpf_inq[1] and codigo_im in imoveis_t[0] \
                        and Imoveis_Cadastrados['Status'][local_f] == 'S':
                    while True:
                        data_final = input('Digite a data de finalização do aluguel: ').strip()
                        if len(data_final) == 8 and data_final.isnumeric():
                            break

                    Imoveis_Cadastrados['Data_f'][local_f] = data_final
                    Imoveis_Cadastrados['Status'][local_f] = 'N'
                    w_excel(Imoveis_Cadastrados, 'Imoveis_Cadastrados.xlsx')
                    print('\nAluguel finalizado com sucesso!')

                    local_f = Alugueis_Registrados['Codigo'].index(codigo_im)
                    Alugueis_Registrados['Codigo'][local_f] = f'{codigo_im}-F'
                    Alugueis_Registrados['Data_f'][local_f] = data_final
                    Alugueis_Registrados['Status'][local_f] = 'F'
                    w_excel(Alugueis_Registrados, 'Alugueis_Registrados.xlsx')
                else:
                    print('\nO imóvel encontra-se desalugado!')
            else:
                print('\nO cpf do inquilino ou código do imovel não foi encontrado no sistema!')
                break

def relatorio_prop():
    try:
        print(pd.read_excel('Proprietarios.xlsx'))
    except FileNotFoundError:
        print("\nNão tem proprietarios cadastradas!")


def relatorio_imovel():
    try:
        print(pd.read_excel('Imoveis_Cadastrados.xlsx'))
    except FileNotFoundError:
        print("\nNão tem imóveis cadastrados!")


def relatorio_inquilino():
    try:
        print(pd.read_excel('Inquilinos.xlsx'))
    except FileNotFoundError:
        print("\nNão tem inquilinos cadastrados!")


def relatorio_alugueis():
    try:
        print(pd.read_excel('Alugueis_Registrados.xlsx'))
    except FileNotFoundError:
        print("\nNão tem alugueis cadastrados!")


def relatorio_comissoes():
    try:
        print(pd.read_excel('Arrecadacao.xlsx'))
    except FileNotFoundError:
        print("\nNão tem alugueis cadastrados!")


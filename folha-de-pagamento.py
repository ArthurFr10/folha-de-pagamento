import os

def limpa_tela():
    os.system("cls || clear")

class Funcionario():

    def __init__(self, nome:str, senha:str):
        self.nome = nome
        self.senha = senha

def criando_matricula():
    lista_funcionario = []
    lista_nome_funcionario = []
    lista_senha_funcionario =[]
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
    funcionario = Funcionario(nome, senha)
    lista_funcionario.append(funcionario)
    lista_nome_funcionario.append(nome)
    lista_senha_funcionario.append(senha)
    print("Cadastro feito com sucesso")

def lendo_matricula():
    if Funcionario.nome ==  and Funcionario.senha != Funcionario.senha:
        print("Acesso confirmado")
    else:
        print("Tente novamente")

    
limpa_tela()
while True:
    opcao = int(input("""Seja Bem Vindo ao sistema. O que deseja fazer?
    1 - Criar uma nova matrícula
    2 - Acessar conta já existente
    """))
    
    match opcao:
        case 1:
            criando_matricula()
        
        case 2:
            lendo_matricula()
            
            

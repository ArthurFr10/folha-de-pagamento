import os

def limpa_tela():
    os.system("cls || clear")

class Funcionario():

    def __init__(self, nome:str, senha:str):
        self.nome = nome
        self.senha = senha
        
lista_funcionario = []

def criando_matricula():
    nome_cadastro = input("Digite seu nome: ")
    senha_cadastro = input("Digite sua senha: ")
    funcionario = Funcionario(nome_cadastro, senha_cadastro)
    lista_funcionario.append(funcionario)
    limpa_tela()
    print("Cadastro feito com sucesso")


def lendo_matricula():
    while True:
        nome_login = input("Digite o seu nome: ")
        senha_login = input("Digite sua senha: ")
        for funcionario in lista_funcionario:
            if funcionario.nome == nome_login and funcionario.senha == senha_login:
                limpa_tela()
                print("Acesso liberado")
                print(f"Seja bem vindo ao sistema {funcionario.nome}!")
                return funcionario
            limpa_tela()
            print("Tente novamente")
            

def perguntando(a):
    a.salario_bruto = input("Digite o seu salário bruto: ")
    a.vale_transporte = input("Deseja receber o vale transporte?")
    a.vale_refeicao = input("Digite o valor do vale refeição: ")
    lista_funcionario.append(a)
    
limpa_tela()
while True:
    opcao = int(input("""Seja Bem Vindo ao sistema. O que deseja fazer?
1 - Criar uma nova matrícula
2 - Acessar conta já existente
=>"""))
    match opcao:
        case 1:
            criando_matricula()
            
        case 2:
            funcionario = lendo_matricula()
            perguntando(funcionario)
            break

                
    



        
        

            
            

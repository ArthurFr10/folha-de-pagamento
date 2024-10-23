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
    a.salario_bruto = float(input("Digite o seu salário bruto: "))
    a.dependentes = int(input)
    a.vale_transporte = input("Deseja receber o vale transporte(sim / não)?")
    a.vale_refeicao = float(input("Digite o valor do vale refeição: "))
    lista_funcionario.append(a)

def INSS(salario):
    if salario <= 1100.00:
        desconto = salario * 0.075
        salario_liquido = salario - desconto
        return salario_liquido
    elif salario >= 1100.01 and salario <= 2203.48:
        desconto = salario * 0.09
        salario_liquido = salario - desconto
        return salario_liquido
    elif salario >= 2203.49 and salario <= 3305.22:
        desconto = salario * 0.12
        salario_liquido = salario - desconto
        return salario_liquido
    elif salario >= 3305.23 and salario <= 6433.57:
        desconto = salario * 0.14
        salario_liquido = salario - desconto
        return salario_liquido
    else:
        salario_liquido = salario - 854.36
        return salario_liquido

def IRRF(salario):
    if salario >= 2259.21 and salario <= 2826.65:
        desconto = salario * 0.075
        salario_liquido = salario - desconto
        return salario_liquido
    elif salario >= 2826.66 and salario <= 3751.05:
        desconto = salario * 0.15
        salario_liquido = salario - desconto
        return salario_liquido
    elif salario >= 3751.06 and salario <= 4664.68:
        desconto = salario * 0. 
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
while True:



                
    



        
        

            
            

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
            
def perguntando():
    salario_bruto = float(input("Digite o seu salário bruto: "))
    dependentes = int(input("Digite quantos dependentes você tem: "))
    vale_transporte = bool(input("Deseja receber o vale transporte(sim / não)?"))
    vale_refeicao = float(input("Digite o valor do vale refeição: "))
    return salario_bruto, dependentes, vale_transporte, vale_refeicao
    

def INSS(salario):
    if salario <= 1100.00:
        desconto = salario * 0.075
        return desconto
    elif salario >= 1100.01 and salario <= 2203.48:
        desconto = salario * 0.09
        return desconto
    elif salario >= 2203.49 and salario <= 3305.22:
        desconto = salario * 0.12
        return desconto
    elif salario >= 3305.23 and salario <= 6433.57:
        desconto = salario * 0.14
        return desconto
    else:
        desconto = salario - 854.36
        return desconto

def IRRF(salario, depedente):
    if salario >= 2259.21 and salario <= 2826.65:
        desconto = salario * 0.075
        return desconto
    elif salario >= 2826.66 and salario <= 3751.05:
        desconto = salario * 0.15
        return desconto
    elif salario >= 3751.06 and salario <= 4664.68:
        desconto = salario * 0.225
        return desconto
    elif salario >= 4664.68:
        desconto = salario * 0.275
        return desconto
    deducao_por_depedente = 189.59
    deducao_total = depedente - deducao_por_depedente
    return deducao_total

def vale_transportes(salario, variavel_transporte):
    if variavel_transporte == "sim":
        desconto = salario * 0.06
        return desconto
    return 0

def vale_refeicoes(salario, variavel_refeicao):
    desconto = variavel_refeicao * 0.20
    return desconto

def plano_de_saude(salario, dependente):
    desconto = dependente * 150.00
    return desconto
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
            salario_bruto, dependentes, vale_transporte, vale_refeicao = perguntando()
            break
desconto_inss = INSS(salario_bruto)
desconto_irff = IRRF(salario_bruto, dependentes)
desconto_vale_transporte = vale_transportes(salario_bruto, vale_transporte)
desconto_vale_refeicao = vale_refeicoes(salario_bruto, vale_refeicao)
desconto_plano_de_saude = plano_de_saude(salario_bruto, dependentes)
salario_liquido = salario_bruto - (desconto_inss + desconto_irff + desconto_vale_transporte + desconto_vale_refeicao + desconto_plano_de_saude)
print(f"{funcionario.nome} tem de salário líquido: R$ {salario_liquido:.2f}")


                
    



        
        

            
            

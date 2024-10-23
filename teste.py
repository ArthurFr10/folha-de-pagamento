import os

def limpa_tela():
    os.system("cls" if os.name == "nt" else "clear")

class Usuario:
    def __init__(self, nome: str, senha: str):
        self.nome = nome
        self.senha = senha

usuarios = []  # Lista para armazenar os usuários

def criar_cadastro():
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")

    # Verifica se o nome já está cadastrado
    for usuario in usuarios:
        if usuario.nome == nome:
            print("Nome de usuário já cadastrado. Tente novamente.")
            return
    
    novo_usuario = Usuario(nome, senha)
    usuarios.append(novo_usuario)
    limpa_tela()
    print("Cadastro feito com sucesso!")

def realizar_login():
    while True:
        nome = input("Digite seu nome: ")
        senha = input("Digite sua senha: ")

        for usuario in usuarios:
            if usuario.nome == nome and usuario.senha == senha:
                limpa_tela()
                print("Acesso liberado!")
                return usuario
        
        limpa_tela()
        print("Nome ou senha incorretos. Tente novamente.")
        continuar = input("Deseja tentar novamente? (sim/não): ")
        if continuar.lower() != 'sim':
            break

def perguntas_adicionais(usuario):
    print(f"Bem-vindo, {usuario.nome}!")
    idade = input("Quantos anos você tem? ")
    cidade = input("Qual é a sua cidade? ")
    profissao = input("Qual é a sua profissão? ")
    
    print("\nObrigado por responder às perguntas!")
    print(f"Idade: {idade}, Cidade: {cidade}, Profissão: {profissao}")

def main():
    limpa_tela()
    while True:
        opcao = input("""Seja bem-vindo ao sistema. O que deseja fazer?
1 - Criar um novo cadastro
2 - Fazer login
3 - Sair
=> """)
        
        if opcao == "1":
            criar_cadastro()
        elif opcao == "2":
            usuario = realizar_login()
            if usuario:
                perguntas_adicionais(usuario)
        elif opcao == "3":
            print("Saindo do sistema. Até logo!")
            break
        else:
            limpa_tela()
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
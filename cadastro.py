# Cria um dicionário vazio para armazenar os dados de cadastro
cadastros = {}

novos_cadastro = {}
# Função para registrar um novo usuário
def registrar_usuario():
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")
    cadastros[email] = {'Nome': nome, 'Senha': senha}
    print("Cadastro realizado com sucesso!")
    
def listar_usuarios():
    print("\nLista de Usuários Registrados:")
    for email, dados in cadastros.items():
        print(f"Email: {email}")
        print(f"Nome: {dados['Nome']}")
        print(f"Senha: {dados['Senha']}\n")

# Menu principal
while True:
    print("\nEscolha uma opção:")
    print("1. Registrar novo usuário")
    print("2. Listar usuários registrados")
    print("3. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        registrar_usuario()
    elif opcao == '2':
        listar_usuarios()
    elif opcao == '3':
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")

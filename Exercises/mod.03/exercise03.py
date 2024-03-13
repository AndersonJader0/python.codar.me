usuario = "admin"
senha = "12345"
autenticacao = False

while autenticacao == False:
    usuarioLogin = input("Digite o nome de usuário: ")
    senhaLogin = input("Digite a senha: ")
    if usuarioLogin == usuario and senhaLogin == senha:
        autenticacao = True
    else:
        print("Login inválido")

print("Login realizado com sucesso!")
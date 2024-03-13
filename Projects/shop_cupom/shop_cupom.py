##import validadorCPF
import os

clientes = []

select = int(input("#---- Opções do sistema ----#\n# 1- Cadastrar cliente      #\n# 2- Consultar cadastros    #\n# 3- Cadastrar compra       #\n"))

if select == 1:
    print("## tabela registro ##\n# nome:            #\n# idade:           #\n# cpf:             #\n# loja_fidelidade: #")
    nome = input("Digite o nome:")
    print("\n" * os.get_terminal_size().lines)

    print("## tabela registro ##\n# nome:", nome, "\n# idade:           #\n# cpf:             #\n# loja_fidelidade: #")
    idade = input("Digite a idade")
    print("\n" * os.get_terminal_size().lines)

    print("## tabela registro ##\n# nome:", nome, "\n# idade:", idade,"\n# cpf:             #\n# loja_fidelidade: #")
    ##Validador = validadorCPF.ValidadorCPF()
    ##Validador.solicitar_CPF
    CPF = input("Digite o CPF: ")
    print("\n" * os.get_terminal_size().lines)

    print("## tabela registro ##\n# nome:", nome, "\n# idade:", idade,"\n# cpf:", CPF,"\n# loja_fidelidade: #")
    fidelidade = input("Registrar fidelidade: S/N")
    clientes.append(nome, idade, CPF, fidelidade)

    print(clientes[0])

    #print("## tabela registro ##\n# nome:", nome, "\n# idade:", idade,"\n# cpf:", CPF,"\n# loja_fidelidade: ", fidelidade)
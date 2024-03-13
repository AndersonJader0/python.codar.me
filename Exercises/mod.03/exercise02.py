import sys


valor1 = float(input("Digite um número: "))
valor2 = float(input("Digite outro número: "))
operador = input("Digite um operador: ")

if operador == "+":
    print(valor1 + valor2)
elif operador == "-":
    print(valor1 - valor2)
elif operador == "x":
    print(valor1 * valor2)
elif operador == "/":
    if valor2 == 0:
        print(valor1)
        sys.exit()
    print(valor1 / valor2)
else:
    "Operador digitado não reconhecível"
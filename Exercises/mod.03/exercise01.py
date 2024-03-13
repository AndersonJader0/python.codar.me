#Programa FizzBuzz

x = int(input("Digite um número inteiro: "))

multiplo_de_5 = x % 5 == 0
multiplo_de_3 = x % 3 == 0


if multiplo_de_5 == True and multiplo_de_3 == True:
    print("FizzBuzz")
elif multiplo_de_5 == True and multiplo_de_3 == False:
    print("Buzz")
elif multiplo_de_5 == False and multiplo_de_3 == True:
    print("Fizz")
else:
    print("Nem fizz e nem Buzz")
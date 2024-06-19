# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

n1 = float(input("Informe um número: "))

if n1 == 0:
    print("O valor é Nulo.")
elif n1 > 0:
    print("O valor é Positivo.")
else:
    print("O valor é Negativo.")
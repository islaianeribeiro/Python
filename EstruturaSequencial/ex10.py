#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

c = float(input("Qual a temperatura em Graus Celsius? "))
f = c * 1.8 + 32
print(f"A temperatura em Farenheits é: {f:.1f}")
#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

f = float(input("Qual a temperatura em farenheits? "))
c = 5 * ((f-32) / 9)
print(f"A temperatura em graus Celsius é : {c:.1f}")
# Faça um Programa que peça dois números e imprima o maior deles.

n1 = float(input("Informe um número: "))
n2 = float(input("Informe outro número: "))

if n1 > n2:
    print(f"O maior número é: {n1:.1f}")
else: 
    print(f"O maior número é: {n2:.1f}")
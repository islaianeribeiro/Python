#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#a. O produto do dobro do primeiro com metade do segundo.
#b. A soma do triplo do primeiro com o terceiro.
#c. O terceiro elevado ao cubo.

n1 = int(input("Informe um número inteiro: "))
n2 = int(input("Informe outro número inteiro: "))
n3 = float(input("Informe um número real: "))

a = (n1 * 2) + (n2 / 2)
b = n1 * 3 + n3
c = n3 ** 3

print(f"O produto do dobro do primeiro com metade do segundo: {a:.1f}")
print(f"A soma do triplo do primeiro com o terceiro: {b:.1f}")
print(f"O terceiro elevado ao cubo: {c:.1f}")
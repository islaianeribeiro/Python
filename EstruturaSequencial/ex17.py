#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

medida = float(input("Informe a área em metros quadrados: "))
litros = medida / 6
latas = math.ceil(litros / 18)
galoes = math.ceil(litros / 3.6)
preco1 = latas * 80
preco2 = galoes * 25

mistura_lata = int(litros / 18.0)
mistura_galao = int((litros - (mistura_lata * 18)) / 3.6)

if litros - (mistura_lata * 18) % 3.6 != 0:
    mistura_galao += 1

print(f"Comprar apenas latas de 18 litros: {latas}, preço: {preco1:.2f}")
print(f"Comprar apenas galões de 3.6 litros: {galoes}, preço: {preco2:.2f}")
print(f"Comprar latas: {mistura_lata} e galoes: {mistura_galao}, preço: ", (mistura_lata * 80) + (mistura_galao * 25))
# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

# Ainda resolvendo.
pro1 = float(input("Digite o valor do primeiro produto: "))
pro2 = float(input("Digite o valor do segundo produto: "))
pro3 = float(input("Digite o valor do terceiro produto: "))

if pro1 <= pro2 and pro1 <= pro3:
    menor = pro1
    p = "primeiro"
elif pro2 <= pro1 and pro2 <= pro3:
    menor = pro2
    p = "segundo"
else:
    menor = pro3
    p = "terceiro"

print(f"Você deve comprar o {p} produto, pois seu valor é R${menor}, o mais barato dos produtos.")
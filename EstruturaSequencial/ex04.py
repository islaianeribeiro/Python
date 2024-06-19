#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

notaf = 0
for c in range(1, 5):
    nota = float(input(f"Informe a {c}º nota: "))
    notaf += nota

print("A média final é ", notaf / 4)
# Faça um Programa que leia três números e mostre o maior deles.

n1 = int(input("Digite o primeiro valor:"))
n2 = int(input("Digite o segundo valor:"))
n3 = int(input("Digite o terceiro valor:"))
maior = n3
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 >= n2:
    maior = n3
    menor = n1
if n2 < n3 and n2 < n1:
    menor = n2
if n3 <= n2 and n3 < n1:
    menor = n3
print(f"O menor número digitado foi {menor}")
print(f"O maior número digitado foi {maior}")
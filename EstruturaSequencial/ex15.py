#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
#Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, 
#faça um programa que nos dê: a. Salário bruto; b. Quanto pagou ao INSS; c. Quanto pagou ao sindicato; d. O salário líquido; e. Calcule os descontos e o salário líquido.

dinheiro = float(input("Quanto você ganha por hora? "))
horas = float(input("Quantas horas você trabalha no mês? "))

SB = dinheiro * horas
IR = (SB * 11) / 100
INSS = (SB * 8) / 100
SINDI = (SB * 5) / 100
descontos = IR + INSS + SINDI
SL = SB - descontos

print(f"Seu salário bruto é de R$ {SB:.2f}")
print(f"Seu imposto de renda é de R$ {IR:.2f}")
print(f"Você pagou ao INSS R$ {INSS:.2f}")
print(f"Você pagou ao Sindicato R$ {SINDI:.2f}")
print(f"Seu salário referido no mês já com os descontos é de R$ {SL:.2f}")
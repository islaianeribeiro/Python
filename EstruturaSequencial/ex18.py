#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho = float(input("Qual o tamanho do arquivo? "))
velocidade = float(input("Qual a velocidade de um link de internet em Mbps? "))
tempo = (tamanho / velocidade) * 60

print(f'Tempo aproximado de download: {tempo:.2f} Minutos ' )
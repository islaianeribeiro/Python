# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

pro1 = float(input("Digite o valor do primeiro produto: "))
pro2 = float(input("Digite o valor do segundo produto: "))
pro3 = float(input("Digite o valor do terceiro produto: "))

def menor():
#Se houver apenas um número menor.
    if pro1 < pro2 and pro1 < pro3:
        print('--------------------------------------')
        print(f'O produto 1 é o mais barato.')
        print(f'Seu valor é de R${pro1}')
    elif pro2 < pro1 and pro2 < pro3:
        print('--------------------------------------')
        print(f'O produto 2 é o mais barato.')
        print(f'Seu valor é de R${pro2}')
    elif pro3 < pro1 and pro3 < pro2:
        print('--------------------------------------')
        print(f'O produto 3 é o mais barato.')
        print(f'Seu valor é de R${pro3}')
#Se alguns números forem iguais.
    elif pro1 == pro2 and pro1 < pro3:
        print('--------------------------------------')
        print(f'Os produtos 1 e 2 são os mais baratos.')
        print(f'Seu valor é de R${pro1}')
    elif pro1 == pro3 and pro1 < pro2:
        print('--------------------------------------')
        print(f'Os produtos 1 e 3 são os mais baratos.')
        print(f'Seu valor é de R${pro1}')
    elif pro2 == pro3 and pro2 < pro1:
        print('--------------------------------------')
        print(f'Os produtos 2 e 3 são os mais baratos.')
        print(f'Seu valor é de R${pro2}')
#Se todos os números forem iguais.
    else:
        print('--------------------------------------')
        print(f'Todos os preços são iguais, então não há menor valor.')
        print(f'O valor é de R${pro1}')


menor()
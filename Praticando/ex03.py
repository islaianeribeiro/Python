peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / altura ** 2
print(f"Seu imc: {imc:.2f}")

if imc < 17:
    print("Muito abaixo do peso")
elif imc >= 17 and imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print("Peso ideal") 
elif imc >= 25 and imc < 30:
    print("Acima do peso")
elif imc >= 30 and imc < 35:
    print("Obesidade grau I")
elif imc >= 35 and imc < 40:
    print("Obesidade grau II") 
else:
    print("Obesidade grau III")



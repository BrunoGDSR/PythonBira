numerador = int(input("Digite o numerador: "))
denominador = int(input("Digite o denominador: "))

if denominador==0:
    print("Erro: o denominador não pode ser 0!")
else:
    resultado = numerador//denominador
    print(f"A divisão inteira de {numerador} por {denominador} é: {resultado}")

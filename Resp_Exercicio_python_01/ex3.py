#At3-------------------------------------------------------------

print("\n=== CALCULADORA ===")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("====================\n")

opcao = input("Escolha uma operação (1/2/3/4): ")

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if opcao == "1":
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado}")
    
elif opcao == "2":
    resultado = num1 - num2
    print(f"{num1} - {num2} = {resultado}")
    
elif opcao == "3":
    resultado = num1 * num2
    print(f"{num1} * {num2} = {resultado}")
    
elif opcao == "4":
    if num2 != 0:
        resultado = num1 / num2
        print(f"{num1} / {num2} = {resultado}")
    else:
        print("Erro: Não é possível dividir por zero!")
        
else:
    print("Opção inválida! Digite 1, 2, 3 ou 4.")
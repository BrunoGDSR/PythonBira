num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
operador = input('Digite o operador (+, -, *, /): ')
potencia = float(input('Digite a potência: '))

if operador == '+':
    resultado = num1 + num2
elif operador == '-':
    resultado = num1 - num2
elif operador == '*':
    resultado = num1 * num2
elif operador == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        print('Erro: Divisão por zero!')
        resultado = None
else:
    print('Operador inválido!')
    resultado = None

if resultado is not None:
    resultado_final = resultado ** potencia
    print(f'({num1} {operador} {num2})^{potencia} = {resultado_final}')

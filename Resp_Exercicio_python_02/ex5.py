refrigerante = float(input("Preço do refrigerante: "))
cerveja = float(input("Preço da cerveja: "))
agua = float(input("Preço da água: "))

menor_preco = min(refrigerante, cerveja, agua)

if menor_preco == refrigerante:
    print("O produto mais barato é o refrigerante.")
elif menor_preco == cerveja:
    print("O produto mais barato é a cerveja.")
else:
    print("O produto mais barato é a água.")
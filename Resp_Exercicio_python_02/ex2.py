total_2023 = float(input("Digite o total de vendas de 2023: "))
total_2024 = float(input("Digite o total de vendas de 2024: "))

percentual = ((total_2024 - total_2023) / total_2023) * 100

if percentual > 0:
    print("Houve crescimento de", percentual, "%")
elif percentual < 0:
    print("Houve decrescimento de", percentual, "%")
else:
    print("Não houve crescimento.")
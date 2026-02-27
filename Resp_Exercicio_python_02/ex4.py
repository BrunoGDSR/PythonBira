preco_2022 = float(input("Preço em 2022: "))
preco_2023 = float(input("Preço em 2023: "))
preco_2024 = float(input("Preço em 2024: "))

maior = max(preco_2022, preco_2023, preco_2024)
menor = min(preco_2022, preco_2023, preco_2024)

print("Maior preço:", maior)
print("Menor preço:", menor)
# Solicita a quantidade de maçãs compradas
quantidade = int(input("Quantas maçãs você deseja comprar? "))

# Define os preços
preco_unitario = 1.30 if quantidade < 12 else 1.00

# Calcula o custo total
custo_total = quantidade * preco_unitario

# Exibe o resultado
print(f"Total a pagar: R$ {custo_total:.2f}")

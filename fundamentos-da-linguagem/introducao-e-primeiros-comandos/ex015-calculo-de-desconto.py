"""
Cálculo de Desconto

Objetivo:
Ler o preço de um produto e aplicar um percentual de desconto definido pelo usuário.
"""

# Entrada de dados
preco = float(input("Qual é o preço do produto? R$ "))
percentual = float(input("Qual o percentual de desconto? (%) "))

# Cálculo do desconto
desconto = preco * percentual / 100
preco_final = preco - desconto

# Saída de dados
print("-" * 40)
print("Preço original: R${:.2f}".format(preco))
print("Percentual de desconto: {}%".format(percentual))
print("Valor do desconto: R${:.2f}".format(desconto))
print("Preço final do produto: R${:.2f}".format(preco_final))
print("-" * 40)

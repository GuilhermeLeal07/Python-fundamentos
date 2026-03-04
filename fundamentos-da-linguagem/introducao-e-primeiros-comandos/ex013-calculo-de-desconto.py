"""
Exercício 013 - Desconto Dinâmico (Versão Melhorada)

Objetivo:
Calcular o valor final de um produto com desconto e mostrar quanto foi economizado.
"""

# Entrada de dados
preco = float(input("Preço do produto: R$ "))
percentual = float(input("Percentual de desconto (%): "))

# Processamento
valor_desconto = preco * percentual / 100
preco_final = preco - valor_desconto
percentual_restante = 100 - percentual

# Saída de dados
print("-" * 40)
print("Preço original: R${:.2f}".format(preco))
print("Desconto aplicado: {}%".format(percentual))
print("Você economizou: R${:.2f}".format(valor_desconto))
print("Preço final: R${:.2f}".format(preco_final))
print("O produto agora representa {}% do valor original.".format(percentual_restante))
print("-" * 40)

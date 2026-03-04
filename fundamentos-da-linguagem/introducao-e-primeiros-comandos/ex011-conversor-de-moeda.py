"""
Conversor de Moeda

Objetivo:
Ler quanto dinheiro a pessoa possui em reais e mostrar quantos dólares ela pode comprar.

Cotação considerada:
U$1.00 = R$5.23
"""

# Entrada de dados
reais = float(input("Quanto você tem na carteira? R$ "))

# Cotação fixa
cotacao = 5.23

# Processamento
dolares = reais / cotacao

# Saída de dados
print("-" * 40)
print("Valor em reais: R${:.2f}".format(reais))
print("Cotação do dólar: R${:.2f}".format(cotacao))
print("Você pode comprar: U${:.2f}".format(dolares))
print("-" * 40)

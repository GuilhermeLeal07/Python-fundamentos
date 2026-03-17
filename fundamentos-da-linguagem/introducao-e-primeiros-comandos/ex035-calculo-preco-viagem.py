"""
Cálculo do preço da viagem

Objetivo:
Criar um programa que leia a distância de uma viagem em quilômetros e calcule o preço da passagem.

Regras:
- Até 200 km → R$0.50 por km
- Acima de 200 km → R$0.45 por km

Conceitos praticados:
- entrada de dados
- estruturas condicionais (if / else)
- operações matemáticas
- formatação de valores
"""

# Entrada de dados
# -------------------------------------------------
distancia = float(input("Quantos km tem a sua viagem? "))

print("Você está prestes a começar uma viagem de {} km.".format(distancia))


# -------------------------------------------------
# Cálculo do preço da passagem
# -------------------------------------------------
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

# -------------------------------------------------
# Resultado
# -------------------------------------------------

print("O preço da sua passagem será de R${:.2f}".format(preco))

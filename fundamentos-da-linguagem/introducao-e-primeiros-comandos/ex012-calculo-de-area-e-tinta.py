"""
Cálculo de Área e Tinta

Objetivo:
Ler a largura e a altura de uma parede, calcular sua área e a quantidade de tinta necessária, considerando que 1 litro de tinta cobre 2m².
"""

# Entrada de dados
largura = float(input("Largura da parede (m): "))
altura = float(input("Altura da parede (m): "))

# Processamento
area = largura * altura
tinta_necessaria = area / 2

# Saída de dados
print("-" * 40)
print("Dimensões da parede: {}m x {}m".format(largura, altura))
print("Área da parede: {:.2f} m²".format(area))
print("Quantidade de tinta necessária: {:.2f} L".format(tinta_necessaria))
print("-" * 40)

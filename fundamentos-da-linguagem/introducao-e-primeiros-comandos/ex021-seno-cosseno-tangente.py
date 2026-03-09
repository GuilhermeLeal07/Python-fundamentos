"""
Seno, Cosseno e Tangente

Objetivo:
Ler um ângulo qualquer e mostrar o valor do seno, cosseno e tangente utilizando a biblioteca math.
"""

import math

# Entrada de dados
angulo = float(input("Digite o ângulo em graus: "))

# Conversão para radianos
rad = math.radians(angulo)

# Cálculos
seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)

# Saída de dados
print("-" * 40)
print("Ângulo: {} graus".format(angulo))
print("Seno: {:.2f}".format(seno))
print("Cosseno: {:.2f}".format(cosseno))
print("Tangente: {:.2f}".format(tangente))
print("-" * 40)

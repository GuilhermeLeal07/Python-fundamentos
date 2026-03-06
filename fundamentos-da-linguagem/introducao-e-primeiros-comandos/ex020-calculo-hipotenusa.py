"""
Cálculo da Hipotenusa

Objetivo:
Ler o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo e calcular o comprimento da hipotenusa.

O cálculo pode ser feito de duas formas:
MÉTODO 1 - Usando a fórmula matemática diretamente
MÉTODO 2 - Utilizando a biblioteca math do Python
"""

# -=-=-=-=-=-=-=-=-=-=-=-=-=-
# MÉTODO 1 - Fórmula manual
# -=-=-=-=-=-=-=-=-=-=-=-=-=-

co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))

hip = (co ** 2 + ca ** 2) ** (1/2)

print("-" * 40)
print("Resultado usando cálculo manual")
print("A hipotenusa mede {:.2f}".format(hip))
print("-" * 40)


# -=-=-=-=-=-=-=-=-=-=-=-=-=-
# MÉTODO 2 - Usando math
# -=-=-=-=-=-=-=-=-=-=-=-=-=-

import math

co = float(input("\nComprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))

hip = math.hypot(co, ca)

print("-" * 40)
print("Resultado usando a biblioteca math")
print("A hipotenusa mede {:.2f}".format(hip))
print("-" * 40)

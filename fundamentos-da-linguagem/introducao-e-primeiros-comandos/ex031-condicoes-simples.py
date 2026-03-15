"""
Condições simples (if / else)

Objetivo:
Exemplo básico de uso de estruturas condicionais em Python. O programa verifica a idade de um carro e informa se ele é novo ou velho.
"""

# Entrada de dados
tempo = int(input("Quantos anos tem seu carro? "))

# Estrutura condicional
if tempo <= 3:
    print("Seu carro é novo")
else:
    print("Seu carro é velho")

print("-- FIM --")

"""
Versão simplificada usando operador condicional:
"""

tempo = int(input("\nQuantos anos tem seu carro? "))

print("Carro novo" if tempo <= 3 else "Carro velho")
print("-- FIM --")

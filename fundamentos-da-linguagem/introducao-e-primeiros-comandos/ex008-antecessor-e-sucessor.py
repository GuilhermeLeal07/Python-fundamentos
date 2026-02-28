"""
Objetivo:
Ler um número inteiro e mostrar seu antecessor e sucessor.
"""

# Entrada de dados
n = int(input("Escolha um número inteiro: "))

# a - antecessor
a = n - 1

# s - sucessor
s = n + 1

print("-" * 40)

print('Analisando o valor {}, seu antecessor vale {} e seu sucessor vale {}'.format(n, a, s))

print("-" * 40)

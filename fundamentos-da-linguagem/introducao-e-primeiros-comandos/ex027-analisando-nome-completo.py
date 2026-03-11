"""
Primeiro e último nome de uma pessoa

Objetivo:
Ler o nome completo de uma pessoa e mostrar separadamente o primeiro e o último nome.
"""

# Entrada de dados
nome = input("Digite seu nome completo: ").strip()

# Separação do nome em lista
partes_nome = nome.split()

# Primeiro e último nome
primeiro_nome = partes_nome[0]
ultimo_nome = partes_nome[-1]

# Saída de dados
print("-" * 40)
print("PRAZER EM TE CONHECER")
print("Seu primeiro nome é {}".format(primeiro_nome))
print("Seu último nome é {}".format(ultimo_nome))
print("-" * 40)

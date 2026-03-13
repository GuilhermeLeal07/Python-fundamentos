"""
Primeiro e último nome de uma pessoa

Objetivo:
Ler o nome completo de uma pessoa e mostrar o primeiro e o último nome separadamente.
"""

# Entrada de dados
nome_completo = input("Digite seu nome completo: ").strip()

# Separação do nome
partes_nome = nome_completo.split()

# Primeiro e último nome
primeiro_nome = partes_nome[0]
ultimo_nome = partes_nome[-1]

# Saída de dados
print("-" * 40)
print("Muito prazer em te conhecer!")
print("Seu primeiro nome é {}".format(primeiro_nome))
print("Seu último nome é {}".format(ultimo_nome))
print("-" * 40)

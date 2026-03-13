"""
Verificando se o nome possui "Silva"

Objetivo:
Ler o nome completo de uma pessoa e verificar se ele contém a palavra "Silva".
"""

# Entrada de dados
nome = input("Digite seu nome completo: ").strip()

# Verificação
tem_silva = "SILVA" in nome.upper()

# Saída de dados
print("-" * 40)
print("Seu nome tem 'Silva'? {}".format(tem_silva))
print("-" * 40)

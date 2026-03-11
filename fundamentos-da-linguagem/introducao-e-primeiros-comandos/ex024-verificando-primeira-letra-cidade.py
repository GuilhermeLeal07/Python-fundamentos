"""
Verificando as primeiras letras de um texto

Objetivo:
Ler o nome de uma cidade e verificar se ela começa com a palavra "SANTO".
"""

# Entrada de dados
cidade = input("Digite o nome de uma cidade: ").strip()

# Verificação
resultado = cidade[:5].upper() == "SANTO"

# Saída de dados
print("-" * 40)
print("A cidade começa com 'SANTO'? {}".format(resultado))
print("-" * 40)

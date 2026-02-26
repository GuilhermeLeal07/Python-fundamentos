"""
-- Análise de tipos primitivos

Objetivo:
Ler um valor digitado pelo usuário e exibir informações sobre seu tipo e suas características.
"""

valor = input("Digite algo: ")

print("O tipo primitivo desse valor é {}".format(type(valor)))

# Verifica se a string contém apenas espaços em branco
print("Só tem espaços? {}".format(valor.isspace()))

# Verifica se a string contém apenas caracteres numéricos
print("É um número? {}".format(valor.isnumeric()))

# Verifica se contém apenas letras (sem números ou símbolos)
print("É alfabético? {}".format(valor.isalpha()))

# Verifica se contém letras ou números
print("É alfanumérico? {}".format(valor.isalnum()))

# Verifica se todas as letras estão em maiúsculo
print("Está em maiúsculas? {}".format(valor.isupper()))

# Verifica se todas as letras estão em minúsculo
print("Está em minúsculas? {}".format(valor.islower()))

# Verifica se está capitalizada (primeira letra maiúscula)
print("Está capitalizada? {}".format(valor.istitle()))

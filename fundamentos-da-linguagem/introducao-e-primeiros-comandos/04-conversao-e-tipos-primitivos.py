"""
Prática sobre conversão de tipos e tipos primitivos em Python.

Objetivo:
Entender por que o input() retorna uma string
e como converter corretamente para tipos numéricos.
"""
""" 
==============================
Tipos Primitivos em Python
==============================

int: 7, -4, 0, 1234
float: 4.5, 0.0987, -7.2468, 7.0
bool: True, False
str: "Olá", "7.23", ""

==============================
Conversão de string para inteiro
==============================

O input() sempre retorna uma string.
Para realizar operações matemáticas, precisamos converter para int ou float.
"""

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

soma = n1 + n2

print("A soma vale", soma)

"""
==============================
Outra forma de exibir o resultado
==============================
"""

print("A soma vale {}".format(soma))

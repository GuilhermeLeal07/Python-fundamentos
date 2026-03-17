"""
Par ou Ímpar

Objetivo:
Criar um programa que leia um número inteiro
e mostre se ele é PAR ou ÍMPAR.

Conceitos praticados:
- entrada de dados
- operador módulo (%)
- estruturas condicionais (if / else)
"""

"""
Entrada de dados
-------------------------------------------------
"""

numero = int(input("Digite um número inteiro: "))

"""
Verificação usando o operador módulo
-------------------------------------------------
"""
resultado = numero % 2

"""
O operador % retorna o RESTO da divisão.

Exemplo:
10 % 2 = 0  → número PAR
11 % 2 = 1  → número ÍMPAR
-------------------------------------------------
Estrutura condicional
-------------------------------------------------
"""
if resultado == 0:
    print("O número {} é PAR.".format(numero))
else:
    print("O número {} é ÍMPAR.".format(numero))

"""
Arredondamento Matemático

Objetivo:
Ler um número real e mostrar diferentes formas de arredondamento utilizando funções da biblioteca math.

Lembrando:
math.trunc() --> remove a parte decimal
math.floor() --> arredonda para baixo
math.ceil() --> arredonda para cima

Exemplo:
  Número: 6.8
    trunc -> 6
    floor -> 6
    ceil -> 7
"""

import math

# Entrada de dados
num = float(input("Digite um número real: "))

# Processamento
parte_inteira = math.trunc(num)
arredondar_para_baixo = math.floor(num)
arredondar_para_cima = math.ceil(num)

# Saída de dados
print("-" * 40)
print("Número digitado: {}".format(num))
print("Parte inteira (trunc): {}".format(parte_inteira))
print("Arredondado para baixo (floor): {}".format(arredondar_para_baixo))
print("Arredondado para cima (ceil): {}".format(arredondar_para_cima))
print("-" * 40)

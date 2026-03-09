"""
Ordem de apresentação dos alunos

Objetivo:
Ler o nome de quatro alunos e sortear a ordem de apresentação dos trabalhos.

Explicação:
Utiliza a biblioteca random para embaralhar os nomes dos alunos e gerar uma ordem aleatória de apresentação.

A biblioteca random permite gerar valores aleatórios, como:
- sortear números
- escolher itens de listas
- embaralhar listas

Neste exemplo utilizarei:
random.shuffle(lista)

Essa função embaralha os elementos de uma lista, alterando a ordem original dos itens.
"""

import random

# Entrada de dados
n1 = input("Nome do primeiro aluno: ")
n2 = input("Nome do segundo aluno: ")
n3 = input("Nome do terceiro aluno: ")
n4 = input("Nome do quarto aluno: ")

# Lista de alunos
lista = [n1, n2, n3, n4]

# Para embaralhar a ordem usamos o random.shuffler
random.shuffle(lista)

# Saída de dados
print("-" * 40)
print("Ordem de apresentação:")
print(lista)
print("-" * 40)

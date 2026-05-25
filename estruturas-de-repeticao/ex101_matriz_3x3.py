"""
Ex101 - Criando e exibindo uma matriz 3x3

Neste exercício, utilizamos listas compostas para criar uma matriz 3x3 preenchida com valores digitados pelo usuário.

O programa realiza:

- Criação de matriz
- Leitura de valores
- Armazenamento organizado em linhas e colunas
- Exibição formatada da matriz

Conceitos trabalhados:

- Matrizes
- Listas compostas
- Estrutura for aninhada
- Índices de linha e coluna
- Formatação de saída

O objetivo é desenvolver lógica de manipulação de estruturas bidimensionais.
"""

# Criação da matriz 3x3
matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Entrada de dados
for linha in range(0, 3):

    for coluna in range(0, 3):

        matriz[linha][coluna] = int(
            input(f'Digite um valor para [{linha}, {coluna}]: ')
        )

# Saída
print('-=-' * 30)

for linha in range(0, 3):

    for coluna in range(0, 3):

        print(f'[{matriz[linha][coluna]:^5}]', end='')

    print()

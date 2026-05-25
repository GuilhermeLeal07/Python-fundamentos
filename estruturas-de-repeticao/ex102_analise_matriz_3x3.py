"""
Ex102 - Analisando dados em uma matriz 3x3

Neste exercício, utilizamos matrizes para armazenar valores numéricos e realizar análises específicas.

O programa realiza:

- Criação de matriz 3x3
- Soma dos valores pares
- Soma da terceira coluna
- Identificação do maior valor da segunda linha
- Exibição formatada da matriz

Conceitos trabalhados:

- Matrizes
- Listas compostas
- Estrutura for aninhada
- Operador módulo (%)
- Comparação de valores
- Manipulação de índices

O objetivo é desenvolver lógica de análise e manipulação de estruturas bidimensionais.
"""

# Criação da matriz
matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Variáveis de controle
soma_pares = 0
soma_terceira_coluna = 0
maior_segunda_linha = 0

# Entrada de dados
for linha in range(0, 3):

    for coluna in range(0, 3):

        matriz[linha][coluna] = int(
            input(f'Digite um valor para [{linha}, {coluna}]: ')
        )

# Exibição da matriz
print('-=-' * 30)

for linha in range(0, 3):

    for coluna in range(0, 3):

        print(f'[{matriz[linha][coluna]:^5}]', end='')

        # Soma dos valores pares
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]

    print()

print('-=-' * 30)

# Soma da terceira coluna
for linha in range(0, 3):

    soma_terceira_coluna += matriz[linha][2]

# Maior valor da segunda linha
for coluna in range(0, 3):

    if coluna == 0:

        maior_segunda_linha = matriz[1][coluna]

    elif matriz[1][coluna] > maior_segunda_linha:

        maior_segunda_linha = matriz[1][coluna]

# Saída
print(f'A soma dos valores pares é {soma_pares}.')

print(
    f'A soma dos valores da terceira coluna é '
    f'{soma_terceira_coluna}.'
)

print(
    f'O maior valor da segunda linha é '
    f'{maior_segunda_linha}.'
)

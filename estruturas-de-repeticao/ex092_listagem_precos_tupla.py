"""
Ex092 - Listagem de preços utilizando tuplas

Neste exercício, utilizamos uma tupla para armazenar produtos e seus respectivos preços.

O programa realiza:

- Exibição organizada de produtos
- Formatação tabular de preços
- Percorrimento de tuplas com range()
- Alinhamento de texto e valores monetários

Conceitos trabalhados:

- Tuplas
- Estrutura for
- range()
- len()
- Formatação de strings
- Operador módulo (%)

O objetivo é desenvolver organização visual e manipulação estruturada de dados.
"""

# Tupla com produtos e preços
listagem = (
    'Lápis', 1.75,
    'Borracha', 2.00,
    'Caderno', 15.90,
    'Estojo', 25.00,
    'Transferidor', 4.20,
    'Compasso', 9.99,
    'Mochila', 120.32,
    'Canetas', 22.30,
    'Livros', 34.90
)

# Saída
print('--' * 20)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('--' * 20)

# Percorre toda a tupla
for posicao in range(0, len(listagem)):

    # Produtos
    if posicao % 2 == 0:
        print(f'{listagem[posicao]:.<30}', end='')

    # Preços
    else:
        print(f'R${listagem[posicao]:>7.2f}')

print('--' * 20)

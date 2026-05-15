"""
Ex090 - Números aleatórios utilizando tuplas

Neste exercício, utilizamos a biblioteca random para gerar números aleatórios armazenados em uma tupla.

O programa realiza:

- Sorteio de números aleatórios
- Armazenamento em tupla
- Exibição dos valores sorteados
- Identificação do maior e menor valor

Conceitos trabalhados:

- Tuplas
- Biblioteca random
- Função randint()
- Estrutura for
- Funções max() e min()

O objetivo é desenvolver lógica de manipulação e análise de dados gerados automaticamente.
"""

# Importação
from random import randint

# Tupla com números aleatórios
numeros = (
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
    randint(1, 10)
)

# Saída
print('Os valores sorteados foram: ', end='')

for numero in numeros:
    print(f'{numero} ', end='')

print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')

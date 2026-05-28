"""
Ex106 - Ranking de jogadores com lançamento de dado

Neste exercício, utilizamos dicionários para armazenar os resultados de jogadores em um sorteio de dados.

O programa realiza:

- Sorteio de números aleatórios
- Armazenamento em dicionário
- Exibição dos resultados
- Ordenação do ranking
- Definição do vencedor

Conceitos trabalhados:

- Dicionários
- Biblioteca random
- Biblioteca operator
- sorted()
- itemgetter()
- enumerate()

O objetivo é desenvolver lógica de organização, ordenação e classificação de dados.
"""

# Importação
from random import randint
from time import sleep
from operator import itemgetter

# Dicionário com os resultados
jogo = {
    'Jogador 1': randint(1, 6),
    'Jogador 2': randint(1, 6),
    'Jogador 3': randint(1, 6),
    'Jogador 4': randint(1, 6)
}

# Lista do ranking
ranking = []

# Exibição dos resultados
print('Valores sorteados:')

for jogador, valor in jogo.items():

    print(f'{jogador} tirou {valor} no dado.')

    sleep(1)

# Ordenação do ranking
ranking = sorted(
    jogo.items(),
    key=itemgetter(1),
    reverse=True
)

# Exibição do ranking
print('-=-' * 30)

print('== RANKING DOS JOGADORES ==')

for indice, jogador in enumerate(ranking):

    print(
        f'{indice + 1}º lugar: '
        f'{jogador[0]} com {jogador[1]}'
    )

    sleep(1)

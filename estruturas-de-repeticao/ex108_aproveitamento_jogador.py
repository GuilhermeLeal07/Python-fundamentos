"""
Ex108 - Aproveitamento de jogador de futebol

Neste exercício, utilizamos dicionários e listas para armazenar informações sobre o desempenho de um jogador.

O programa realiza:

- Cadastro do nome do jogador
- Registro de partidas jogadas
- Armazenamento de gols por partida
- Cálculo do total de gols
- Exibição organizada dos dados

Conceitos trabalhados:

- Dicionários
- Listas
- Método append()
- Função sum()
- enumerate()
- Manipulação de estruturas compostas

O objetivo é desenvolver lógica de cadastro e análise de desempenho esportivo.
"""

# Dicionário do jogador
jogador = {}

# Lista de gols por partida
partidas = []

# Entrada de dados
jogador['nome'] = input(
    'Nome do jogador: '
).strip()

total_partidas = int(
    input(
        f'Quantas partidas '
        f'{jogador["nome"]} jogou? '
    )
)

# Cadastro dos gols
for contador in range(0, total_partidas):

    gols = int(
        input(
            f'Quantos gols na partida '
            f'{contador + 1}? '
        )
    )

    partidas.append(gols)

# Armazena dados no dicionário
jogador['gols'] = partidas[:]

# Soma total dos gols
jogador['total'] = sum(partidas)

# Saída
print('==' * 30)

print(f'Nome: {jogador["nome"]}')

print(
    f'Partidas jogadas: '
    f'{len(jogador["gols"])}'
)

print(f'Total de gols: {jogador["total"]}')

print('==' * 30)

# Detalhamento das partidas
for indice, gols in enumerate(jogador['gols']):

    print(
        f'Na partida {indice + 1}, '
        f'fez {gols} gol(s).'
    )

print('==' * 30)

"""
Ex110 - Aproveitamento detalhado de um jogador

Neste exercício, utilizamos dicionários e listas para armazenar e exibir o desempenho completo de um jogador de futebol.

O programa realiza:

- Cadastro do nome do jogador
- Registro dos gols em cada partida
- Cálculo do total de gols
- Exibição do dicionário completo
- Relatório detalhado por partida

Conceitos trabalhados:

- Dicionários
- Listas
- append()
- sum()
- items()
- enumerate()
- Estruturas compostas

O objetivo é desenvolver lógica de armazenamento, organização e consulta de dados esportivos.
"""

# Dicionário principal
jogador = {}

# Lista de gols
gols = []

# Entrada de dados
jogador['nome'] = input('Nome do jogador: ').strip()

partidas = int(
    input(f'Quantas partidas {jogador["nome"]} jogou? ')
)

# Cadastro dos gols
for contador in range(partidas):

    gols.append(
        int( input(f'Quantos gols na partida {contador + 1}? ')))

# Armazenamento dos dados
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)

# Exibição do dicionário
print('-=' * 30)

print(jogador)

print('-=' * 30)

# Exibição das chaves
for chave, valor in jogador.items():

    print(f'O campo {chave} tem o valor {valor}')

print('-=' * 30)

# Resumo do desempenho
print(
    f'O jogador {jogador["nome"]} jogou '
    f'{len(jogador["gols"])} partidas.'
)

# Relatório das partidas
for indice, gols in enumerate(jogador['gols']):

    print(
        f' => Na partida {indice + 1}, '
        f'fez {gols} gol(s).'
    )

print(
    f'Foi um total de '
    f'{jogador["total"]} gol(s).'
)

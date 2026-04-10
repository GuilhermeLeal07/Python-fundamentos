"""
Exercício 054 - Jokenpô

Este programa simula o jogo Pedra, Papel e Tesoura
entre o jogador e o computador.
"""

# ===============================
# Importações
# ===============================

from random import randint
from time import sleep

# ===============================
# Dados do jogo
# ===============================

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

# ===============================
# Entrada do jogador
# ===============================

print('Suas opções:')
print('[0] PEDRA')
print('[1] PAPEL')
print('[2] TESOURA')

jogador = int(input('Qual é a sua jogada? '))

print('-' * 40)

# ===============================
# Animação
# ===============================

print('JO')
sleep(.5)
print('KEN')
sleep(.5)
print('PO!!!')
sleep(.5)

print('-' * 40)

# ===============================
# Resultado
# ===============================

if jogador not in [0, 1, 2]:
    print('Jogada inválida!')

else:
    print(f'Computador jogou: {itens[computador]}')
    print(f'Jogador jogou: {itens[jogador]}')

    print('-' * 40)

    if computador == jogador:
        print('EMPATE!')

    elif (jogador == 0 and computador == 2) or \
         (jogador == 1 and computador == 0) or \
         (jogador == 2 and computador == 1):
        print('JOGADOR VENCE!')

    else:
        print('COMPUTADOR VENCE!')

print('-' * 40)

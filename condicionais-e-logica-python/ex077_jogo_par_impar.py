"""
Exercício 077 - Jogo Par ou Ímpar

Este programa simula um jogo de Par ou Ímpar contra o computador.
O jogo continua até o jogador perder.
Ao final, mostra o total de vitórias consecutivas.
"""

# ===============================
# Importação
# ===============================

from random import randint

# ===============================
# Inicialização
# ===============================

vitorias = 0

# ===============================
# Loop do jogo
# ===============================

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador

    tipo = ''
    while tipo not in ['P', 'I']:
        tipo = input('Par ou Ímpar? [P/I] ').strip().upper()[0]

    print('-' * 40)
    print(f'Você jogou {jogador} e o computador {computador}.')
    print(f'Total: {total} → {"PAR" if total % 2 == 0 else "ÍMPAR"}')

    # ===========================
    # Verificação de vitória
    # ===========================

    ganhou = (total % 2 == 0 and tipo == 'P') or (total % 2 == 1 and tipo == 'I')

    if ganhou:
        print('Você GANHOU!')
        vitorias += 1
    else:
        print('Você PERDEU!')
        break

    print('-' * 40)
    print('Vamos jogar novamente...')

# ===============================
# Resultado final
# ===============================

print('-' * 40)
print(f'GAME OVER! Você venceu {vitorias} vezes consecutivas.')
print('-' * 40)

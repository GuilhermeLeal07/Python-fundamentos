"""
Exercício 067 - Jogo de Adivinhação

O computador pensa em um número entre 0 e 10.
O jogador deve tentar adivinhar até acertar.
No final, o programa informa o número de tentativas.
"""

# ===============================
# Importação
# ===============================

from random import randint

# ===============================
# Configuração do jogo
# ===============================

computador = randint(0, 10)
palpites = 0
acertou = False

print('Sou o seu computador...')
print('Pensei em um número entre 0 e 10.')
print('Tente adivinhar!')

print('-' * 40)

# ===============================
# Loop do jogo
# ===============================

while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1

    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente novamente.')
        else:
            print('Menos... tente novamente.')

# ===============================
# Resultado
# ===============================

print('-' * 40)
print(f'Parabéns! Você acertou em {palpites} tentativas.')
print('-' * 40)

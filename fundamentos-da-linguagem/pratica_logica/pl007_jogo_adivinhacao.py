"""
Jogo de Adivinhação

O sistema gera um número aleatório entre 1 e 10.
O jogador tenta adivinhar e recebe dicas para melhorar sua tentativa.
"""

# ======================
# IMPORTAÇÃO
# ======================
import random

# ======================
# PROCESSAMENTO
# ======================
numero_secreto = random.randint(1, 10)

# ======================
# ENTRADA
# ======================
print('JOGO DE ADIVINHAÇÃO')
print('Tente adivinhar o número entre 1 e 10!\n')

palpite = int(input('Digite seu palpite: '))

# ======================
# VALIDAÇÃO
# ======================
if palpite < 1 or palpite > 10:
    status = 'Inválido'
else:
    status = 'Válido'

# ======================
# SAÍDA
# ======================
print('\n===== RESULTADO =====')

if status == 'Inválido':
    print('Número inválido!!! Digite um valor entre 1 e 10.')

else:
    print(f'Seu palpite: {palpite}')
    print(f'Número secreto: {numero_secreto}')

    if palpite == numero_secreto:
        print('PARABÉNS!!! Você acertou em cheio!!!')
    else:
        print('Você errou! Mas foi uma boa tentativa.')

        # dica
        if palpite > numero_secreto:
            print('Dica: o número secreto é MENOR que o seu palpite.')
        else:
            print('Dica: o número secreto é MAIOR que o seu palpite.')

"""
Exercício 076 - Tabuada Interativa

Este programa mostra a tabuada de vários números.
O usuário pode solicitar quantas tabuadas quiser.
A execução só é encerrada quando um número negativo for digitado.
"""

# ===============================
# Loop principal
# ===============================

while True:
    numero = int(input('Quer ver a tabuada de qual valor? '))

    if numero < 0:
        print('Encerrando o programa...')
        break

    print('-' * 40)
    print(f'Tabuada do {numero}')
    print('-' * 40)

    # ===========================
    # Geração da tabuada
    # ===========================

    for contador in range(1, 11):
        print(f'{numero} x {contador:2} = {numero * contador}')

    print('-' * 40)

# ===============================
# Saída final
# ===============================

print('PROGRAMA TABUADA ENCERRADO. VOLTE SEMPRE!')

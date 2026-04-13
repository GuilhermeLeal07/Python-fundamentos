"""
Exercício 055 - Contagem Regressiva

Este programa realiza uma contagem regressiva de 10 até 0, com pausa de 1 segundo entre cada número.
Ao final, exibe uma mensagem comemorativa.
"""

from time import sleep

# ===============================
# Contagem regressiva
# ===============================

print('Contagem regressiva para o Ano Novo...')
print('-' * 40)

for numero in range(10, 0, -1):
    print(numero)
    sleep(1)

print('-' * 40)
print('FELIZ ANO NOVO!!!')
print('-' * 40)

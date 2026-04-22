"""
Exercício 072 - Sequência de Fibonacci

Este programa lê um número inteiro N e mostra os N primeiros termos da sequência de Fibonacci.
"""

# ===============================
# Entrada de dados
# ===============================

quantidade = int(input('Quantos termos você quer mostrar? '))

# ===============================
# Processamento e saída
# ===============================

print('-' * 40)
print('Sequência de Fibonacci:')

termo1 = 0
termo2 = 1

# Casos iniciais
if quantidade == 1:
    print(f'{termo1} -> FIM')

elif quantidade >= 2:
    print(f'{termo1} -> {termo2}', end='')

    contador = 3
    while contador <= quantidade:
        proximo = termo1 + termo2
        print(f' -> {proximo}', end='')
        termo1 = termo2
        termo2 = proximo
        contador += 1

    print(' -> FIM')

print('-' * 40)

"""
Exercício 059 - Soma de Números Pares

Este programa lê seis números inteiros e calcula a soma apenas dos valores pares.
"""

# ===============================
# Processamento
# ===============================

soma = 0
contador = 0

for indice in range(1, 7):
    numero = int(input(f'Digite o {indice}º valor: '))

    if numero % 2 == 0:
        soma += numero
        contador += 1

# ===============================
# Saída
# ===============================

print('-' * 40)
print(f'Quantidade de números pares: {contador}')
print(f'Soma dos valores pares: {soma}')
print('-' * 40)

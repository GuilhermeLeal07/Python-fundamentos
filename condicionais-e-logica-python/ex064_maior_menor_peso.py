"""
Exercício 064 - Maior e Menor Peso

Este programa lê o peso de cinco pessoas e informa o maior e o menor peso registrados.
"""

# ===============================
# Processamento
# ===============================

maior_peso = 0
menor_peso = 0

for pessoa in range(1, 6):
    peso = float(input(f'Peso da {pessoa}ª pessoa (kg): '))

    if pessoa == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso

# ===============================
# Saída
# ===============================

print('-' * 40)
print(f'O maior peso registrado foi: {maior_peso:.1f} kg')
print(f'O menor peso registrado foi: {menor_peso:.1f} kg')
print('-' * 40)

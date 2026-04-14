"""
Exercício 057 - Soma de Ímpares Múltiplos de 3

Este programa calcula a soma de todos os números ímpares que são múltiplos de 3 no intervalo de 1 até 500.
"""

# ===============================
# Processamento
# ===============================

soma = 0
contador = 0

for numero in range(1, 501, 2):  # percorre apenas ímpares
    if numero % 3 == 0:
        contador += 1
        soma += numero

# ===============================
# Saída
# ===============================

print('-' * 40)
print(f'Quantidade de valores encontrados: {contador}')
print(f'Soma total: {soma}')
print('-' * 40)

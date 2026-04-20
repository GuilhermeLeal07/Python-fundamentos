"""
Exercício 069 - Cálculo de Fatorial

Este programa calcula o fatorial de um número:
- Utilizando função pronta (math.factorial)
- Utilizando cálculo manual com laço while
"""

# ===============================
# Importação
# ===============================

from math import factorial

# ===============================
# Entrada de dados
# ===============================

numero = int(input('Digite um número para calcular o fatorial: '))

# ===============================
# Método 1 - Função pronta
# ===============================

resultado_funcao = factorial(numero)

print('-' * 40)
print(f'Usando função pronta:')
print(f'{numero}! = {resultado_funcao}')
print('-' * 40)

# ===============================
# Método 2 - Cálculo manual
# ===============================

contador = numero
fatorial = 1

print('Calculando manualmente:')
print(f'{numero}! = ', end='')

while contador > 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1

print(f'{fatorial}')
print('-' * 40)

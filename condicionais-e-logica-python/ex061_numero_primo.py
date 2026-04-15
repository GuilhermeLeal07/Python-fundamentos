"""
Exercício 061 - Verificador de Número Primo

Este programa verifica se um número é primo e mostra todos os seus divisores.
"""

# ===============================
# Entrada de dados
# ===============================

numero = int(input('Digite um número: '))

# ===============================
# Processamento
# ===============================

total_divisores = 0

print('-' * 40)
print(f'Divisores de {numero}:')

for divisor in range(1, numero + 1):
    if numero % divisor == 0:
        print(divisor, end=' | ')  # mostra o divisor
        total_divisores += 1

# ===============================
# Saída
# ===============================

print('\n' + '-' * 40)
print(f'O número {numero} foi divisível {total_divisores} vezes.')

if total_divisores == 2:
    print('Resultado: É um número PRIMO.')
else:
    print('Resultado: NÃO é um número primo.')

print('-' * 40)

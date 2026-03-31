"""
Este arquivo explora diferentes usos do laço 'for' em Python.

Conteúdos abordados:
- Contagem crescente
- Contagem regressiva
- Uso de passo (step)
- Entrada dinâmica do usuário
- Acumulador (somatório)

------------------------------------------
DESAFIO:
1. Mostre os números de 1 até 10
2. Mostre os números de 10 até 1
3. Mostre apenas números pares de 0 até 20
4. Peça 5 números ao usuário e mostre a soma total
------------------------------------------
"""

# ==========================================
# 1. Contagem crescente -->
# ==========================================

print('Contagem de 1 até 10:')
for c in range(1, 11):
    print(c)
print('-=-' * 15)

# ==========================================
# 2. Contagem regressiva <--
# ==========================================

print('Contagem de 10 até 1:')
for c in range(10, 0, -1):
    print(c)
print('-=-' * 15)

# ==========================================
# 3. Números pares
# ==========================================

print('Números pares de 0 até 20:')
for c in range(0, 21, 2):
    print(c)
print('-=-' * 15)

# =============================================================
# 4. Entrada dinâmica(será contado até chegar o número limite)
# =============================================================

limite = int(input('Digite um número limite: '))

print(f'Contando até {limite}:')
for c in range(0, limite + 1):
    print(c)
print('-=-' * 15)

# ==========================================
# 5. Somatório
# ==========================================

soma = 0

print('Digite 5 números para somar:')
for i in range(1, 6):
    numero = int(input(f'{i}º número: '))
    soma += numero

print(f'Soma total: {soma}')
print('-=-' * 15)

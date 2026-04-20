"""
Exercício 070 - Progressão Aritmética com While

Este programa lê o primeiro termo e a razão de uma PA e mostra os 10 primeiros termos utilizando o laço while.
"""

# ===============================
# Entrada de dados
# ===============================

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

# ===============================
# Processamento
# ===============================

termo = primeiro_termo
contador = 1

# ===============================
# Saída
# ===============================

print('-' * 40)

while contador <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    contador += 1

print('FIM')
print('-' * 40)

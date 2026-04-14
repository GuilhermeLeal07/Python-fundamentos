"""
Exercício 060 - Progressão Aritmética (PA)

Este programa lê o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da sequência.
"""

# ===============================
# Entrada de dados
# ===============================

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

# ===============================
# Processamento
# ===============================

decimo_termo = primeiro_termo + (10 - 1) * razao

# ===============================
# Saída
# ===============================

print('-' * 40)

for termo in range(primeiro_termo, decimo_termo + razao, razao):
    print(termo, end=' -> ')

print('FIM')
print('-' * 40)

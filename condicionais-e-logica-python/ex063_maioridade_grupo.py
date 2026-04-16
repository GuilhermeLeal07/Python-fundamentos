"""
Exercício 063 - Análise de Maioridade

Este programa lê o ano de nascimento de sete pessoas e informa quantas são maiores e quantas são menores de idade.
"""

# ===============================
# Importação
# ===============================

from datetime import date

# ===============================
# Processamento
# ===============================

ano_atual = date.today().year

total_maiores = 0
total_menores = 0

for pessoa in range(1, 8):
    ano_nascimento = int(input(f'Digite o ano de nascimento da {pessoa}ª pessoa: '))
    idade = ano_atual - ano_nascimento

    if idade >= 18:
        total_maiores += 1
    else:
        total_menores += 1

# ===============================
# Saída
# ===============================

print('-' * 40)
print(f'Total de pessoas maiores de idade: {total_maiores}')
print(f'Total de pessoas menores de idade: {total_menores}')
print('-' * 40)

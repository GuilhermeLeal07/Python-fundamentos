"""
Exercício 066 - Validação de Sexo

Este programa lê o sexo de uma pessoa e só aceita os valores 'M' ou 'F'. Caso o valor seja inválido, solicita a entrada novamente.
"""

# ===============================
# Entrada e validação
# ===============================

sexo = input('Informe seu sexo [M/F]: ').strip().upper()[0]

while sexo not in ['M', 'F']:
    sexo = input('Dados inválidos. Informe seu sexo [M/F]: ').strip().upper()[0]

# ===============================
# Saída
# ===============================

print('-' * 40)
print(f'Sexo {sexo} registrado com sucesso.')
print('-' * 40)

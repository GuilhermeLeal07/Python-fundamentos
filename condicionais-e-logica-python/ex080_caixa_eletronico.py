"""
Exercício 080 - Simulador de Caixa Eletrônico

Este programa simula um caixa eletrônico.
O usuário informa um valor e o sistema calcula quantas cédulas de cada valor serão entregues.

Cédulas disponíveis: R$50, R$20, R$10 e R$1
"""

# ===============================
# Entrada
# ===============================

print('=' * 40)
print(f'{"BANCO LEAL":^40}')
print('=' * 40)

valor = int(input('Qual valor você deseja sacar? R$ '))

# ===============================
# Processamento
# ===============================

valor_restante = valor
cedula = 50
total_cedulas = 0

while True:
    if valor_restante >= cedula:
        valor_restante -= cedula
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f'{total_cedulas} cédula(s) de R$ {cedula}')

        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1

        total_cedulas = 0

        if valor_restante == 0:
            break

# ===============================
# Saída
# ===============================

print('=' * 40)
print('Retire seu dinheiro. Volte sempre!')
print('=' * 40)

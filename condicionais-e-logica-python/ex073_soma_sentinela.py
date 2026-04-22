"""
Exercício 073 - Soma com Condição de Parada

Este programa lê vários números inteiros.
A execução só para quando o usuário digitar 999.
No final, mostra a quantidade de números digitados e a soma total (desconsiderando o valor 999).
"""

# ===============================
# Inicialização
# ===============================

numero = 0
contador = 0
soma = 0

# ===============================
# Entrada e processamento
# ===============================

numero = int(input('Digite um número [999 para parar]: '))

while numero != 999:
    soma += numero
    contador += 1
    numero = int(input('Digite um número [999 para parar]: '))

# ===============================
# Saída
# ===============================

print('-' * 40)
print(f'Quantidade de números digitados: {contador}')
print(f'Soma total: {soma}')
print('-' * 40)

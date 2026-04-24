"""
Exercício 075 - Soma com Break

Este programa lê vários números inteiros.
A execução só para quando o usuário digitar 999.
No final, mostra a quantidade de números digitados e a soma total (desconsiderando o valor 999).
"""

# ===============================
# Inicialização
# ===============================

soma = 0
contador = 0

# ===============================
# Entrada e processamento
# ===============================

while True:
    numero = int(input('Digite um número [999 para parar]: '))

    if numero == 999:
        print('Encerrando...')
        break

    soma += numero
    contador += 1

# ===============================
# Saída
# ===============================

print('-' * 40)
print(f'Quantidade de números digitados: {contador}')
print(f'Soma total: {soma}')
print('-' * 40)

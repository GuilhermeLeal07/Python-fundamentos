"""
Exercício 058 - Tabuada Interativa

Este programa permite ao usuário visualizar a tabuada de vários números, até decidir encerrar.
"""

# ===============================
# Sistema de tabuada
# ===============================

while True:
    numero = int(input('Digite um número para ver a tabuada (0 para sair): '))

    if numero == 0:
        print('Encerrando o programa...')
        break

    print('-' * 40)

    for multiplicador in range(1, 11):
        resultado = numero * multiplicador
        print(f'{numero} x {multiplicador} = {resultado}')

    print('-' * 40)

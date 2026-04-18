"""
Exercício 068 - Menu de Operações

Este programa lê dois valores e apresenta um menu com opções de operações matemáticas.
O usuário pode escolher a operação desejada até decidir sair.
"""

# ===============================
# Entrada inicial
# ===============================

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

opcao = 0

# ===============================
# Loop do sistema
# ===============================

while opcao != 5:
    print('\n' + '-' * 40)
    print('''
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    print('-' * 40)

    opcao = int(input('Escolha uma opção: '))

    # ===========================
    # Processamento
    # ===========================

    if opcao == 1:
        resultado = n1 + n2
        print(f'A soma entre {n1} e {n2} é {resultado}')

    elif opcao == 2:
        resultado = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é {resultado}')

    elif opcao == 3:
        if n1 > n2:
            print(f'O maior valor é {n1}')
        elif n2 > n1:
            print(f'O maior valor é {n2}')
        else:
            print('Os dois valores são iguais')

    elif opcao == 4:
        print('Informe os novos valores:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))

    elif opcao == 5:
        print('Finalizando o programa...')

    else:
        print('Opção inválida. Tente novamente.')

# ===============================
# Saída final
# ===============================

print('\nFim do programa! Volte sempre!')

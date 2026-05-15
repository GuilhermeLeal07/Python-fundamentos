"""
Ex088 - Números por extenso utilizando tuplas

Neste exercício, utilizamos uma tupla para armazenar números escritos por extenso de 0 até 20.

O programa solicita um número ao usuário e mostra sua representação textual.

Conceitos trabalhados:

- Tuplas
- Índices
- Estrutura while
- Validação de entrada
- Estruturas de repetição

O objetivo é desenvolver lógica de consulta
e manipulação de dados imutáveis.
"""

# Tupla com números por extenso
cont = (
    'zero', 'um', 'dois', 'três', 'quatro',
    'cinco', 'seis', 'sete', 'oito', 'nove',
    'dez', 'onze', 'doze', 'treze', 'catorze',
    'quinze', 'dezesseis', 'dezessete', 'dezoito',
    'dezenove', 'vinte'
)

# Processamento
while True:

    while True:
        numero = int(input('Digite um número entre 0 e 20: '))

        if 0 <= numero <= 20:
            break

        print('TENTE NOVAMENTE. ', end=' ')

    # Saída
    print(f'Você digitou o número {cont[numero]}.')

    continuar = input('Deseja continuar? [S/N] ').strip().upper()

    if continuar != 'S':
        print('Encerrando programa...')
        break

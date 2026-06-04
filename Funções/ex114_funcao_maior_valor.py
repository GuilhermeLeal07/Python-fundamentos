"""
Ex115 - Função maior()

Neste exercício, criamos uma função capaz de receber uma quantidade variável de números inteiros e identificar o maior valor informado.

O programa realiza:

- Recebimento de vários números
- Contagem dos valores informados
- Identificação do maior número
- Exibição dos resultados

Conceitos trabalhados:

- Funções
- Empacotamento de parâmetros (*args)
- Estrutura for
- Comparação de valores
- Biblioteca time

O objetivo é aprender a criar funções que recebem quantidades variáveis de argumentos.
"""

from time import sleep

def maior(*num):

    cont = 0
    maior_valor = 0

    print('-=-' * 30)

    print('Analisando os valores passados...')

    for valor in num:

        print(f'{valor} ', end='', flush=True)

        sleep(0.3)

        if cont == 0:

            maior_valor = valor

        else:

            if valor > maior_valor:

                maior_valor = valor

        cont += 1

    print()

    print(f'Foram informados {cont} valores ao todo.')

    if cont > 0:

        print(f'O maior valor informado foi {maior_valor}.')

    else:

        print('Nenhum valor foi informado.')


maior(2, 9, 4, 5, 7, 1)

maior(4, 7, 0)

maior(1, 2)

maior(6)

maior()

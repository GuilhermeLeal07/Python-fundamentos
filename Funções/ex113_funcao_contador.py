"""
Ex113 - Função contador()

Neste exercício, criamos uma função capaz de realizar contagens crescentes e decrescentes.

O programa realiza:

- Contagem de 1 até 10
- Contagem de 10 até 0
- Contagem personalizada
- Correção automática de passo inválido
- Exibição gradual dos números

Conceitos trabalhados:

- Funções
- Parâmetros
- Estruturas de repetição
- while
- Validação de dados
- Biblioteca time

O objetivo é aprender a criar funções mais flexíveis e reutilizáveis.
"""

from time import sleep


def contador(i, f, p):

    print('-=-' * 20)

    print(f'Contagem de {i} até {f} de {p} em {p}')

    sleep(2.5)

    # Corrige passo negativo
    if p < 0:
        p *= -1

    # Corrige passo zero
    if p == 0:
        p = 1

    # Contagem crescente
    if i < f:

        cont = i

        while cont <= f:

            print(f'{cont} ', end='', flush=True)

            sleep(0.5)

            cont += p

        print('FIM!')

    # Contagem decrescente
    else:

        cont = i

        while cont >= f:

            print(f'{cont} ', end='', flush=True)

            sleep(0.5)

            cont -= p

        print('FIM!')


contador(1, 10, 1)

contador(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')

ini = int(input('Início: '))

fim = int(input('Fim: '))

pas = int(input('Passo: '))

contador(ini, fim, pas)

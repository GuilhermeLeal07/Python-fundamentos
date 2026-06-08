"""
Ex116 - Função para cálculo de fatorial

Neste exercício, criamos uma função capaz de calcular o fatorial de um número.

O programa permite:

- Calcular o fatorial
- Mostrar ou ocultar o processo do cálculo
- Utilizar parâmetro opcional

Conceitos trabalhados:

- Funções
- Parâmetros opcionais
- Estrutura de repetição
- return
- Booleanos (True e False)

O objetivo é aprender a criar funções mais flexíveis através de parâmetros opcionais.
"""


def fatorial(n, show=False):
    f = 1

    for c in range(n, 0, -1):
        if show:
            print(c, end='')

            if c > 1:
                print(' x ', end='')

            else:
                print(' = ', end='')
        f *= c
      
    return f

print(fatorial(5, show=True))  # show=True é para mostrar o resultado por completo.

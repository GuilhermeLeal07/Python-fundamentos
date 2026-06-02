"""
Ex112 - Função escreva()

Neste exercício, criamos uma função capaz de exibir mensagens com uma moldura ajustável.

O programa realiza:

- Recebimento de uma mensagem
- Cálculo automático do tamanho da moldura
- Exibição formatada do texto

Conceitos trabalhados:

- Funções
- Parâmetros
- len()
- Formatação de saída
- Reutilização de código

O objetivo é aprender a criar funções que adaptam seu comportamento de acordo com os dados recebidos.
"""

def escreva(msg):

    tamanho = len(msg) + 4

    print('~' * tamanho)

    print(f'  {msg}')

    print('~' * tamanho)

escreva('Guilherme Leal')

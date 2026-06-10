"""
Ex117 - Função ficha()

Neste exercício, criamos uma função capaz de exibir a ficha de um jogador de futebol.

O programa permite:

- Informar o nome do jogador
- Informar a quantidade de gols
- Trabalhar com parâmetros opcionais
- Tratar entradas inválidas

Conceitos trabalhados:

- Funções
- Parâmetros opcionais
- Validação de dados
- Método isnumeric()
- Método strip()

O objetivo é aprender a criar funções mais robustas e seguras.
"""


def ficha(jog='<DESCONHECIDO>', gol=0):
    print(
        f'O jogador {jog} '
        f'fez {gol} gol(s) '
        f'no campeonato.' )


n = str(input('Nome do jogador: '))

g = str(input('Número de Gols: '))

if g.isnumeric():
    g = int(g)

else:
    g = 0

if n.strip() == '':
    ficha(gol=g)

else:
    ficha(n, g)

"""
Ex119 - Função notas()

Neste exercício, criamos uma função capaz de analisar várias notas e retornar um dicionário com informações da turma.

O programa realiza:

- Contagem de notas
- Identificação da maior nota
- Identificação da menor nota
- Cálculo da média
- Avaliação da situação da turma (opcional)
- Documentação da função com docstring

Conceitos trabalhados:

- Funções
- Parâmetros opcionais
- Empacotamento (*args)
- Dicionários
- Docstrings
- Funções nativas do Python

O objetivo é aprender a criar funções mais completas e documentadas.
"""


def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos
    :param sit: valor opcional indicando se deve ou não adicionar a situação da turma
    :return: dicionário contendo informações da turma
    """

    r = dict()

    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)

    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'

        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'

        else:
            r['situação'] = 'RUIM'
    return r


resp = notas(9, 10, 5.5, 2.5, 1, 1.5, sit=True)
print(resp)
help(notas)

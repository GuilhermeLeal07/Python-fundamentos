"""
Ex116 - Função voto()

Neste exercício, criamos uma função capaz de determinar a situação eleitoral de uma pessoa com base no seu ano de nascimento.

O programa realiza:

- Recebimento do ano de nascimento
- Cálculo automático da idade
- Verificação da situação eleitoral
- Retorno da mensagem adequada

Conceitos trabalhados:

- Funções
- Parâmetros
- return
- Estruturas condicionais
- Biblioteca datetime

O objetivo é aprender a utilizar funções que retornam valores para o programa.
"""

from datetime import date

def voto(ano):
    atual = date.today().year
    idade = atual - ano

    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA!'

    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL!'

    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'


nasc = int(
    input('Em que ano você nasceu? ')
)

print(voto(nasc))

"""
Ex118 - Função leiaInt()

Neste exercício, criamos uma função capaz de validar a entrada de dados, aceitando apenas números inteiros.

O programa realiza:

- Leitura de um valor
- Validação da entrada
- Tratamento de erro
- Retorno do número convertido

Conceitos trabalhados:

- Funções
- Estrutura while
- Validação de dados
- Método isnumeric()
- return
- Laços de repetição

O objetivo é criar uma função mais segura para entrada de dados do usuário.
"""


def leiaInt(msg):
    ok = False
    valor = 0

    while True:
        n = str(input(msg))

        if n.isnumeric():
            valor = int(n)
            ok = True

        else:
            print(
                '\033[0;31m'
                'ERRO! Digite um número inteiro válido.'
                '\033[m')

        if ok:
            break

    return valor

n = leiaInt('Digite um número: ')

print(f'Você acabou de digitar o número {n}')

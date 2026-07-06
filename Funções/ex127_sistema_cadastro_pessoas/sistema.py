from time import sleep
from lib.arquivo import (
    arquivo_existe,
    cadastrar,
    criar_arquivo,
    ler_arquivo,
)
from lib.interface import cabecalho, menu, leia_int

"""
Sistema principal de cadastro de pessoas.

Responsável por controlar o fluxo da aplicação.
"""

ARQUIVO = 'pessoas.txt'

if not arquivo_existe(ARQUIVO):
    criar_arquivo(ARQUIVO)

while True:
    resposta = menu([
        'Ver pessoas cadastradas',
        'Cadastrar nova pessoa',
        'Sair do sistema'
    ])

    if resposta == 1:
        ler_arquivo(ARQUIVO)

    elif resposta == 2:
        cabecalho('NOVO CADASTRO')

        nome = input('Nome: ')
        idade = leia_int('Idade: ')
        cadastrar(ARQUIVO, nome, idade)

    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break

    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')

    sleep(2)

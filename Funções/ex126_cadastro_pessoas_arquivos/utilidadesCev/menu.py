from funcoes import (
    arquivo_existe,
    criar_arquivo,
    ler_arquivo,
    cadastrar,
)

ARQUIVO = 'arquivo.txt'

if not arquivo_existe(ARQUIVO):
    criar_arquivo(ARQUIVO)

while True:

    print('─' * 30)
    print('      MENU PRINCIPAL')
    print('─' * 30)

    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova pessoa')
    print('0 - Sair')

    opc = input('Sua opção: ').strip()

    if opc == '1':
        ler_arquivo(ARQUIVO)

    elif opc == '2':
        nome = input('Nome: ')
        idade = input('Idade: ')
        cadastrar(ARQUIVO, nome, idade)

    elif opc == '0':
        print('Saindo do programa...')
        break

    else:
        print('ERRO! Digite uma opção válida.')

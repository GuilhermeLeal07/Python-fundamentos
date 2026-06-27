def titulo(texto):
    print('~' * 30)
    print(texto.center(30))
    print('~' * 30)


def ajuda(funcao):
    print('=' * 30)
    print(f'Função {funcao.__name__} retorna:')
    help(funcao)

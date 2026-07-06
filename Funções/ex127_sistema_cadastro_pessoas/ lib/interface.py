def linha(tam=42):
    """Retorna uma linha decorativa."""
    return '-' * tam

def cabecalho(txt):
    """Exibe um cabeçalho formatado."""

    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    """Mostra o menu principal."""
    cabecalho('MENU PRINCIPAL')

    for i, item in enumerate(lista, start=1):
        print(f'{i} - {item}')
    print(linha())

    return leia_int('Sua opção: ')

def leia_int(msg):
    """Lê apenas números inteiros."""
    while True:
        try:
            return int(input(msg))

        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')

        except KeyboardInterrupt:
            print('\n\033[31mEntrada interrompida pelo usuário.\033[m')
            return 0

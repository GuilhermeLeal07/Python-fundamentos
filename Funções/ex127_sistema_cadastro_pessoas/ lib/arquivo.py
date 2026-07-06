from time import sleep

def arquivo_existe(nome):
    """Verifica se o arquivo existe."""

    try:
        open(nome, 'rt')

    except FileNotFoundError:
        return False

    else:
        return True

def criar_arquivo(nome):
    """Cria um arquivo vazio."""

    try:
        with open(nome, 'wt+'):

            pass

    except Exception as erro:
        print(f'Houve um erro ao criar o arquivo: {erro}')

    else:
        print(f'Arquivo {nome} criado com sucesso!')


def ler_arquivo(nome):
    """Exibe todos os cadastros."""

    try:
        with open(nome, 'rt') as arquivo:

            print('-' * 42)
            print('PESSOAS CADASTRADAS'.center(42))
            print('-' * 42)

            for linha in arquivo:
                dado = linha.split(';')
                dado[1] = dado[1].replace('\n', '')

                print(f'{dado[0]:<30}{dado[1]:>3} anos')

    except Exception as erro:
        print(f'Erro ao ler o arquivo: {erro}')

def cadastrar(arq, nome='desconhecido', idade=0):
    """Adiciona um novo cadastro."""

    try:
        with open(arq, 'at') as arquivo:
            arquivo.write(f'{nome};{idade}\n')

    except Exception as erro:
        print(f'Houve um erro ao escrever os dados: {erro}')

    else:
        print(f'Novo registro de {nome} adicionado.')
        sleep(1)

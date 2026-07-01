import os


def arquivo_existe(nome_arquivo):
    """Verifica se o arquivo existe."""

    return os.path.exists(nome_arquivo)

def criar_arquivo(nome_arquivo):
    """Cria um novo arquivo vazio."""

    try:
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write('')

    except Exception as erro:
        print(f'Erro ao criar o arquivo "{nome_arquivo}": {erro}')

    else:
        print(f'Arquivo "{nome_arquivo}" criado com sucesso!')

def ler_arquivo(nome_arquivo):
    """Lê e exibe o conteúdo do arquivo."""

    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                print(linha.strip())

    except Exception as erro:
        print(f'Erro ao ler o arquivo "{nome_arquivo}": {erro}')

def cadastrar(nome_arquivo, nome='Desconhecido', idade=0):
    """Adiciona um novo cadastro ao arquivo."""

    try:
        with open(nome_arquivo, 'a') as arquivo:
            arquivo.write(f'{nome};{idade}\n')

    except Exception as erro:
        print(f'Erro ao escrever no arquivo "{nome_arquivo}": {erro}')

    else:
        print(f'Novo registro de {nome} adicionado com sucesso!')

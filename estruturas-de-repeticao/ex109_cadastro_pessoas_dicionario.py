"""
Ex109 - Cadastro e análise de pessoas utilizando dicionários

Neste exercício, utilizamos listas e dicionários para armazenar informações de várias pessoas.

O programa realiza:

- Cadastro de nome, sexo e idade
- Cálculo da média de idade
- Listagem das mulheres cadastradas
- Exibição das pessoas acima da média

Conceitos trabalhados:

- Dicionários
- Listas compostas
- Método copy()
- Estrutura while
- Validação de entrada
- Cálculos estatísticos básicos

O objetivo é desenvolver lógica de cadastro, organização e análise de dados.
"""

# Lista principal
galera = []

# Dicionário temporário
pessoa = {}

# Variáveis de controle
soma_idades = 0

# Cadastro das pessoas
while True:

    pessoa.clear()

    # Nome
    pessoa['nome'] = input(
        'Nome: '
    ).strip()

    # Sexo
    while True:

        pessoa['sexo'] = input(
            'Sexo [M/F]: '
        ).strip().upper()[0]

        if pessoa['sexo'] in 'MF':
            break

        print('ERRO! Digite apenas M ou F.')

    # Idade
    pessoa['idade'] = int(
        input('Idade: ')
    )

    # Soma das idades
    soma_idades += pessoa['idade']

    # Adiciona cópia do dicionário
    galera.append(pessoa.copy())

    # Continuação
    while True:

        resposta = input(
            'Quer continuar? [S/N] '
        ).strip().upper()[0]

        if resposta in 'SN':
            break

        print('ERRO! Digite apenas S ou N.')

    if resposta == 'N':
        break

# Média de idade
media = soma_idades / len(galera)

# Saída
print('==' * 30)

print(
    f'A) Ao todo temos '
    f'{len(galera)} pessoas cadastradas.'
)

print(
    f'B) A média de idade é de '
    f'{media:.2f} anos.'
)

# Mulheres cadastradas
print('C) Mulheres cadastradas: ', end='')

for pessoa in galera:

    if pessoa['sexo'] == 'F':

        print(f'{pessoa["nome"]} ', end='')

print()

# Pessoas acima da média
print('D) Lista das pessoas acima da média:')

for pessoa in galera:

    if pessoa['idade'] >= media:

        print()

        for chave, valor in pessoa.items():

            print(
                f'{chave}: {valor}'
            )

print()

print('<<< ENCERRADO >>>')

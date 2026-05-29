"""
Ex107 - Cadastro de trabalhador utilizando dicionário

Neste exercício, utilizamos dicionários para armazenar dados profissionais de uma pessoa.

O programa realiza:

- Cadastro do nome
- Cálculo da idade
- Cadastro da carteira de trabalho
- Registro de contratação e salário
- Cálculo da aposentadoria
- Exibição organizada dos dados

Conceitos trabalhados:

- Dicionários
- Biblioteca datetime
- Estruturas condicionais
- Manipulação de chaves e valores
- Cálculos automáticos

O objetivo é desenvolver lógica de cadastro e organização de informações profissionais.
"""

# Importação
from datetime import datetime

# Dicionário principal
dados = {}

# Entrada de dados
dados['nome'] = input('Nome: ').strip()

ano_nascimento = int(
    input('Ano de nascimento: ')
)

# Cálculo da idade
dados['idade'] = (
    datetime.now().year - ano_nascimento
)

# Validação da CTPS
while True:

    ctps = input(
        'Número da CTPS (0 = não possui): '
    ).strip()

    if ctps.isdigit():

        dados['ctps'] = int(ctps)

        break

    print('ERRO! Digite apenas números.')

# Verifica se possui carteira
if dados['ctps'] != 0:

    dados['contratação'] = int(
        input('Ano de contratação: ')
    )

    dados['salário'] = float(
        input('Salário: R$ ')
    )

    # Cálculo da aposentadoria
    dados['aposentadoria'] = (
        dados['idade']
        + (
            (dados['contratação'] + 35)
            - datetime.now().year
        )
    )

# Saída organizada
print('==' * 30)

print(f'Nome: {dados["nome"]}')

print(f'Idade: {dados["idade"]} anos')

print(f'CTPS: {dados["ctps"]}')

# Exibe apenas se possuir carteira
if dados['ctps'] != 0:

    print(
        f'Ano de contratação: '
        f'{dados["contratação"]}'
    )

    print(
        f'Salário: '
        f'R$ {dados["salário"]:.2f}'
    )

    print(
        f'Aposentadoria: '
        f'{dados["aposentadoria"]} anos'
    )

print('==' * 30)

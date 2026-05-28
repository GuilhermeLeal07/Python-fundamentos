"""
Ex105 - Cadastro de aluno utilizando dicionário

Neste exercício, utilizamos dicionários para armazenar informações de um aluno.

O programa realiza:

- Cadastro do nome
- Cadastro da média
- Verificação da situação do aluno
- Exibição organizada dos dados

Conceitos trabalhados:

- Dicionários
- Estruturas condicionais
- Método items()
- Manipulação de chaves e valores
- Organização de dados

O objetivo é desenvolver lógica de armazenamento estruturado utilizando dicionários.
"""

# Criação do dicionário
aluno = {}

# Entrada de dados
aluno['nome'] = input('Nome: ')

aluno['média'] = float(
    input(f'Média de {aluno["nome"]}: ')
)

# Verificação da situação
if aluno['média'] >= 7:

    aluno['situação'] = 'APROVADO'

elif 5 <= aluno['média'] < 7:

    aluno['situação'] = 'RECUPERAÇÃO'

else:

    aluno['situação'] = 'REPROVADO'

# Saída
print('-=-' * 30)

for chave, valor in aluno.items():

    print(f' * {chave} é igual a {valor}')

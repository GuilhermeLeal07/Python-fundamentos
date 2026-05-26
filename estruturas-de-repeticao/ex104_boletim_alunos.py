"""
Ex104 - Sistema de boletim escolar

Neste exercício, utilizamos listas compostas
para armazenar informações de alunos e suas notas.

O programa realiza:

- Cadastro de alunos
- Armazenamento das notas
- Cálculo da média
- Exibição de boletim geral
- Consulta individual de notas

Conceitos trabalhados:

- Listas compostas
- Estrutura while
- Método append()
- enumerate()
- Cálculo de média
- Manipulação de índices

O objetivo é desenvolver lógica de organização
e consulta de dados em sistemas acadêmicos.
"""

# Lista principal
ficha = []

# Cadastro dos alunos
while True:

    nome = input('Nome: ')

    nota1 = float(input('Nota 1: '))

    nota2 = float(input('Nota 2: '))

    media = (nota1 + nota2) / 2

    # Adiciona os dados do aluno
    ficha.append([nome, [nota1, nota2], media])

    # Continua ou encerra
    resposta = input('Quer continuar? [S/N] ').strip().upper()

    if resposta == 'N':
        break

# Exibição do boletim
print('-=-' * 15)

print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')

print('-' * 26)

for indice, aluno in enumerate(ficha):

    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

# Consulta individual
while True:

    print('-' * 35)

    opcao = int(
        input('Mostrar notas de qual aluno? (999 interrompe): ')
    )

    if opcao == 999:

        print('FINALIZANDO...')

        break

    if opcao <= len(ficha) - 1:

        print(
            f'Notas de {ficha[opcao][0]} são '
            f'{ficha[opcao][1]}'
        )

print('<<< VOLTE SEMPRE >>>')

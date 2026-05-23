"""
Ex099 - Cadastro de pessoas e análise de peso

Neste exercício, utilizamos listas compostas para armazenar dados de várias pessoas.

O programa realiza:

- Cadastro de nomes e pesos
- Contagem de pessoas cadastradas
- Identificação do maior peso
- Identificação do menor peso
- Exibição das pessoas mais pesadas e mais leves

Conceitos trabalhados:

- Listas compostas
- Método append()
- Método clear()
- Cópia de listas
- Estrutura while
- Comparação de valores

O objetivo é desenvolver lógica de armazenamento e análise de dados estruturados.
"""

# Listas
temporario = []
pessoas = []

# Variáveis de controle
maior_peso = 0
menor_peso = 0

# Entrada de dados
while True:

    temporario.append(
        input('Nome: ')
    )

    temporario.append(
        float(input('Peso: '))
    )

    # Primeiro cadastro
    if len(pessoas) == 0:

        maior_peso = menor_peso = temporario[1]

    else:

        # Verifica maior peso
        if temporario[1] > maior_peso:
            maior_peso = temporario[1]

        # Verifica menor peso
        if temporario[1] < menor_peso:
            menor_peso = temporario[1]

    # Copia os dados
    pessoas.append(temporario[:])

    # Limpa lista temporária
    temporario.clear()

    # Continua ou encerra
    resposta = input('Quer continuar? [S/N] ').strip().upper()

    if resposta == 'N':
        break

# Saída
print('-=-' * 30)

print(f'Os dados cadastrados foram: {pessoas}')

print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')

# Pessoas mais pesadas
print(f'O maior peso foi {maior_peso}kg. Peso de: ', end='')

for pessoa in pessoas:

    if pessoa[1] == maior_peso:
        print(f'{pessoa[0]} ', end='')

print()

# Pessoas mais leves
print(f'O menor peso foi {menor_peso}kg. Peso de: ', end='')

for pessoa in pessoas:

    if pessoa[1] == menor_peso:
        print(f'{pessoa[0]} ', end='')

print()

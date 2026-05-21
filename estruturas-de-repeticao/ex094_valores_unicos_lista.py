"""
Ex094 - Cadastro de valores únicos em lista

Neste exercício, utilizamos listas para armazenar valores numéricos sem permitir duplicatas.

O programa realiza:

- Cadastro de números
- Verificação de valores repetidos
- Ordenação da lista
- Exibição dos valores únicos

Conceitos trabalhados:

- Listas
- Estrutura while
- Operador in / not in
- Método append()
- Método sort()
- Validação de dados

O objetivo é desenvolver lógica de controle e organização de informações.
"""

# Lista de números
numeros = []

# Processamento
while True:

    numero = int(input('Digite um valor: '))

    # Verifica se o número já existe
    if numero not in numeros:

        numeros.append(numero)

        print('Valor adicionado com sucesso...')

    else:
        print('Valor duplicado! Não vou adicionar... ')

    # Pergunta se deseja continuar
    resposta = input('Quer continuar? [S/N] ').strip().upper()

    if resposta == 'N':
        break

# Ordena os valores
numeros.sort()

# Saída
print('-=-' * 30)

print(f'Você digitou os valores: {numeros}')

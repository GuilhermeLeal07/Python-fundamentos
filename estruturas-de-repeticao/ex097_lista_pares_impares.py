"""
Ex097 - Separando números pares e ímpares em listas

Neste exercício, utilizamos listas para armazenar valores digitados pelo usuário e separá-los entre números pares e ímpares.

O programa realiza:

- Cadastro de números
- Separação automática de pares e ímpares
- Exibição organizada das listas

Conceitos trabalhados:

- Listas
- Estrutura while
- Estrutura for
- enumerate()
- Operador módulo (%)
- Método append()

O objetivo é desenvolver lógica de classificação e organização de dados.
"""

# Listas principais
numeros = []
pares = []
impares = []

# Entrada de dados
while True:

    numeros.append(
        int(input('Digite um número: '))
    )

    resposta = input('Quer continuar? [S/N] ').strip().upper()

    if resposta == 'N':
        break

# Separação dos números
for indice, valor in enumerate(numeros):

    # Verifica números pares
    if valor % 2 == 0:
        pares.append(valor)

    # Verifica números ímpares
    else:
        impares.append(valor)

# Saída
print('-=-' * 30)

print(f'A lista completa é: {numeros}')
print(f'A lista de pares é: {pares}')
print(f'A lista de ímpares é: {impares}')

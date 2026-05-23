"""
Ex100 - Separando números pares e ímpares em lista composta

Neste exercício, utilizamos uma lista composta para armazenar números pares e ímpares separadamente.

O programa realiza:

- Leitura de sete valores numéricos
- Verificação de números pares e ímpares
- Armazenamento em listas separadas
- Ordenação crescente dos valores

Conceitos trabalhados:

- Listas compostas
- Método append()
- Método sort()
- Estrutura for
- Operador módulo (%)
- Organização de dados

O objetivo é desenvolver lógica de classificação e manipulação estruturada de listas.
"""

# Lista composta
numeros = [[], []]

# Entrada de dados
for contador in range(1, 8):

    valor = int(
        input(f'Digite o {contador}º valor: ')
    )

    # Verifica números pares
    if valor % 2 == 0:

        numeros[0].append(valor)

    # Verifica números ímpares
    else:

        numeros[1].append(valor)

# Ordenação das listas
numeros[0].sort()
numeros[1].sort()

# Saída
print('-=-' * 30)

print(f'Todos os valores pares digitados foram: {numeros[0]}')

print(f'Todos os valores ímpares digitados foram: {numeros[1]}')

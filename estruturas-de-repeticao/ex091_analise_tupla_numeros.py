"""
Ex091 - Analisando números em uma tupla

Neste exercício, utilizamos uma tupla para armazenar quatro números digitados pelo usuário.

O programa realiza:

- Contagem de quantas vezes o número 9 apareceu
- Verificação da posição do primeiro número 3
- Identificação dos números pares

Conceitos trabalhados:

- Tuplas
- Método count()
- Método index()
- Estrutura for
- Operador de módulo (%)
- Verificações condicionais

O objetivo é desenvolver habilidades de análise e consulta de dados em estruturas imutáveis.
"""

# Entrada
numeros = (
    int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite mais um número: ')),
    int(input('Digite o último número: '))
)

# Saída
print(f'\nVocê digitou os valores: {numeros}')

# Quantidade de vezes que o número 9 apareceu
print(f'O valor 9 apareceu {numeros.count(9)} vezes.')

# Verifica posição do primeiro valor 3
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3) + 1}ª posição.')
else:
    print('O valor 3 não foi digitado.')

# Verifica números pares
print('Os números pares digitados foram: ', end='')

for numero in numeros:
    if numero % 2 == 0:
        print(numero, end=' ')

"""
Ex093 - Maior e menor valor em uma lista

Neste exercício, utilizamos listas para armazenar valores digitados pelo usuário.

O programa realiza:

- Cadastro de valores numéricos
- Identificação do maior valor
- Identificação do menor valor
- Exibição das posições dos valores na lista

Conceitos trabalhados:

- Listas
- Estrutura for
- enumerate()
- Comparação de valores
- Manipulação de índices

O objetivo é desenvolver lógica de análise e localização de dados dentro de listas.
"""

# Lista de números
lista_num = []

# Variáveis de controle
maior = 0
menor = 0

# Entrada de dados
for contador in range(0, 5):

    lista_num.append(
        int(input(f'Digite um valor para a posição {contador}: '))
    )

    # Primeiro valor da lista
    if contador == 0:
        maior = menor = lista_num[contador]

    # Comparação dos valores
    else:

        if lista_num[contador] > maior:
            maior = lista_num[contador]

        if lista_num[contador] < menor:
            menor = lista_num[contador]

# Saída
print('=-' * 30)

print(f'Você digitou os valores: {lista_num}')

# Mostra posições do maior valor
print(f'O maior valor digitado foi {maior} nas posições ', end='')

for indice, valor in enumerate(lista_num):

    if valor == maior:
        print(f'{indice}... ', end='')

# Mostra posições do menor valor
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')

for indice, valor in enumerate(lista_num):

    if valor == menor:
        print(f'{indice}... ', end='')

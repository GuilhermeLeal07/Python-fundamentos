"""
Ex095 - Inserindo valores em ordem sem utilizar sort()

Neste exercício, utilizamos listas para armazenar valores já em ordem crescente sem utilizar o método sort().

O programa realiza:

- Cadastro de números
- Inserção automática na posição correta
- Organização crescente da lista
- Controle manual de posições

Conceitos trabalhados:

- Listas
- Método insert()
- Estrutura for
- Estrutura while
- Índices
- Comparações condicionais

O objetivo é desenvolver lógica de ordenação e manipulação dinâmica de listas.
"""

# Lista principal
lista = []

# Entrada de dados
for contador in range(0, 5):

    numero = int(input('Digite um valor: '))

    # Primeiro valor ou maior que o último da lista
    if contador == 0 or numero > lista[-1]:

        lista.append(numero)

        print('Adicionado ao final da lista...')

    else:

        posicao = 0

        # Procura posição correta
        while posicao < len(lista):

            if numero <= lista[posicao]:

                lista.insert(posicao, numero)

                print(f'Adicionado na posição {posicao} da lista...')

                break

            posicao += 1

# Saída
print('-=-' * 30)

print(f'Os valores digitados em ordem foram: {lista}')

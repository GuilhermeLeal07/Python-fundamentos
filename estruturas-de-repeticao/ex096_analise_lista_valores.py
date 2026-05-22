"""
Ex096 - Analisando valores em uma lista

Neste exercício, utilizamos listas para armazenar vários números digitados pelo usuário.

O programa realiza:

- Cadastro de valores
- Contagem de elementos
- Ordenação decrescente
- Verificação da existência de um valor específico

Conceitos trabalhados:

- Listas
- Estrutura while
- Método append()
- Método sort()
- Operador in
- Função len()

O objetivo é desenvolver lógica de análise e manipulação de dados em listas.
"""

# Lista principal
valores = []

# Entrada de dados
while True:

    valores.append(
        int(input('Digite um valor: '))
    )

    resposta = input('Quer continuar? [S/N] ').strip().upper()

    if resposta == 'N':
        break

# Saída
print('-=-' * 30)

# Quantidade de elementos
print(f'Você digitou {len(valores)} elementos.')

# Ordenação decrescente
valores.sort(reverse=True)

print(f'Os valores em ordem decrescente são: {valores}')

# Verificação do número 5
if 5 in valores:
    print('O valor 5 faz parte da lista!')

else:
    print('O valor 5 não foi encontrado na lista.')

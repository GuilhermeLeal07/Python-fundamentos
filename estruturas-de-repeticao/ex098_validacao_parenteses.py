"""
Ex098 - Validação de expressões com parênteses

Neste exercício, utilizamos listas como pilha para verificar se uma expressão matemática possui os parênteses abertos e fechados corretamente.

O programa realiza:

- Leitura de expressões
- Verificação de abertura e fechamento de parênteses
- Validação da estrutura da expressão

Conceitos trabalhados:

- Listas como pilha
- Estrutura for
- Método append()
- Método pop()
- Validação de expressões
- Estruturas condicionais

O objetivo é desenvolver lógica de validação e controle de estruturas em expressões.
"""

# Entrada
expressao = input('Digite a expressão: ')

# Lista utilizada como pilha
pilha = []

# Processamento
for simbolo in expressao:

    # Abre parênteses
    if simbolo == '(':
        pilha.append('(')

    # Fecha parênteses
    elif simbolo == ')':

        if len(pilha) > 0:
            pilha.pop()

        else:
            pilha.append(')')
            break

# Saída
if len(pilha) == 0:
    print('Sua expressão está válida!')

else:
    print('Sua expressão está errada!')

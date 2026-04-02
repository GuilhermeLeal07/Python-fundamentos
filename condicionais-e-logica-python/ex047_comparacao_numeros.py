"""
Exercício 047 - Comparação de Números

Este programa lê dois números e informa qual é maior
ou se ambos são iguais.

------------------------------------------
Fluxo:
1. Usuário digita dois números
2. O sistema compara os valores
3. Exibe o resultado da comparação
------------------------------------------
"""

# ===============================
# Entrada de dados
# ===============================

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))

# ===============================
# Processamento e saída
# ===============================

print('-' * 40)

if numero1 > numero2:
    print('O primeiro número é maior que o segundo.')
elif numero2 > numero1:
    print('O segundo número é maior que o primeiro.')
else:
    print('Os dois números são iguais.')

print('-' * 40)

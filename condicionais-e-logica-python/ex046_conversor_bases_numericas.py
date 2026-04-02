"""
Exercício 046 - Conversor de Bases Numéricas

Este programa converte um número inteiro para diferentes bases numéricas.

Opções disponíveis:
1 - Binário
2 - Octal
3 - Hexadecimal

------------------------------------------
Fluxo:
1. Usuário digita um número inteiro
2. Escolhe a base de conversão
3. O sistema exibe o resultado convertido
------------------------------------------
"""

# ===============================
# Entrada de dados
# ===============================

numero = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL ''')

opcao = int(input('Sua opção: '))

# ===============================
# Processamento e saída
# ===============================

print('-' * 40)

if opcao == 1:
    # Usei o [2:] para tirar os 2 primeiro no resultado
    resultado = bin(numero)[2:]
    print(f'{numero} em BINÁRIO é igual a {resultado}')

elif opcao == 2:
    resultado = oct(numero)[2:]
    print(f'{numero} em OCTAL é igual a {resultado}')

elif opcao == 3:
    resultado = hex(numero)[2:]
    print(f'{numero} em HEXADECIMAL é igual a {resultado}')

else:
    print('Opção inválida! Escolha entre 1, 2 ou 3.')

print('-' * 40)

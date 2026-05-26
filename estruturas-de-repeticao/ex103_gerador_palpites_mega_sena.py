"""
Ex103 - Gerador de palpites para Mega Sena

Neste exercício, utilizamos listas compostas e números aleatórios para gerar jogos da Mega Sena.

O programa realiza:

- Sorteio de números aleatórios
- Geração de múltiplos jogos
- Organização dos números em ordem crescente
- Exibição formatada dos palpites

Conceitos trabalhados:

- Listas compostas
- Biblioteca random
- Função randint()
- Estrutura while
- Método append()
- Método sort()
- Validação de números repetidos

O objetivo é desenvolver lógica de sorteio, organização e manipulação de listas.
"""

# Importações
from random import randint
from time import sleep

# Listas
numeros = []
jogos = []

# Interface
print('-=-' * 15)
print('        JOGA NA MEGA SENA')
print('-=-' * 15)

# Quantidade de jogos
quantidade = int(
    input('Quantos jogos você quer que eu sorteie? ')
)

# Controle dos jogos
total = 0

while total < quantidade:

    contador = 0

    # Geração dos números
    while True:

        numero = randint(1, 60)

        # Evita números repetidos
        if numero not in numeros:

            numeros.append(numero)

            contador += 1

        # Finaliza com 6 números
        if contador >= 6:
            break

    # Organiza os números
    numeros.sort()

    # Adiciona o jogo na lista principal
    jogos.append(numeros[:])

    # Limpa lista temporária
    numeros.clear()

    total += 1

# Saída
print('-=-' * 5, f'SORTEANDO {quantidade} JOGOS', '-=-' * 5)

for indice, jogo in enumerate(jogos):

    print(f'Jogo {indice + 1}: {jogo}')

    sleep(1)

print('-=-' * 5, '|| BOA SORTE ||', '-=-' * 5)

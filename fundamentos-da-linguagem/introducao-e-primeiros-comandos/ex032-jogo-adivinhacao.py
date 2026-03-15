"""
Jogo da Adivinhação

Objetivo:
Criar um programa onde o computador "pensa" em um número entre 0 e 5 e o jogador tenta adivinhar qual foi o número escolhido.

O programa deve informar se o jogador venceu ou perdeu.

Conceitos praticados neste exercício:
- importação de bibliotecas
- geração de números aleatórios
- uso de tempo de espera (sleep)
- estruturas condicionais (if / else)
"""
"""
-------------------------------------------------
Importação das bibliotecas necessárias
-------------------------------------------------
"""

import random # random → usado para gerar números aleatórios
from time import sleep # sleep → usado para criar uma pequena pausa no programa

"""
-------------------------------------------------
O computador "pensa" em um número
-------------------------------------------------
"""

computador = random.randint(0, 5)

"""
randint significa:
Gerar um número inteiro aleatório dentro de um intervalo
"""

"""
-------------------------------------------------
Apresentação do jogo
-------------------------------------------------
"""

print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5.")
print("Tente adivinhar qual foi o número escolhido!")
print("-=-" * 20)

"""
-------------------------------------------------
Jogador tenta adivinhar
-------------------------------------------------
"""
jogador = int(input("Em que número eu pensei? "))

"""
-------------------------------------------------
Simulação de processamento
-------------------------------------------------
"""
print("PROCESSANDO...")
sleep(3)

# sleep(3) faz o programa esperar 3 segundos antes de mostrar o resultado


#Resultado:

if jogador == computador:
    print("Parabéns! Você conseguiu me vencer!")
else:
    print("GANHEI! Eu pensei no número {} e não no {}.".format(computador, jogador))

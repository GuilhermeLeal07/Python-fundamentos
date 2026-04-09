"""
Exercício 050 - Graduação em Jiu-Jitsu

Este programa classifica o praticante de acordo com seu tempo de treino.

------------------------------------------
Faixas:
- Até 1 ano → Faixa Branca
- Até 3 anos → Faixa Azul
- Até 5 anos → Faixa Roxa
- Até 8 anos → Faixa Marrom
- Acima → Faixa Preta
------------------------------------------
"""

# ===============================
# Entrada de dados
# ===============================

tempo = float(input('Há quantos anos você treina? '))

# ===============================
# Processamento e saída
# ===============================

print('-' * 40)

if tempo <= 1:
    print('Faixa: BRANCA')

elif tempo <= 3:
    print('Faixa: AZUL')

elif tempo <= 5:
    print('Faixa: ROXA')

elif tempo <= 8:
    print('Faixa: MARROM')

else:
    print('Faixa: PRETA')

print('-' * 40)

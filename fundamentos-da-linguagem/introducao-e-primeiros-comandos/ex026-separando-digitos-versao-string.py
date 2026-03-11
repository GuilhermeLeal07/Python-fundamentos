"""
Separando dígitos de um número (versão com string)

Objetivo:
Ler um número inteiro e mostrar separadamente os dígitos de unidade, dezena, centena e milhar.

Irei usar o zfill(4) pois isso preenche com zeros à esquerda.
"""

# Entrada de dados
num = input("Digite um número entre 0 e 9999: ").zfill(4)

# Separação dos dígitos
m = num[0]
c = num[1]
d = num[2]
u = num[3]

# Saída de dados
print("-" * 40)
print("Analisando o número {}".format(num))
print("Milhar: {}".format(m))
print("Centena: {}".format(c))
print("Dezena: {}".format(d))
print("Unidade: {}".format(u))
print("-" * 40)

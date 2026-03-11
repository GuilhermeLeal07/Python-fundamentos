"""
Separando dígitos de um número

Objetivo:
Ler um número inteiro e mostrar separadamente os dígitos de unidade, dezena, centena e milhar.
"""

# Entrada de dados
num = int(input("Digite um número entre 0 e 9999: "))

# Cálculo dos dígitos
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

# Saída de dados
print("-" * 40)
print("Analisando o número {}".format(num))
print("Unidade: {}".format(u))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("Milhar: {}".format(m))
print("-" * 40)

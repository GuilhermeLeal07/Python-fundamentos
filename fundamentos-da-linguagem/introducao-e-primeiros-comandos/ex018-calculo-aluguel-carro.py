"""
Cálculo de aluguel de carro

Objetivo:
Calcular o valor total a pagar pelo aluguel de um carro, considerando a quantidade de dias alugados e os quilômetros percorridos.

Regras:
R$55 por dia de aluguel
R$0.20 por quilômetro rodado
"""

# Entrada de dados
dias = int(input("Por quantos dias o carro foi alugado? "))
km = float(input("Quantos quilômetros foram percorridos? "))

# Cálculo do valor total
valor_total = (dias * 55) + (km * 0.20)

# Saída de dados
print("-" * 40)
print("Dias de aluguel: {}".format(dias))
print("Quilômetros percorridos: {:.2f} km".format(km))
print("Valor total a pagar: R${:.2f}".format(valor_total))
print("-" * 40)

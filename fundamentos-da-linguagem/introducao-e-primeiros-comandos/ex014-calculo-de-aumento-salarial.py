"""
Cálculo de Aumento Salarial

Objetivo:
Ler o salário de um funcionário e aplicar um percentual de aumento definido pelo usuário.
"""

# Entrada de dados
salario = float(input("Informe o salário atual do funcionário: R$ "))
percentual = float(input("Qual percentual de aumento deseja aplicar? (%) "))

# Cálculo do aumento
aumento = salario * percentual / 100
novo_salario = salario + aumento

# Saída de dados
print("-" * 40)
print("Salário atual: R${:.2f}".format(salario))
print("Percentual de aumento aplicado: {}%".format(percentual))
print("Valor do aumento: R${:.2f}".format(aumento))
print("Novo salário: R${:.2f}".format(novo_salario))
print("-" * 40)

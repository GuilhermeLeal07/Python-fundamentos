"""
Aumento salarial

Objetivo:
Ler o salário de um funcionário e calcular seu aumento.

Regras:
- Salários até R$1250 → aumento de 15%
- Salários acima de R$1250 → aumento de 10%

Conceitos praticados:
- estruturas condicionais (if / else)
- operações matemáticas
- uso de f-strings (formatação moderna)
"""

# -------------------------------------------------
# Entrada de dados

salario = float(input("Qual é o salário do funcionário? R$ "))

# -------------------------------------------------
# Cálculo do aumento

if salario <= 1250:
    novo_salario = salario + (salario * 15 / 100)
else:
    novo_salario = salario + (salario * 10 / 100)


# -------------------------------------------------
# Saída de dados

print("-" * 40)
print(f"Quem ganhava R${salario:.2f} passa a ganhar R${novo_salario:.2f} agora.")
print("-" * 40)

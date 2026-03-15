"""
Verificador de velocidade

Objetivo:
Criar um programa que leia a velocidade de um carro.

Se a velocidade ultrapassar 80 km/h, o motorista deve receber uma multa no valor de R$7.00 para cada km/h acima do limite.

Conceitos praticados:
- entrada de dados
- estruturas condicionais (if / else)
- operações matemáticas
- formatação de números
"""

# Entrada de dados
# -------------------------------------------------

velocidade = float(input("Qual a velocidade do carro (km/h)? "))


# Mensagem inicial
# -------------------------------------------------

print("Tenha um bom dia! Dirija com segurança.")


# Verificação da velocidade
# -------------------------------------------------

if velocidade > 80:
    
    print("MULTADO! Você ultrapassou o limite permitido.")

    # cálculo da multa
    multa = (velocidade - 80) * 7

    print("Você deve pagar uma multa de R${:.2f}".format(multa))

else:
    
    print("Você está dentro do limite de velocidade.")

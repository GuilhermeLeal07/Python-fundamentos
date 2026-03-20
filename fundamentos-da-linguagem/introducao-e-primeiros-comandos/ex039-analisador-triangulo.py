"""
Analisador de Triângulo

Objetivo:
Ler o comprimento de três segmentos de reta e verificar se eles podem formar um triângulo.

Caso formem, identificar o tipo:
- Equilátero (todos os lados iguais)
- Isósceles (dois lados iguais)
- Escaleno (todos os lados diferentes)

Conceitos praticados:
- estruturas condicionais (if / elif / else)
- operadores lógicos (and, or)
- comparação de valores
"""

# Apresentação
# -------------------------------------------------

print("Analisador de Triângulo")
print("-=-" * 20)

# -------------------------------------------------
# Entrada de dados
# -------------------------------------------------

l1 = float(input("Qual o lado 1? "))
l2 = float(input("Qual o lado 2? "))
l3 = float(input("Qual o lado 3? "))

# -------------------------------------------------
# Verificação se forma triângulo
# -------------------------------------------------

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    
    print("Os segmentos PODEM formar um triângulo.")

    # ---------------------------------------------
    # Classificação do triângulo
    # ---------------------------------------------

    if l1 == l2 == l3:
        print("Tipo: EQUILÁTERO")
    
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("Tipo: ISÓSCELES")
    
    else:
        print("Tipo: ESCALENO")

else:
    print("Os segmentos NÃO podem formar um triângulo.")

"""
Maior e menor números

Objetivo:
Ler três números e mostrar qual é o maior e qual é o menor.

Conceitos praticados:
- entrada de dados
- estruturas condicionais (if)
- comparação entre valores
- uso de f-strings (formatação moderna)
"""

# Entrada de dados
# -------------------------------------------------

n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
n3 = int(input("Terceiro valor: "))


# -------------------------------------------------
# Verificação do menor valor

menor = n1

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3


# -------------------------------------------------
# Verificação do maior valor

maior = n1

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3


# -------------------------------------------------
# Saída de dados

print("-=-" * 40)
print(f"O menor valor digitado foi {menor}")
print(f"O maior valor digitado foi {maior}")
print("-=-" * 40)

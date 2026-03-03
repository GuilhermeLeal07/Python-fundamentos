"""
Dobro, Triplo e Raiz Quadrada

Objetivo:
Ler um número e mostrar seu dobro, triplo e raiz quadrada.
"""

n = float(input("Digite um número: "))

dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2) #Lembrando, RAIZ quadrada usando potência

print("-" * 40)
print("Número escolhido: {}".format(numero))
print("Dobro: {}".format(dobro))
print("Triplo: {}".format(triplo))
print("Raiz quadrada: {:.2f}".format(raiz))
print("-" * 40)

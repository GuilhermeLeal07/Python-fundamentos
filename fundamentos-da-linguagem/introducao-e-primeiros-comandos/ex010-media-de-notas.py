"""
Cálculo de Média

Objetivo:
Ler o nome de um aluno e duas notas, calculando a média final.
"""

# Nome do aluno e suas notas
nome = input("Aluno, qual é seu nome? ")
n1 = float(input("Qual é a nota da sua T1? "))
n2 = float(input("Qual é a nota da sua T2? "))

media = (n1 + n2) / 2

print("-" * 40)
print("Aluno: {}".format(nome))
print("Notas: {:.2f} e {:.2f}".format(n1, n2))
print("Média final: {:.2f}".format(media))
print("-" * 40)

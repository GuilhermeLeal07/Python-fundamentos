"""
Analisando a letra "A" em uma frase

Objetivo:
Ler uma frase e mostrar:
- Quantas vezes aparece a letra "A"
- A posição da primeira ocorrência
- A posição da última ocorrência
"""

# Entrada de dados
frase = input("Digite uma frase: ").strip().upper()

# Análise da frase
quantidade_a = frase.count("A")
primeira_posicao = frase.find("A") + 1
ultima_posicao = frase.rfind("A") + 1

# Saída de dados
print("-" * 40)
print("A letra 'A' aparece {} vezes.".format(quantidade_a))
print("A primeira letra 'A' aparece na posição {}".format(primeira_posicao))
print("A última letra 'A' aparece na posição {}".format(ultima_posicao))
print("-" * 40)

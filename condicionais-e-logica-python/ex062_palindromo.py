"""
Exercício 062 - Verificador de Palíndromo

Este programa verifica se uma frase é um palíndromo, desconsiderando espaços e letras maiúsculas/minúsculas.
"""

# ===============================
# Entrada de dados
# ===============================

frase = input('Digite uma frase: ').strip().upper()

# ===============================
# Tratamento da frase
# ===============================

palavras = frase.split()
junto = ''.join(palavras)

# ===============================
# Processamento
# ===============================

inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

# ===============================
# Saída
# ===============================

print('-' * 40)
print(f'Frase original: {frase}')
print(f'Frase invertida: {inverso}')
print('-' * 40)

if inverso == junto:
    print('Resultado: É um PALÍNDROMO.')
else:
    print('Resultado: NÃO é um palíndromo.')

print('-' * 40)

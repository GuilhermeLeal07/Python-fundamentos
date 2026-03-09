"""
Manipulação de strings(texto) em Python

Exemplo demonstrando operações comuns com strings:
- Fatiamento
- Análise de texto
- Transformações
- Remoção de espaços
- Separação e junção de palavras
"""

# Frase base
frase = "Curso em Video Python"

# -----------------------------
# 1. Fatiamento de String
# -----------------------------
print(frase[0:5])     # 'Curso' → pega do índice 0 até o 4 (o final 5 não entra)
print(frase[9:14])    # 'Video' → pega do índice 9 até 13
print(frase[:5])      # 'Curso' → omite o início, começa do 0
print(frase[6:])      # 'em Video  Python' → omite o fim, vai até o final
print(frase[::2])     # 'Cro mVdo yhn' → pega de 2 em 2 caracteres

# -----------------------------
# 2. Análise
# -----------------------------
print(len(frase))           # quantidade total de caracteres (inclui espaços)
print(frase.count('o'))     # quantos 'o' existem
print(frase.find('deo'))    # posição de 'deo'
print(frase.find('Python')) # posição de Python

# -----------------------------
# 3. Transformações: replace(), upper(), lower(), capitalize(), title()
# -----------------------------
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

# -----------------------------
# 4. Removendo espaços (strip())
# -----------------------------
frase_com_espacos = "   Aprendendo Python   "
print(frase_com_espacos.strip())  # remove espaços do início e do fim
print(frase_com_espacos.rstrip()) # remove só da direita
print(frase_com_espacos.lstrip()) # remove só da esquerda

# -----------------------------
# 5. Separar e juntar palavras
# -----------------------------
lista_palavras = frase.split()  # ['Curso', 'em', 'Video', 'Python']
print('-'.join(lista_palavras)) # 'Curso-em-Video-Python'
print(' '.join(lista_palavras)) # 'Curso em Video Python'

"""
Cores no Terminal (ANSI Escape Codes)

Objetivo:
Demonstrar como utilizar cores e estilos no terminal usando ANSI.

-------------------------------------------------
FORMATO ANSI:

\033[style;text;backgroundm

Exemplo:
\033[1;33;44m → texto amarelo, fundo azul, negrito
-------------------------------------------------

STYLE (estilo)
0 → nenhum
1 → negrito
4 → sublinhado
7 → negativo (inverte cores)

TEXT (cor do texto)
30 → branco
31 → vermelho
32 → verde
33 → amarelo
34 → azul
35 → roxo
36 → ciano
37 → cinza

BACKGROUND (cor de fundo)
40 → branco
41 → vermelho
42 → verde
43 → amarelo
44 → azul
45 → roxo
46 → ciano
47 → cinza
"""

# -------------------------------------------------
# Exemplos práticos
# -------------------------------------------------

print("\033[1;31mVermelho em negrito\033[m")
print("\033[1;32mVerde em negrito\033[m")
print("\033[1;33mAmarelo em negrito\033[m")
print("\033[1;34mAzul em negrito\033[m")
print("\033[1;35mRoxo em negrito\033[m")
print("\033[1;36mCiano em negrito\033[m")

print("=-=" * 40)

print("\033[7;30mTexto em modo negativo\033[m")
print("\033[4;33mTexto sublinhado amarelo\033[m")
print("\033[1;30;43mTexto preto com fundo amarelo\033[m")

print("=-=" * 40)

# Interação simples
nome = input("Digite seu nome: ")
print(f"\033[1;36mPrazer em te conhecer, {nome}!\033[m")

# Interação com usuário (opcional)
texto = input("Digite um texto: ")
cor = input("Escolha uma cor (vermelho, verde, azul...): ")

print(colorir(texto, cor))

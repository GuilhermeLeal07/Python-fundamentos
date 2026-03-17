"""
Verificador de Ano Bissexto

Objetivo:
Criar um programa que leia um ano qualquer e informe se ele é bissexto ou não.

Observação:
Se o usuário digitar 0, o programa irá analisar o ano atual.

Regras do ano bissexto:
- O ano deve ser divisível por 4
- Mas não pode ser divisível por 100
- Exceto se também for divisível por 400
"""

# Importação
# -------------------------------------------------

from datetime import date  # para pegar o ano atual

# -------------------------------------------------
# Entrada de dados
# -------------------------------------------------

ano = int(input("Que ano quer analisar? (0 para ano atual): "))


# -------------------------------------------------
# Ano atual
# -------------------------------------------------

if ano == 0:
    ano = date.today().year

# -------------------------------------------------
# Agora para o ano bissexto
# -------------------------------------------------

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é BISSEXTO.")
else:
    print(f"O ano {ano} NÃO é BISSEXTO.")

"""
Exercício 048 - Alistamento Militar

Este programa verifica a situação de alistamento militar
com base na idade do usuário e também pergunta se ele já se alistou.

------------------------------------------
Fluxo:
1. Usuário informa o ano de nascimento
2. O sistema calcula a idade atual
3. Pergunta se o usuário já se alistou
4. Se SIM → informa que está em dia
5. Se NÃO → analisa a situação:
   - Se ainda vai se alistar
   - Se é hora de se alistar
   - Se já passou do prazo
------------------------------------------
"""

# ===============================
# Importação e entrada de dados
# ===============================

from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input('Digite seu ano de nascimento: '))

# ===============================
# Processamento da idade
# ===============================

idade = ano_atual - ano_nascimento

print('-' * 40)
print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}')
print('-' * 40)

# ===============================
# Pergunta ao usuário
# ===============================

resposta = input('Você já se alistou? [S/N] ').strip().upper()

print('-' * 40)

# ===============================
# Verificação da situação
# ===============================

if resposta == 'S':
    print('Você está em dia com suas obrigações militares.')

elif resposta == 'N':

    if idade == 18:
        print('Você deve se alistar IMEDIATAMENTE!')

    elif idade < 18:
        anos_faltando = 18 - idade
        ano_alistamento = ano_atual + anos_faltando

        print(f'Ainda faltam {anos_faltando} anos para o alistamento.')
        print(f'Seu alistamento será em {ano_alistamento}.')

    else:
        anos_passados = idade - 18
        ano_alistamento = ano_atual - anos_passados

        print(f'Você já deveria ter se alistado há {anos_passados} anos.')
        print(f'Seu alistamento foi em {ano_alistamento}.')
        print('COMPAREÇA À JUNTA MILITAR O QUANTO ANTES.')

else:
    print('Opção inválida. Digite apenas S ou N.')

print('-' * 40)

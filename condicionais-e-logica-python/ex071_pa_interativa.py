"""
Exercício 071 - Progressão Aritmética Interativa

Este programa mostra os termos de uma PA e permite que o usuário solicite mais termos até decidir parar.
"""

# ===============================
# Entrada de dados
# ===============================

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

# ===============================
# Processamento
# ===============================

termo = primeiro_termo
contador = 1
total = 0
termos_adicionais = 10

print('-' * 40)

while termos_adicionais != 0:
    total += termos_adicionais

    while contador <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        contador += 1

    print('PAUSA')
    termos_adicionais = int(input('Quantos termos você quer mostrar a mais? '))

# ===============================
# Saída
# ===============================

print('\nProgressão finalizada.')
print(f'Total de termos exibidos: {total}')
print('-' * 40)

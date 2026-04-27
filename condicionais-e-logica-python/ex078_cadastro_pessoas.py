"""
Exercício 078 - Cadastro e Análise de Pessoas

Este programa lê idade e sexo de várias pessoas.
Ao final, informa:
- Quantas pessoas têm mais de 18 anos
- Quantos homens foram cadastrados
- Quantas mulheres têm menos de 20 anos
"""

# ===============================
# Inicialização
# ===============================

total_maiores_18 = 0
total_homens = 0
total_mulheres_menos_20 = 0

# ===============================
# Loop principal
# ===============================

while True:
    print('-' * 40)
    print('CADASTRO DE PESSOA')
    print('-' * 40)

    idade = int(input('Idade: '))

    sexo = ''
    while sexo not in ['M', 'F']:
        sexo = input('Sexo [M/F]: ').strip().upper()[0]

    # ===========================
    # Processamento
    # ===========================

    if idade >= 18:
        total_maiores_18 += 1

    if sexo == 'M':
        total_homens += 1

    if sexo == 'F' and idade < 20:
        total_mulheres_menos_20 += 1

    # ===========================
    # Continuação
    # ===========================

    resposta = ''
    while resposta not in ['S', 'N']:
        resposta = input('Quer continuar? [S/N]: ').strip().upper()[0]

    if resposta == 'N':
        break

# ===============================
# Saída
# ===============================

print('\n' + '=' * 40)
print('RESULTADO FINAL')
print('=' * 40)

print(f'Total de pessoas com mais de 18 anos: {total_maiores_18}')
print(f'Total de homens cadastrados: {total_homens}')
print(f'Mulheres com menos de 20 anos: {total_mulheres_menos_20}')

print('=' * 40)

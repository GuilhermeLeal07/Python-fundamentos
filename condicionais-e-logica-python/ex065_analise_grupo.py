"""
Exercício 065 - Análise de Grupo

Este programa lê o nome, idade e sexo de 4 pessoas
e informa:
- A média de idade do grupo
- O nome do homem mais velho
- Quantas mulheres têm menos de 20 anos
"""

# ===============================
# Processamento
# ===============================

soma_idade = 0
maior_idade_homem = 0
nome_homem_mais_velho = ''
total_mulheres_menos_20 = 0

for pessoa in range(1, 5):
    print(f'----- {pessoa}ª PESSOA -----')

    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()

    soma_idade += idade

    # Verifica homem mais velho
    if sexo == 'M':
        if pessoa == 1 or idade > maior_idade_homem:
            maior_idade_homem = idade
            nome_homem_mais_velho = nome

    # Conta mulheres com menos de 20
    if sexo == 'F' and idade < 20:
        total_mulheres_menos_20 += 1

# ===============================
# Saída
# ===============================

media_idade = soma_idade / 4

print('-' * 40)
print(f'Média de idade do grupo: {media_idade:.1f} anos')
print(f'Homem mais velho: {nome_homem_mais_velho} ({maior_idade_homem} anos)')
print(f'Mulheres com menos de 20 anos: {total_mulheres_menos_20}')
print('-' * 40)

"""
Exercício 049 - Média de Notas

Este programa calcula a média de um aluno e informa sua situação.

------------------------------------------
Critérios:
- Média abaixo de 5.0 → REPROVADO
- Média entre 5.0 e 6.9 → RECUPERAÇÃO
- Média 7.0 ou superior → APROVADO
------------------------------------------
"""

# ===============================
# Entrada de dados
# ===============================

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

# ===============================
# Processamento
# ===============================

media = (nota1 + nota2) / 2

# ===============================
# Saída
# ===============================

print('-' * 40)
print(f'Suas notas foram {nota1:.2f} e {nota2:.2f}')
print(f'Média final: {media:.2f}')
print('-' * 40)

if media < 5.0:
    print('Aluno REPROVADO.')

elif 5.0 <= media < 7.0:
    print('Aluno em RECUPERAÇÃO. Estude um pouco mais.')

else:
    print('Aluno APROVADO. Parabéns!')

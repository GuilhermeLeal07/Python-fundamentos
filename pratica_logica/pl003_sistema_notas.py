"""
Sistema de Notas do Aluno

Este sistema calcula a média de um aluno com base em 4 avaliações:
- 2 provas (Avaliação 1 e Avaliação 2)
- 2 trabalhos (Trabalho 1 e Trabalho 2)

A média final é calculada pela soma das 4 notas dividida por 4.

Regras de avaliação:
- Média maior ou igual a 6.0 → Aprovado
- Média entre 3.0 e 5.9 → Recuperação
- Média menor que 3.0 → Reprovado

O sistema também valida:
- Matrícula (somente números, até 10 dígitos)
- Notas (valores entre 0 e 10)

Ao final, exibe:
- Dados do aluno
- Média final
- Situação acadêmica
- Mensagem de desempenho
"""

# ======================
# ENTRADA
# ======================
nome = input('Digite o nome do aluno: ')
matricula = input('Digite a matrícula (somente números, até 10 dígitos): ')

av1 = float(input('Digite a nota da Avaliação 1: '))
av2 = float(input('Digite a nota da Avaliação 2: '))
trab1 = float(input('Digite a nota do Trabalho 1: '))
trab2 = float(input('Digite a nota do Trabalho 2: '))

# =======================
# PROCESSAMENTO DOS DADOS
# =======================
status = 'Válido'

# Validação da matrícula
if not matricula.isdigit() or len(matricula) > 10:
    status = 'Inválido'

# Validação das notas
elif (av1 < 0 or av1 > 10 or
      av2 < 0 or av2 > 10 or
      trab1 < 0 or trab1 > 10 or
      trab2 < 0 or trab2 > 10):
    status = 'Inválido'

else:
    media = (av1 + av2 + trab1 + trab2) / 4

    if media >= 6:
        situacao = 'Aprovado'
        mensagem = 'Parabéns! Você está aprovado!!!'

    elif media >= 3:
        situacao = 'Recuperação'
        mensagem = 'Você ainda pode melhorar. Continue se dedicando!'

    else:
        situacao = 'Reprovado'
        mensagem = 'REFORÇO NECESSÁRIO. Não desista, você pode evoluir!'

# ======================
# SAÍDA
# ======================
print('\n===== RESULTADO =====')

if status == 'Inválido':
    print('Dados inválidos. Verifique as informações.')
else:
    print(f'Aluno: {nome}')
    print(f'Matrícula: {matricula}')
    print(f'Média: {media:.2f}')
    print(f'Situação: {situacao}')
    print(f'Mensagem: {mensagem}')

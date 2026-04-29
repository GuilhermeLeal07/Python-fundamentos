"""
Simulador de Empréstimo

Este sistema avalia se um empréstimo pode ser aprovado com base no salário do usuário.

Regra:
A parcela mensal NÃO pode ultrapassar 30% do salário!!!
"""

# ======================
# ENTRADA
# ======================
valor_emprestimo = float(input('Digite o valor do empréstimo: R$'))
salario = float(input('Digite o seu salário: R$'))
anos = int(input('Digite em quantos anos deseja pagar: '))

# ======================
# PROCESSAMENTO
# ======================
status = 'Válido'

if valor_emprestimo <= 0 or salario <= 0 or anos <= 0:
    status = 'Inválido'

else:
    parcelas = anos * 12
    valor_parcela = valor_emprestimo / parcelas

    limite = salario * 0.30  # 30% do salário

    if valor_parcela <= limite:
        aprovado = True
        mensagem = 'Empréstimo aprovado!'
    else:
        aprovado = False
        mensagem = 'Empréstimo não aprovado. Compromete muito sua renda.'

# ======================
# SAÍDA
# ======================
print('\n===== RESULTADO =====')

if status == 'Inválido':
    print('Dados inválidos. Verifique as informações.')
else:
    print(f'Valor do empréstimo: R${valor_emprestimo:.2f}')
    print(f'Salário: R${salario:.2f}')
    print(f'Parcelas: {parcelas}x')
    print(f'Valor da parcela: R${valor_parcela:.2f}')
    print(f'Limite permitido (30%): R${limite:.2f}')

    if aprovado:
        print('Status: APROVADO!!!')
    else:
        print('Status: NEGADO')

    print(f'Mensagem: {mensagem}')

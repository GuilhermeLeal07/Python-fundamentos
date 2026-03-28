"""
Simulador de Financiamento (com amortização simples)

Este sistema calcula o valor total de um financiamento e permite simular antecipação de parcelas com desconto.

Regras:
- Prazo máximo: 35 anos
- Parcela não pode ultrapassar 30% do salário
"""

# ======================
# ENTRADA
# ======================
valor_imovel = float(input('Digite o valor do imóvel: R$'))
salario = float(input('Digite o seu salário: R$'))
anos = int(input('Digite em quantos anos deseja financiar: '))
juros_anual = float(input('Digite a taxa de juros anual (%): '))

# ======================
# PROCESSAMENTO
# ======================
status = 'Válido'

if valor_imovel <= 0 or salario <= 0 or anos <= 0 or juros_anual < 0:
    status = 'Inválido'

elif anos > 35:
    status = 'Inválido'

else:
    meses = anos * 12

    # juros simples
    juros_total = valor_imovel * (juros_anual / 100) * anos
    valor_total = valor_imovel + juros_total

    parcela = valor_total / meses
    limite = salario * 0.30

    if parcela <= limite:
        aprovado = True
        mensagem = 'Financiamento aprovado! 🏠'
    else:
        aprovado = False
        mensagem = 'Financiamento não aprovado. Parcela muito alta para sua renda.'

# ======================
# SAÍDA
# ======================
print('\n===== SIMULAÇÃO =====')

if status == 'Inválido':
    print('Dados inválidos.')
else:
    print(f'Valor do imóvel: R${valor_imovel:.2f}')
    print(f'Total de juros: R${juros_total:.2f}')
    print(f'Valor total a pagar: R${valor_total:.2f}')
    print(f'Parcelas: {meses}x de R${parcela:.2f}')
    print(f'Limite permitido (30% do salário): R${limite:.2f}')

    if aprovado:
        print('Status: APROVADO')
    else:
        print('Status: NEGADO')

    print(f'Mensagem: {mensagem}')

# =============================
# AMORTIZAÇÃO (SÓ SE APROVADO)
# =============================
if status == 'Válido':
    if aprovado:

        print('\nDeseja antecipar parcelas?')
        print('[1] Sim')
        print('[2] Não')

        opcao = input('Escolha: ')

        if opcao == '1':
            qtd = int(input('Quantas parcelas deseja adiantar? '))

            if qtd > 0 and qtd <= meses:
                valor_adiantado = parcela * qtd

                # desconto simples de 10%
                desconto = valor_adiantado * 0.10
                valor_final = valor_adiantado - desconto

                print('\n===== AMORTIZAÇÃO =====')
                print(f'Parcelas antecipadas: {qtd}')
                print(f'Valor sem desconto: R${valor_adiantado:.2f}')
                print(f'Desconto: R${desconto:.2f}')
                print(f'Valor final para antecipação: R${valor_final:.2f}')

            else:
                print('Quantidade inválida de parcelas.')

        elif opcao == '2':
            print('Nenhuma antecipação realizada.')

        else:
            print('Opção inválida.')

    else:
        print('\nFinanciamento não aprovado. Simulação encerrada.')

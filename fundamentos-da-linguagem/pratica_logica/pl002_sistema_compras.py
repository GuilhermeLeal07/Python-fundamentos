"""
Sistema de Compras
Descontos, cupons e forma de pagamento
"""

# =============================
# ENTRADA DO VALOR DA COMPRA
# =============================
valor = float(input('Digite o valor da compra: R$'))

print('\nEscolha a forma de pagamento:')
print('[1] À vista')
print('[2] Cartão')

opcao = input('Digite a opção: ')

# ============================
# ANÁLISE DO DESCONTO
# ============================
if valor < 0:
    status = 'Inválido'

else:
    if opcao == '1':
        forma_pagamento = 'À vista'

        if valor <= 100:
            desconto_percentual = 0.05
            cupom = 0
            mensagem = 'Compra realizada com sucesso! Volte sempre!'

        elif valor <= 500:
            desconto_percentual = 0.10
            cupom = 5
            mensagem = 'Ótima compra! Você ganhou um cupom de 5% para a próxima compra!'

        else:
            desconto_percentual = 0.15
            cupom = 10
            mensagem = 'Parabéns! Você ganhou um cupom de 10% para a próxima compra!'

    elif opcao == '2':
        forma_pagamento = 'Cartão'
        desconto_percentual = 0
        cupom = 0
        mensagem = 'Pagamento no cartão realizado com sucesso!'

    else:
        status = 'Inválido'

    # Só calcula se a opção for válida
    if opcao in ['1', '2']:
        desconto = valor * desconto_percentual
        valor_final = valor - desconto
        status = 'Válido'

# ======================
# SAÍDA
# ======================
print('\n===== RESULTADO =====')

if status == 'Inválido':
    print('Dados inválidos. Tente novamente.')
else:
    print(f'Valor da compra: R${valor:.2f}')
    print(f'Forma de pagamento: {forma_pagamento}')
    print(f'Valor final: R${valor_final:.2f}')

    if opcao == '1' and cupom > 0:
        print(f'Você recebeu um cupom de {cupom}% para a próxima compra!')

    print(mensagem)

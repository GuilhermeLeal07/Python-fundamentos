"""
Exercício 053 - Sistema de Pagamento

Este programa calcula o valor final de uma compra
com base na forma de pagamento escolhida.

------------------------------------------
Opções:
1 - À vista (dinheiro/cheque): 10% de desconto
2 - À vista no cartão: 5% de desconto
3 - Em até 2x no cartão: preço normal
4 - 3x ou mais no cartão: 20% de juros
------------------------------------------
"""

# ===============================
# Entrada de dados
# ===============================

print('=' * 40)
print('LOJA LEAL'.center(40))
print('=' * 40)

preco = float(input('Preço das compras: R$ '))

print('\nFormas de pagamento:')
print('[1] À vista dinheiro/cheque (10% desconto)')
print('[2] À vista no cartão (5% desconto)')
print('[3] 2x no cartão (sem juros)')
print('[4] 3x ou mais no cartão (20% juros)')

opcao = int(input('Escolha a opção: '))

# ===============================
# Processamento
# ===============================

print('-' * 40)

if opcao == 1:
    total = preco * 0.90
    print('Pagamento à vista com 10% de desconto.')

elif opcao == 2:
    total = preco * 0.95
    print('Pagamento à vista no cartão com 5% de desconto.')

elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'Pagamento em 2x de R${parcela:.2f} sem juros.')

elif opcao == 4:
    total = preco * 1.20
    parcelas = int(input('Quantas parcelas? '))
    parcela = total / parcelas
    print(f'Pagamento em {parcelas}x de R${parcela:.2f} com juros.')

else:
    print('Opção inválida.')
    total = preco

# ===============================
# Saída
# ===============================

print('-' * 40)
print(f'Valor final da compra: R${total:.2f}')
print('-' * 40)

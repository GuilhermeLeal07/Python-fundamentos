"""
Exercício 079 - Análise de Compras

Este programa lê o nome e o preço de vários produtos.
Ao final, informa:
- Total gasto na compra
- Quantos produtos custam mais de R$1000
- Qual é o produto mais barato
"""

# ===============================
# Inicialização
# ===============================

total_compra = 0
total_acima_1000 = 0
menor_preco = 0
produto_mais_barato = ''
quantidade_produtos = 0

# ===============================
# Loop principal
# ===============================

while True:
    print('-' * 40)
    print('CADASTRO DE PRODUTO')
    print('-' * 40)

    produto = input('Nome do produto: ').strip()
    preco = float(input('Preço: R$ '))

    quantidade_produtos += 1
    total_compra += preco

    if preco > 1000:
        total_acima_1000 += 1

    if quantidade_produtos == 1 or preco < menor_preco:
        menor_preco = preco
        produto_mais_barato = produto

    resposta = ''
    while resposta not in ['S', 'N']:
        resposta = input('Quer continuar? [S/N]: ').strip().upper()[0]

    if resposta == 'N':
        break

# ===============================
# Saída
# ===============================

print('\n' + '=' * 40)
print('RESUMO DA COMPRA')
print('=' * 40)

print(f'Total gasto: R$ {total_compra:.2f}')
print(f'Produtos acima de R$1000: {total_acima_1000}')
print(f'Produto mais barato: {produto_mais_barato} (R$ {menor_preco:.2f})')

print('=' * 40)

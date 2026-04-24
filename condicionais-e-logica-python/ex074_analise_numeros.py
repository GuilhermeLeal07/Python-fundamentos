"""
Exercício 074 - Análise de Números

Este programa lê vários números inteiros e:
- Calcula a média
- Identifica o maior e o menor valor
O usuário decide quando parar a execução.
"""

# ===============================
# Inicialização
# ===============================

resposta = 'S'
soma = 0
quantidade = 0

# ===============================
# Entrada e processamento
# ===============================

while resposta == 'S':
    numero = int(input('Digite um número: '))
    
    soma += numero
    quantidade += 1

    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    resposta = input('Quer continuar? [S/N] ').strip().upper()[0]

# ===============================
# Saída
# ===============================

media = soma / quantidade

print('-' * 40)
print(f'Quantidade de números digitados: {quantidade}')
print(f'Média: {media:.2f}')
print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')
print('-' * 40)

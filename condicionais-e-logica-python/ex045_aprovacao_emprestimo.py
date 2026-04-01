"""
Exercício 045 - Aprovação de Empréstimo

Este programa analisa se um empréstimo pode ser aprovado com base no salário do comprador.

Regra:
- A prestação mensal NÃO pode ultrapassar 30% do salário.
------------------------------------------
Fluxo:
1. Usuário informa:
   - valor da casa
   - salário
   - tempo de pagamento
2. O sistema calcula a prestação mensal
3. Compara com o limite permitido
------------------------------------------
"""

# ===============================
# Entrada de dados
# ===============================

valor_casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))

# ===============================
# Processamento
# ===============================

prestacao = valor_casa / (anos * 12)
limite = salario * 0.30

# ===============================
# Saída de dados
# ===============================

print('-' * 40)
print(f'Para pagar uma casa de R${valor_casa:.2f} em {anos} anos:')
print(f'A prestação será de R${prestacao:.2f}')
print(f'Limite permitido: R${limite:.2f}')
print('-' * 40)

if prestacao <= limite:
    print('Empréstimo APROVADO')
else:
    print('Empréstimo NEGADO')

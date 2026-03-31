"""
Este arquivo explora o uso do laço 'while' em Python.

Diferença principal:
- for → quando sabemos o limite
- while → quando NÃO sabemos o limite

------------------------------------------
DESAFIO:
1. Peça números até o usuário digitar 0
2. Mostre:
   - Quantos números foram digitados
   - Quantos são pares
   - Quantos são ímpares
------------------------------------------
"""

# ==========================================
# 1. Contagem simples com while
# ==========================================

print('Contagem de 1 até 9:')
c = 1
while c < 10:
    print(c)
    c += 1
print('-=-' * 15)

# ==========================================
# 2. Entrada até condição de parada
# ==========================================

print('Digite valores (0 para parar):')
numero = 1

while numero != 0:
    numero = int(input('Digite um valor: '))

print('Programa encerrado')
print('-=-' * 15)

# ==========================================
# 3. Sistema com pergunta de continuação
# ==========================================

resposta = 'S'

while resposta == 'S':
    valor = int(input('Digite um valor: '))
    resposta = input('Quer continuar? [S/N] ').strip().upper()

print('Fim do sistema')
print('-=-' * 15)

# ==========================================
# 4. DESAFIO
# ==========================================

contador = 0
pares = 0
impares = 0

print('Digite números para fazer a análise.')
print('Digite 0 para encerrar e ver o resultado.')
print('-' * 40)

while True:
    n = int(input('Digite um número: '))
    
    if n == 0:
        print('\nEncerrando análise...')
        break
    
    contador += 1
    
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

print('-' * 40)
print('\nRESULTADO DA ANÁLISE')
print(f'Total de números digitados: {contador}')
print(f'Quantidade de números pares: {pares}')
print(f'Quantidade de números ímpares: {impares}')
print('-' * 40)

"""
Exemplo 044 - Interrupção de Laços (break)

Este arquivo explora o uso do 'break' dentro de laços while.

O 'break' é usado para interromper um laço antes da condição final.

------------------------------------------
Exemplo:
- O programa pede números ao usuário
- A execução continua até um valor específico ser digitado
- Quando esse valor aparece, o laço é encerrado
------------------------------------------
"""

# ===============================
# Soma com condição de parada
# ===============================

print('Digite números para somar.')
print('Digite 999 para encerrar e ver o resultado.')
print('-' * 40)

soma = 0

while True:
    numero = int(input('Digite um número: '))
    
    if numero == 999:
        print('\nEncerrando operação...')
        break
    
    soma += numero

print('-' * 40)
print('RESULTADO DA SOMA')
print(f'Soma total dos valores: {soma}')
print('-' * 40)

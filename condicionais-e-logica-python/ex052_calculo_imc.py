"""
Exercício 052 - Cálculo de IMC

Este programa calcula o Índice de Massa Corporal (IMC)
e informa a classificação do usuário.

------------------------------------------
Classificação:
- Abaixo de 18.5 → Abaixo do peso
- 18.5 até 24.9 → Peso ideal
- 25 até 29.9 → Sobrepeso
- 30 até 39.9 → Obesidade
- 40 ou mais → Obesidade mórbida
------------------------------------------
"""

# ===============================
# Entrada de dados
# ===============================

peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))

# ===============================
# Processamento
# ===============================

imc = peso / (altura ** 2)

# ===============================
# Saída
# ===============================

print('-' * 40)
print(f'Seu IMC é: {imc:.2f}')
print('-' * 40)

if imc < 18.5:
    print('Classificação: Abaixo do peso')

elif imc < 25:
    print('Classificação: Peso ideal')

elif imc < 30:
    print('Classificação: Sobrepeso')

elif imc < 40:
    print('Classificação: Obesidade')

else:
    print('Classificação: Obesidade mórbida')

print('-' * 40)

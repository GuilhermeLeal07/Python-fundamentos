"""
Calculadora de IMC

Este sistema calcula o Índice de Massa Corporal (IMC) com base no peso e altura do usuário, exibindo a classificação e uma mensagem orientativa.
"""

# ======================
# ENTRADA
# ======================
peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))

# ======================
# PROCESSAMENTO
# ======================
status = 'Válido'

# --- Validação ---
if peso <= 0 or altura <= 0:
    status = 'Inválido'

else:
    imc = peso / (altura ** 2)

    if imc < 18.5:
        classificacao = 'Abaixo do peso'
        mensagem = 'Atenção! Procure orientação para melhorar sua saúde.'

    elif imc < 25:
        classificacao = 'Peso normal'
        mensagem = 'Tudo certo! Continue mantendo hábitos saudáveis.'

    elif imc < 30:
        classificacao = 'Sobrepeso'
        mensagem = 'Fique atento! Pequenas mudanças já fazem diferença.'
    elif imc < 35:
        classificacao = 'Obesidade grau 1'
        mensagem = 'É importante cuidar da saúde. Procure orientação.'

    elif imc < 40:
        classificacao = 'Obesidade grau 2'
        mensagem = 'Atenção redobrada! Busque acompanhamento profissional.'

    else:
        classificacao = 'Obesidade grau 3'
        mensagem = 'Risco elevado! Procure ajuda médica com urgência!!!'

# ======================
# SAÍDA
# ======================
print('\n===== RESULTADO =====')

if status == 'Inválido':
    print('DADOS INVÁLIDOS. VERIFIQUE PESO E ALTURA.')
else:
    print(f'Peso: {peso:.1f} kg')
    print(f'Altura: {altura:.2f} m')
    print(f'IMC: {imc:.2f}')
    print(f'Classificação: {classificacao}')
    print(f'Mensagem: {mensagem}')

"""
Sistema de Multa
Versão 2 - Lógica com classificação e mensagens
"""

# ======================
# ENTRADA
# ======================
velocidade = float(input('Digite a velocidade do veículo (km/h): '))

# ======================
# PROCESSAMENTO
# ======================
limite = 80

if velocidade <= limite:
    status = 'Dentro do limite'
else:
    excesso = velocidade - limite

    if excesso <= 10:
        infracao = 'Leve'
        base = 50
        valor_km = 5
        mensagem = 'Atenção! Você está próximo do limite. Dirija com mais cuidado.'

    elif excesso <= 20:
        infracao = 'Média'
        base = 100
        valor_km = 7
        mensagem = 'Cuidado! Você está acima do limite seguro. Reduza a velocidade.'

    else:
        infracao = 'Grave'
        base = 200
        valor_km = 10
        mensagem = 'Perigo! Velocidade muito acima do permitido. Dirija com responsabilidade!'

    multa = base + (excesso * valor_km)
    status = 'Multado'

# ======================
# SAÍDA
# ======================
print('\n===== RESULTADO =====')

if status == 'Dentro do limite':
    print('Você está dentro do limite permitido.')
else:
    print('Você foi multado!')
    print(f'Velocidade: {velocidade:.1f} km/h')
    print(f'Excesso: {excesso:.1f} km/h')
    print(f'Infração: {infracao}')
    print(f'Multa total: R${multa:.2f}')
    print(f'Mensagem: {mensagem}')

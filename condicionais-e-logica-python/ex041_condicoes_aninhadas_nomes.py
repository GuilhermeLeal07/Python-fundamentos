# Exercício 040 - Condições Aninhadas
# ==========================================

"""
Exemplo didático de estrutura condicional:

if carro.esquerda():
    carro.direita()
elif carro.direita():
    carro.siga()
else:
    carro.siga()
"""

nome = input('Qual é seu nome? ').strip().title()

if nome == 'Guilherme':
    mensagem = 'Nome bonito!!'
elif nome in ['Pedro', 'Maria', 'Joao']:
    mensagem = 'Seu nome é bem popular no Brasil!'
elif nome in ['Ana', 'Claudia', 'Jessica', 'Juliana']:
    mensagem = 'Belo nome feminino!'
else:
    mensagem = 'Seu nome é bem normal.'

print(mensagem)
print(f'Tenha um bom dia, {nome}!')

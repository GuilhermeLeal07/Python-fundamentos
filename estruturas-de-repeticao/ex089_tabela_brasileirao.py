"""
Ex089 - Análise da tabela do Brasileirão utilizando tuplas

Neste exercício, utilizamos uma tupla para armazenar os times do Campeonato Brasileiro em ordem de classificação.

O programa realiza:

- Exibição dos primeiros colocados
- Exibição dos últimos colocados
- Ordenação alfabética
- Busca pela posição de um time específico

Conceitos trabalhados:

- Tuplas
- Fatiamento de tuplas
- Função sorted()
- Método index()
- Manipulação de dados

O objetivo é desenvolver habilidades de consulta e organização de informações em estruturas imutáveis.
"""

# Tupla com os times
times = (
    'Botafogo', 'Palmeiras', 'Flamengo', 'Grêmio', 'Fluminense',
    'Athletico-PR', 'Bragantino', 'Fortaleza', 'São Paulo', 'Cuiabá',
    'Cruzeiro', 'Internacional', 'Corinthians', 'Santos',
    'Vasco da Gama', 'Bahia', 'Goiás', 'Coritiba',
    'América-MG', 'Chapecoense'
)

# Saída
print('=-' * 30)

print(f'Lista de times do Brasileirão:\n{times}')

print('=-' * 30)

# Os 5 primeiros colocados
print(f'Os 5 primeiros são: {times[:5]}')

# Os 4 últimos colocados
print(f'Os 4 últimos são: {times[-4:]}')

# Times em ordem alfabética
print(f'Times em ordem alfabética: {sorted(times)}')

# Posição da Chapecoense
posicao = times.index('Chapecoense') + 1

print(f'A Chapecoense está na {posicao}ª posição.')

print('=-' * 30)

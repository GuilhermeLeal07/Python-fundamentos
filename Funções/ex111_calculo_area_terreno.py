"""
Ex111 - Cálculo da área de um terreno

Neste exercício, criamos uma função chamada area() responsável por calcular a área de um terreno retangular.

O programa realiza:

- Leitura da largura do terreno
- Leitura do comprimento do terreno
- Cálculo da área
- Exibição do resultado

Conceitos trabalhados:

- Funções
- Parâmetros
- Variáveis locais
- Operações matemáticas
- Organização do código

O objetivo é aprender a criar funções para reutilizar tarefas específicas.
"""

def area(largura, comprimento):
    area_total = largura * comprimento

    print(
        f'A área de um terreno '
        f'{largura}m x {comprimento}m '
        f'é de {area_total:.2f}m².')

print(' Controle de Terrenos ')
print('-' * 25)

largura = float(input('LARGURA (m): '))

comprimento = float(input('COMPRIMENTO (m): '))

area(largura, comprimento)

"""
Exercício 051 - Analisador de Triângulos

Este programa verifica se três segmentos podem formar um triângulo
e, caso possam, informa o tipo do triângulo.

------------------------------------------
Tipos:
- Equilátero → todos os lados iguais
- Isósceles → dois lados iguais
- Escaleno → todos os lados diferentes
------------------------------------------
"""

# ===============================
# Entrada de dados
# ===============================

print('Analisador de Triângulos')
print('-' * 40)

lado1 = float(input('Digite o primeiro lado: '))
lado2 = float(input('Digite o segundo lado: '))
lado3 = float(input('Digite o terceiro lado: '))

# ===============================
# Verificação de formação
# ===============================

print('-' * 40)

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    
    print('Os segmentos PODEM formar um triângulo.')

    # ===============================
    # Classificação do triângulo
    # ===============================

    if lado1 == lado2 == lado3:
        print('Tipo: EQUILÁTERO')

    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('Tipo: ISÓSCELES')

    else:
        print('Tipo: ESCALENO')

else:
    print('Os segmentos NÃO podem formar um triângulo.')

print('-' * 40)

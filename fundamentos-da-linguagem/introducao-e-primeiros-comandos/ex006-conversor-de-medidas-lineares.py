"""
Aqui farei um teste para praticar meus conhecimentos, farei um Conversor de Medidas.

Objetivo:
Ler um valor em metros e converter para outras unidades de medida.
"""

metro = float(input("Digite um valor em metro: "))

# Medidas que usarei será o cm, mm e Km
quilometro = metro / 1000
hectômetro = metro / 100
decâmetro = metro / 10
# --METRO--
decímetro = metro * 10  
centimetro = metro * 100
milimetro = metro * 1000

print("=" * 30)
print("RESULTADO DAS CONVERSÕES")
print("=" * 30)

print("Valor em metros: {}".format(metro))
print("Quilômetros: {:.3f}".format(quilometro))
print("Hectômetros: {:.3f}".format(hectômetro))
print("Decâmetros: {:.3f}".format(decâmetro))
print("Decímetros: {:.3f}".format(decímetro))
print("Centímetros: {:.3f}".format(centimetro))
print("Milímetros: {:.3f}".format(milimetro))

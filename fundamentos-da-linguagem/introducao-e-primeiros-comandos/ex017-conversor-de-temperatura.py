"""
Conversor de Temperatura

Objetivo:
Converter temperaturas entre Celsius, Fahrenheit e Kelvin.

--Fórmulas utilizadas:
  F = (°C × 9/5) + 32
  K = °C + 273.15
"""

# Entrada de dados
celsius = float(input("Digite a temperatura em °C: "))

# Conversões
fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

# Saída de dados
print("-" * 40)
print("{}°C equivalem a:".format(celsius))
print("{}°F (Fahrenheit)".format(fahrenheit))
print("{}K (Kelvin)".format(kelvin))
print("-" * 40)

# Conversão inversa: Fahrenheit → Celsius
fahrenheit_input = float(input("\nDigite uma temperatura em °F: "))
celsius_convertido = (fahrenheit_input - 32) * 5 / 9
print("{}°F equivalem a {:.2f}°C".format(fahrenheit_input, celsius_convertido))

# Conversão inversa: Kelvin → Celsius
kelvin_input = float(input("\nDigite uma temperatura em K: "))
celsius_convertido2 = kelvin_input - 273.15
print("{}K equivalem a {:.2f}°C".format(kelvin_input, celsius_convertido2))

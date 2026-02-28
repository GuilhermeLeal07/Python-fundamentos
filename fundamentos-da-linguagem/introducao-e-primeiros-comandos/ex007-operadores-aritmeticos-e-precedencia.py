"""
Operadores Aritméticos e Ordem de Precedência

Objetivo:
Explorar os principais operadores aritméticos do Python e compreender a ordem de precedência das operações matemáticas.
"""
""" 
  Operações Aritméticas. 
  + Adição 
  - Subtração 
  * Multiplição 
  / Divisão 
  ** Potênica 
  // Divisão Inteira 
  % resto da divisão 
  
  ========================== 
  OPERADORES ARITMÉTICOS 
  ========================== 
  """

a = 5
b = 2

print("Valores utilizados:")
print("a = {}".format(a))
print("b = {}".format(b))
print("-" * 30)

print("Operações Aritméticas:")
print("Soma (a + b): {}".format(a + b))
print("Subtração (a - b): {}".format(a - b))
print("Multiplicação (a * b): {}".format(a * b))
print("Divisão (a / b): {}".format(a / b))
print("Potência (a ** b): {}".format(a ** b))
print("Divisão inteira (a // b): {}".format(a // b))
print("Resto da divisão (a % b): {}".format(a % b))

""" 
  ORDEM DE PRECEDÊNCIA. 
  1- () 
  2- ** 
  3- *, /, //, % 
  4- +, -

"""
print("\n" + "=" * 30)
print("ORDEM DE PRECEDÊNCIA")
print("=" * 30)

print("1º -> Parênteses ()")
print("2º -> Potência **")
print("3º -> *, /, //, %")
print("4º -> +, -")

print("\nExemplos de precedência:")
print("5 + 3 * 2 = {}".format(5 + 3 * 2))
print("3 * 5 + 4 ** 2 = {}".format(3 * 5 + 4 ** 2))
print("3 * (5 + 4) ** 2 = {}".format(3 * (5 + 4) ** 2))

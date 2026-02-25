"""
Práticas Iniciais em Python

Conteúdos abordados:
- Uso da função print()
- Operações matemáticas simples
- Declaração de variáveis
- Entrada de dados com input()
- Exercícios básicos de fixação

"""

# ==============================
# 1. Primeiros passos com print
# ==============================

print("Hello, world!")  # Exibe uma mensagem na tela

print(7 + 3)  # Exibe o resultado de uma operação matemática

print("Resultado da operação:", 7 + 3)  # Texto + valor numérico


# ==============================
# 2. Trabalhando com variáveis
# ==============================

nome = "Leal"
idade = 23
peso = 91

print("Nome:", nome)
print("Idade:", idade)
print("Peso:", peso)


# ==============================
# 3. Entrada de dados com input
# ==============================

nome = input("Qual é seu nome? ")
idade = input("Quantos anos você tem? ")
peso = input("Quanto você pesa? ")

print("Dados informados:")
print("Nome:", nome)
print("Idade:", idade)
print("Peso:", peso)


# ======================================
# Exercício 01 - Saudação personalizada
# ======================================

nome = input("Digite seu nome: ")
print("Olá", nome, "! Prazer em te conhecer.")


# ======================================
# Exercício 02 - Data de nascimento
# ======================================

dia = input("Que dia você nasceu? ")
mes = input("Que mês você nasceu? ")
ano = input("Que ano você nasceu? ")

print("Você nasceu no dia", dia, "de", mes, "de", ano + ". Correto?")


# ======================================
# Exercício 03 - Soma entre dois números
# ======================================

print("Vamos realizar uma soma simples.")

numero01 = float(input("Digite o primeiro número: "))
numero02 = float(input("Digite o segundo número: "))

resultado = numero01 + numero02

print("O resultado da soma é:", resultado)

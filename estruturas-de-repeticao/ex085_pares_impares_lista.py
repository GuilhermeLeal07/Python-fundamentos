"""
O que é uma Função?

Uma função é um bloco de código reutilizável que executa uma tarefa específica.
Ela serve para organizar, reutilizar e facilitar a manutenção do código.

Em resumo:

👉 “Função é um mini-programa dentro do seu programa.”

🔹 Estrutura básica de uma função
def nome_da_funcao(parametros):
    #  bloco de código
    return valor

Exemplo:
def saudacao():
    print("Olá, seja bem-vindo(a)!")


Para executar a função:

saudacao()

🔹 Funções com parâmetros

Você pode enviar dados para dentro da função por meio dos parâmetros:

def cumprimentar(nome):
    print(f"Olá, {nome}! Tudo bem?")

cumprimentar("Guilherme")
# Saída: Olá, Guilherme! Tudo bem?

🔹 Funções com retorno (return)

O return envia um resultado de volta para quem chamou a função.

def soma(a, b):
    return a + b

resultado = soma(5, 3)
print(resultado)  # 8


💡 Sem return, a função retorna None (ou seja, nada).

🔹 Tipos de parâmetros

Python permite várias formas de definir parâmetros. Veja os principais:

1. Parâmetros padrão (default)
def apresentar(nome="Visitante"):
    print(f"Olá, {nome}!")

apresentar()          # Olá, Visitante!
apresentar("Maria")   # Olá, Maria!

2. Parâmetros nomeados

Você pode chamar os parâmetros pelo nome:

def criar_conta(nome, saldo):
    print(f"Conta criada para {nome} com saldo de R${saldo}")

criar_conta(saldo=500, nome="João")

3. Parâmetros variáveis (*args e **kwargs)
🔸 *args → vários valores (tupla)
def somar_tudo(*numeros):
    return sum(numeros)

print(somar_tudo(1, 2, 3, 4))  # 10

🔸 **kwargs → vários pares chave=valor (dicionário)
def exibir_info(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

exibir_info(nome="Guilherme", idade=20, curso="Computação")

🔹 Escopo de variáveis (local x global)
Variável local

Existe só dentro da função:

def exemplo():
    x = 10
    print(x)

exemplo()
# print(x)  # ❌ erro, variável não existe fora da função

Variável global

Pode ser acessada de qualquer lugar:

x = 100

def mostrar():
    print(x)  # acessa variável global

mostrar()  # 100

🔹 Função dentro de função (aninhada)
def externa():
    def interna():
        print("Função interna chamada!")
    interna()

externa()

🔹 Funções lambda (anônimas)

São funções pequenas e rápidas — úteis quando você precisa de algo simples e direto.

quadrado = lambda x: x * x
print(quadrado(5))  # 25


⚡ Usadas muito com map(), filter(), e sorted().

🔹 Exemplo prático real

Um pequeno programa que calcula médias:

def calcular_media(*notas):
    media = sum(notas) / len(notas)
    return media

def verificar_aprovacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

# Programa principal
media_final = calcular_media(8, 6, 9)
situacao = verificar_aprovacao(media_final)

print(f"Média: {media_final:.1f} - {situacao}")

🔹 Resumo técnico (nível sênior)
Conceito	Explicação	Exemplo
def	Define a função	def soma(a,b): return a+b
Parâmetro	Entrada da função	(a,b)
return	Envia resultado de volta	return resultado
*args	Parâmetros variáveis (tupla)	def f(*args): ...
**kwargs	Parâmetros nomeados (dicionário)	def f(**kwargs): ...
Escopo	Local ou global	x dentro ou fora da função
Lambda	Função curta e anônima	lambda x: x*2

Quer que eu te mostre agora como criar e usar funções em um programa maior (como um mini-sistema com menu interativo) para você ver o uso real delas na prática?

Você disse:
Sim
O ChatGPT disse:

Excelente, Guilherme! 👏
Agora vamos colocar tudo isso em prática com um exemplo real de uso de funções em um mini-sistema interativo — do jeito que um desenvolvedor Python Sênior estruturaria.

💻 Projeto: Sistema simples de controle de alunos

Esse sistema vai:

Cadastrar alunos

Mostrar a lista de alunos

Calcular média das notas

Encerrar o programa

Tudo será feito com funções bem organizadas, para mostrar na prática como modularizar o código.

🔹 Código completo e comentado
# ----------------------------
# SISTEMA DE CONTROLE DE ALUNOS
# ----------------------------

alunos = []  # Lista global que armazena os cadastros


# Função 1 → Cadastrar um novo aluno
def cadastrar_aluno():
    nome = input("Nome do aluno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = calcular_media(nota1, nota2)

    aluno = {
        "nome": nome,
        "nota1": nota1,
        "nota2": nota2,
        "media": media
    }

    alunos.append(aluno)
    print(f"\n✅ Aluno {nome} cadastrado com sucesso!\n")


# Função 2 → Calcular média de notas (função auxiliar)
def calcular_media(n1, n2):
    return (n1 + n2) / 2


# Função 3 → Listar todos os alunos cadastrados
def listar_alunos():
    if not alunos:
        print("\n⚠️ Nenhum aluno cadastrado ainda.\n")
        return

    print("\n------ LISTA DE ALUNOS ------")
    for aluno in alunos:
        print(f"Nome: {aluno['nome']}")
        print(f"Notas: {aluno['nota1']}, {aluno['nota2']}")
        print(f"Média: {aluno['media']:.1f}")
        print("------------------------------")
    print()


# Função 4 → Menu principal
def menu():
    while True:
        print("===== MENU PRINCIPAL =====")
        print("[1] Cadastrar aluno")
        print("[2] Listar alunos")
        print("[3] Sair")
        print("==========================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            print("\n👋 Encerrando o sistema... Até logo!")
            break
        else:
            print("\n❌ Opção inválida! Tente novamente.\n")


# Execução do programa
menu()

🔹 Estrutura Profissional do Código
    Parte	            Função	            Descrição
--------------------------------------------------------------------------------
cadastrar_aluno()   Entrada de dados	Recebe nome e notas
calcular_media()	Lógica de cálculo	Faz a média das notas
listar_alunos()	    Saída de dados	    Mostra todos os alunos cadastrados
menu()          	Controle	        Gerencia as opções do sistema
alunos          	Lista global	    Armazena os cadastros em dicionários

"""
#======================================================================================================
"""
====================== 🧩 PARTE 2 — Funções e Documentação em Python =================================
🔹 1. A função help()

O help() é uma função interna do Python usada para exibir a documentação de qualquer função, objeto, classe, módulo, etc.

📘 Serve para aprender o que algo faz, seus parâmetros e retornos.

Exemplo:
help(print)


➡️ Vai mostrar na tela o que a função print() faz, seus argumentos (sep, end, etc.) e exemplos de uso.

🔹 2. O atributo __doc__

Toda função (ou objeto) em Python possui um atributo oculto chamado __doc__, que guarda a sua documentação interna.

Exemplo:
print(input.__doc__)


➡️ Isso exibe o texto explicativo da função input(), o mesmo que você veria com help(input).

🔹 3. Criando sua própria documentação (Docstrings)

Uma docstring (abreviação de “documentation string”) é uma string entre aspas triplas logo abaixo da definição da função.
Ela serve para explicar o que a função faz, seus parâmetros e o retorno.

🧠 Exemplo 1 — Função com docstring:
def saudacao(nome):

    Exibe uma mensagem de saudação personalizada.

    Parâmetros:
        nome (str): nome da pessoa a ser saudada.

    Retorno:
        None
    
    print(f"Olá, {nome}! Seja bem-vindo(a)!")


Agora você pode usar:

help(saudacao)


ou

print(saudacao.__doc__)


➡️ Ambos mostram o texto da docstring acima.

🔹 4. Retorno de valores (return)

A função return envia dados de volta para quem chamou a função.
Esse é o resultado da função.

Exemplo:
def quadrado(numero):
        Retorna o quadrado de um número.
    return numero ** 2

resultado = quadrado(5)
print(resultado)  # 25


➡️ Quando a função encontra return, ela para a execução e devolve o valor.

🧩 Exemplo 2 — Vários retornos
def dividir(a, b):
    
    Retorna o resultado e o resto da divisão entre dois números.
    
    quociente = a // b
    resto = a % b
    return quociente, resto  # Retorna uma tupla

resultado = dividir(10, 3)
print(resultado)        # (3, 1)
print(resultado[0])     # 3
print(resultado[1])     # 1

🔹 5. Tipagem e documentação (nível profissional)

Você pode especificar tipos de dados esperados e retornados, para facilitar leitura e evitar erros — isso se chama type hints.

def somar(a: int, b: int) -> int:
    
    Soma dois números inteiros.

    Args:
        a (int): primeiro número.
        b (int): segundo número.

    Returns:
        int: resultado da soma.
    
    return a + b

print(somar(10, 5))  # 15


💡 Isso não impede outros tipos (Python é dinâmico), mas ajuda IDEs e linters (como VSCode e PyCharm) a alertarem sobre erros.

🔹 6. Exemplo prático completo (com tudo junto)
def calcular_area(base: float, altura: float) -> float:
    
    Calcula a área de um retângulo.

    Parâmetros:
        base (float): valor da base do retângulo.
        altura (float): valor da altura do retângulo.

    Retorna:
        float: área calculada.
    
    return base * altura


# Exibindo documentação
help(calcular_area)
print(calcular_area.__doc__)

# Usando a função
area = calcular_area(5, 3)
print(f"A área é {area}")

🔹 7. Diferenças rápidas para lembrar
Conceito	Explicação	Exemplo
help()	Mostra a documentação do objeto	help(print)
__doc__	Mostra apenas o texto de ajuda da função	print(print.__doc__)
Docstring	Texto explicativo dentro da função	texto...
return	Envia o resultado de volta	return valor
Type hint	Indica tipo de parâmetro/retorno	def f(x: int) -> int:

"""

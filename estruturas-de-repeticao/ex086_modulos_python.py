"""
🧩 O que é Modulação em Python?

Modulação vem de "módulo", e significa dividir um programa grande em partes menores e mais organizadas, chamadas módulos.

👉 Em outras palavras:

É separar o código em arquivos diferentes, de modo que cada um tenha uma função específica.

🎯 Objetivo da Modulação

✅ Facilitar a leitura e manutenção do código.
✅ Permitir reaproveitar funções e classes em outros programas.
✅ Evitar repetição de código.
✅ Ajudar a organizar melhor projetos grandes.

💡 Exemplo prático — sem modulação

Veja esse código (todo em um arquivo só):

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

# Programa principal
print(somar(5, 2))
print(dividir(10, 2))


👀 Está tudo junto. Funciona, mas imagine se o programa tivesse 100 funções — ficaria uma bagunça.

🔹 Agora, com modulação (o jeito profissional)
🧱 Passo 1 — Criar um módulo

Crie um arquivo chamado operacoes.py
(coloque nesse arquivo as funções)

# operacoes.py

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

🧱 Passo 2 — Criar o programa principal

Crie outro arquivo chamado principal.py

# principal.py

import operacoes  # importa o módulo que criamos

print(operacoes.somar(5, 2))
print(operacoes.dividir(10, 2))


✅ Pronto!
Você separou a lógica das operações em um módulo próprio (operacoes.py)
e deixou o programa principal (principal.py) limpo e organizado.

📦 Entendendo o comando import
Comando	O que faz
import operacoes	Importa o módulo inteiro
from operacoes import somar	Importa apenas a função somar
from operacoes import *	Importa todas as funções do módulo
import operacoes as op	Importa o módulo e dá um apelido

💡 Exemplo:

import operacoes as op

print(op.somar(10, 5))

🔍 Onde os módulos ficam?

Python procura módulos em:

O mesmo diretório do arquivo principal.

As pastas padrão do Python (como site-packages, onde ficam bibliotecas instaladas com pip).

🧠 Docstrings e Módulos

Você pode documentar o módulo também!
Dentro de operacoes.py, adicione no topo:


Módulo operacoes
----------------
Fornece funções básicas de matemática:
- somar(a, b)
- subtrair(a, b)
- multiplicar(a, b)
- dividir(a, b)



E pode ver a documentação com:

import operacoes
help(operacoes)

📁 Estrutura de projeto profissional (exemplo)
meu_projeto/
│
├── principal.py
├── operacoes.py
├── calculadora/
│   ├── __init__.py
│   ├── basicas.py
│   └── avancadas.py
└── dados/
    ├── usuarios.json
    └── relatorios.txt


Assim, cada parte do projeto fica modularizada e independente.

🚀 Resumo
Conceito	Significado
Módulo	Arquivo .py com funções, classes ou variáveis
Modulação	Processo de dividir um programa em módulos
import	Traz funções de outros módulos
Vantagens	Organização, reutilização, clareza, manutenção fácil

Agora vamos dar um passo profissional — criar um pacote Python completo, igual aos que você instala com pip.

Isso é o nível acima da modulação, chamado de empacotamento ou estrutura de pacote.
Vamos ver tudo com explicações + exemplos práticos.

🧩 1️⃣ Relembrando

👉 Um módulo = um arquivo .py
👉 Um pacote = uma pasta com vários módulos + um arquivo especial chamado __init__.py

📁 2️⃣ Estrutura inicial do pacote

Vamos montar um projeto simples chamado “calculadora”.

meu_projeto/
│
├── principal.py
└── calculadora/
    ├── __init__.py
    ├── basicas.py
    └── avancadas.py

📘 3️⃣ Conteúdo dos arquivos
📄 basicas.py
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

📄 avancadas.py
def potencia(a, b):
    return a ** b

def fatorial(n):
    if n < 0:
        return "Erro: número negativo!"
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

📄 __init__.py

Esse arquivo indica ao Python que a pasta calculadora é um pacote.
Sem ele, a pasta seria apenas uma pasta comum.


Pacote Calculadora
------------------
Fornece funções matemáticas básicas e avançadas.

from .basicas import somar, subtrair, multiplicar, dividir
from .avancadas import potencia, fatorial


➡️ O from .basicas import ... quer dizer:

“Importe essas funções do módulo basicas.py que está na mesma pasta (por isso o ponto).”

📄 principal.py
from calculadora import somar, fatorial, potencia

print(somar(10, 5))         # 15
print(fatorial(5))          # 120
print(potencia(2, 3))       # 8

🔍 4️⃣ Como funciona

Quando você faz:

from calculadora import somar


O Python:

Vai até a pasta calculadora/

Encontra o arquivo __init__.py

Executa tudo que está dentro dele

Disponibiliza as funções importadas

📦 5️⃣ Pacotes dentro de pacotes (nível avançado)

Você pode ter algo assim:

meu_projeto/
└── calculadora/
    ├── __init__.py
    ├── basicas/
    │   ├── __init__.py
    │   ├── soma.py
    │   └── divisao.py
    └── avancadas/
        ├── __init__.py
        └── estatistica.py


E o Python entende tudo, se houver __init__.py nas pastas.

💬 6️⃣ Como testar no VS Code

Crie a estrutura de pastas exatamente assim.

Abra a pasta meu_projeto/ no VS Code (não só o arquivo).

Execute o principal.py normalmente (Ctrl + F5 ou python principal.py).

O Python encontrará o pacote calculadora automaticamente.

🧠 7️⃣ O que o __init__.py pode conter

Importações (como no exemplo)

Inicializações do pacote

Variáveis globais

Docstrings explicando o pacote

👉 Ele não precisa estar vazio — pode ser usado para organizar tudo o que o pacote exporta.

🚀 8️⃣ Resumo final
Conceito	Explicação
Módulo	Um único arquivo .py
Pacote	Uma pasta com vários módulos e __init__.py
Importação	from pacote import função
init.py	Diz ao Python que aquela pasta é um pacote
Vantagens	Organização, reutilização, fácil manutenção, escalabilidade
🔧 Extra

Se você quiser um toque profissional, pode adicionar no topo de cada módulo uma docstring de documentação:


Módulo basicas.py
-----------------
Contém funções matemáticas simples:
- somar(a, b)
- subtrair(a, b)
- multiplicar(a, b)
- dividir(a, b)


E no terminal, testar:

import calculadora
help(calculadora)
"""

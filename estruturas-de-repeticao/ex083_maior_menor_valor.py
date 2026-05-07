"""
    1. LISTAS COMPOSTAS

Uma lista composta é uma lista que contém outras listas dentro dela.
É como uma “tabela”, onde cada lista interna representa uma linha e cada elemento dessa lista representa uma coluna.

🔹 Exemplo básico
# Lista simples
pessoa1 = ["Ana", 25]
pessoa2 = ["Bruno", 30]

# Lista composta (lista de listas)
pessoas = [pessoa1, pessoa2]

print(pessoas)
# Saída: [['Ana', 25], ['Bruno', 30]]


    Explicando:

pessoas[0] → acessa ["Ana", 25]

pessoas[0][0] → acessa "Ana"

pessoas[0][1] → acessa 25

🔹 Acessando dados dentro de listas compostas
pessoas = [["Ana", 25], ["Bruno", 30], ["Carlos", 20]]

print(pessoas[1])     # ['Bruno', 30]
print(pessoas[1][0])  # Bruno
print(pessoas[2][1])  # 20

🔹 Adicionando e lendo dados de forma dinâmica
pessoas = []

for i in range(3):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    pessoas.append([nome, idade])

print(pessoas)


🔸 Se você digitar:

Ana
25
Bruno
30
Clara
20


🔸 O resultado será:

[['Ana', 25], ['Bruno', 30], ['Clara', 20]]

⚠️CUIDADO: cópia vs referência (isso é muito importante!)
dados = ["Ana", 25]
galera = []
galera.append(dados)

dados[0] = "Maria"
print(galera)
# ['Maria', 25]  <- mudou também!


👉 Isso acontece porque append() adicionou a referência, não uma cópia.

✅ Correto:

dados = ["Ana", 25]
galera = []
galera.append(dados[:])  # ou list(dados)
dados[0] = "Maria"
print(galera)
# [['Ana', 25]]

🔹 Percorrendo uma lista composta
galera = [["João", 19], ["Maria", 22], ["Pedro", 17]]

for pessoa in galera:
    print(f"{pessoa[0]} tem {pessoa[1]} anos.")


Saída:

João tem 19 anos.
Maria tem 22 anos.
Pedro tem 17 anos.

🔹 Filtrando dados
galera = [["João", 19], ["Maria", 22], ["Pedro", 17]]
maiores = []
menores = []

for p in galera:
    if p[1] >= 18:
        maiores.append(p)
    else:
        menores.append(p)

print("Maiores:", maiores)
print("Menores:", menores)

    2. USANDO LISTAS COM BIBLIOTECAS

Agora que você entende listas compostas, dá pra aproveitar bibliotecas (módulos) que trabalham com elas de forma mais prática e eficiente.

🔸 Biblioteca random

Permite gerar valores aleatórios e trabalhar com listas.

import random

numeros = [1, 2, 3, 4, 5, 6]
escolhido = random.choice(numeros)
print("Número sorteado:", escolhido)

# Embaralhar lista
random.shuffle(numeros)
print("Lista embaralhada:", numeros)

# Gerar lista de números aleatórios
aleatorios = random.sample(range(1, 61), 6)
print("Números da Mega-Sena:", aleatorios)

🔸 Biblioteca statistics

Perfeita para calcular média, mediana, moda, etc. de listas numéricas.

import statistics

notas = [7.5, 8.0, 9.2, 5.5, 8.8]

print("Média:", statistics.mean(notas))
print("Mediana:", statistics.median(notas))
print("Maior nota:", max(notas))
print("Menor nota:", min(notas))

🔸 Biblioteca math

Trabalha com operações matemáticas em listas.

import math

numeros = [4, 9, 16]
raizes = [math.sqrt(n) for n in numeros]
print(raizes)  # [2.0, 3.0, 4.0]

🔸 Biblioteca numpy (avançada)

É uma das mais usadas em Ciência de Dados e IA.
Ela transforma listas comuns em arrays numéricos, muito mais rápidos e poderosos.

import numpy as np

# Criar array a partir de lista
lista = [1, 2, 3, 4]
array = np.array(lista)

# Operações matemáticas vetorizadas (sem loop!)
print(array * 2)       # [2 4 6 8]
print(array + 10)      # [11 12 13 14]
print(array.mean())    # 2.5


✅ Dica: o numpy é o “melhor amigo” das listas numéricas grandes.

🔸 Biblioteca pandas (análise de dados)

Transforma listas compostas em tabelas (DataFrames), facilitando leitura e manipulação.

import pandas as pd

dados = [
    ["Ana", 25, "RJ"],
    ["Bruno", 30, "SP"],
    ["Carla", 22, "MG"]
]

df = pd.DataFrame(dados, columns=["Nome", "Idade", "Estado"])
print(df)


Saída:

    Nome  Idade Estado
0    Ana     25     RJ
1  Bruno     30     SP
2  Carla     22     MG


Você pode filtrar, ordenar e até exportar para Excel facilmente:

print(df[df["Idade"] > 25])   # Filtra maiores de 25
df.to_excel("pessoas.xlsx", index=False)

🔸 Biblioteca json (listas e dicionários)

Usada quando queremos salvar listas compostas em arquivos (como banco de dados simples).

import json

pessoas = [
    {"nome": "Ana", "idade": 25},
    {"nome": "Bruno", "idade": 30}
]

# Converter para JSON (texto)
json_data = json.dumps(pessoas, indent=4)
print(json_data)

# Salvar em arquivo
with open("pessoas.json", "w") as f:
    f.write(json_data)

# Ler de volta
with open("pessoas.json", "r") as f:
    dados = json.load(f)
print(dados)

🧠 Dica final: quando usar listas e quando NÃO usar

✅ Use listas quando:

Você precisa armazenar vários valores em ordem;

Vai adicionar, remover ou percorrer dados pequenos/médios;

Está estudando lógica e estruturas básicas.

❌ Prefira outras estruturas quando:

Precisa de buscas rápidas → use set ou dict;

Trabalha com grandes quantidades de números → use numpy;

Precisa de dados organizados em colunas/linhas → use pandas.
"""

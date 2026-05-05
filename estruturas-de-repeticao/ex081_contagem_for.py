"""
--- O que é uma Tupla em Python? ---

Uma tupla é uma estrutura de dados imutável em Python, muito parecida com uma lista.
A diferença principal é:

Lista → mutável (você pode adicionar, remover, alterar elementos).

Tupla → imutável (uma vez criada, não pode ser alterada).

Como criar uma tupla:
# Criando tuplas
tupla1 = (1, 2, 3)
tupla2 = ("Python", "Java", "C")
tupla3 = (10,)  # tupla de 1 elemento (precisa da vírgula)

--- Características principais ---

Imutável – Não dá para modificar depois de criada.

Indexada – Você acessa elementos por índice, como em listas.

Permite repetição – Pode ter valores duplicados.

Pode conter tipos diferentes – Ex: números, strings, listas dentro de uma mesma tupla.

--- Exemplos práticos ---
1. Acessando elementos
linguagens = ("Python", "C", "Java")

print(linguagens[0])  # Python
print(linguagens[-1]) # Java (último elemento)

2. Iterando sobre tupla
for linguagem in linguagens:
    print(linguagem)

3. Usando em unpacking (desempacotamento)

Muito usado quando uma função retorna vários valores.

def coordenadas():
    return (10, 20)

x, y = coordenadas()
print(x, y)  # 10 20

4. Tuplas dentro de listas (exemplo real de uso)
alunos = [("João", 20), ("Maria", 22), ("Pedro", 19)]

for nome, idade in alunos:
    print(f"{nome} tem {idade} anos")

5. Por que usar tuplas?

Segurança: garante que os dados não serão alterados sem querer.

Performance: tuplas são mais rápidas que listas em acesso.

Hashable: tuplas podem ser usadas como chaves em dicionários, listas não.

Exemplo:

localizacao = {}
localizacao[(10, 20)] = "Escola"
localizacao[(30, 40)] = "Hospital"

print(localizacao[(10, 20)])  # Escola


--- Resumo rápido: ---
Tupla é uma lista imutável. Boa quando você precisa garantir que os dados não mudem, quer mais performance ou precisa usar como chave em dicionário.

    MAS QUAL É A DIFERENÇA DE PERFORMACE E USO DE MEMÓRIA???
Então vamos fazer uma comparação prática entre Lista e Tupla em Python.

--- Comparação: Lista x Tupla ---
1. Criação de Lista e Tupla"""
--- O que é uma Tupla em Python? ---

Uma tupla é uma estrutura de dados imutável em Python, muito parecida com uma lista.
A diferença principal é:

Lista → mutável (você pode adicionar, remover, alterar elementos).

Tupla → imutável (uma vez criada, não pode ser alterada).

Como criar uma tupla:
# Criando tuplas
tupla1 = (1, 2, 3)
tupla2 = ("Python", "Java", "C")
tupla3 = (10,)  # tupla de 1 elemento (precisa da vírgula)

--- Características principais ---

Imutável – Não dá para modificar depois de criada.

Indexada – Você acessa elementos por índice, como em listas.

Permite repetição – Pode ter valores duplicados.

Pode conter tipos diferentes – Ex: números, strings, listas dentro de uma mesma tupla.

--- Exemplos práticos ---
1. Acessando elementos
linguagens = ("Python", "C", "Java")

print(linguagens[0])  # Python
print(linguagens[-1]) # Java (último elemento)

2. Iterando sobre tupla
for linguagem in linguagens:
    print(linguagem)

3. Usando em unpacking (desempacotamento)

Muito usado quando uma função retorna vários valores.

def coordenadas():
    return (10, 20)

x, y = coordenadas()
print(x, y)  # 10 20

4. Tuplas dentro de listas (exemplo real de uso)
alunos = [("João", 20), ("Maria", 22), ("Pedro", 19)]

for nome, idade in alunos:
    print(f"{nome} tem {idade} anos")

5. Por que usar tuplas?

Segurança: garante que os dados não serão alterados sem querer.

Performance: tuplas são mais rápidas que listas em acesso.

Hashable: tuplas podem ser usadas como chaves em dicionários, listas não.

Exemplo:

localizacao = {}
localizacao[(10, 20)] = "Escola"
localizacao[(30, 40)] = "Hospital"

print(localizacao[(10, 20)])  # Escola


--- Resumo rápido: ---
Tupla é uma lista imutável. Boa quando você precisa garantir que os dados não mudem, quer mais performance ou precisa usar como chave em dicionário.

    MAS QUAL É A DIFERENÇA DE PERFORMACE E USO DE MEMÓRIA???
Então vamos fazer uma comparação prática entre Lista e Tupla em Python.

--- Comparação: Lista x Tupla ---
1. Criação de Lista e Tupla
# Lista
lista = [1, 2, 3, 4, 5]

# Tupla
tupla = (1, 2, 3, 4, 5)

2. Verificando tamanho na memória
import sys

print("Tamanho da lista:", sys.getsizeof(lista), "bytes")
print("Tamanho da tupla:", sys.getsizeof(tupla), "bytes")


--- Normalmente a tupla ocupa menos memória que a lista, porque não precisa armazenar métodos de modificação. ---

3. Testando velocidade de acesso
import timeit

# Acesso por índice
tempo_lista = timeit.timeit(stmt="lista[3]", setup="lista=[1,2,3,4,5]", number=1_000_000)
tempo_tupla = timeit.timeit(stmt="tupla[3]", setup="tupla=(1,2,3,4,5)", number=1_000_000)

print("Tempo lista:", tempo_lista)
print("Tempo tupla:", tempo_tupla)


--- O acesso em tupla tende a ser mais rápido que em lista. ---

4. Mutabilidade na prática
# Lista pode ser alterada
lista[0] = 100
print("Lista alterada:", lista)

# Tupla não pode ser alterada
try:
    tupla[0] = 100
except TypeError as e:
    print("Erro:", e)


--- Listas são mutáveis, tuplas são imutáveis. ---

5. Quando usar cada uma?

✅ Lista: quando você precisa adicionar, remover ou alterar elementos.

✅ Tupla: quando os dados são fixos e não devem ser alterados (ex.: coordenadas, configurações, retornos de função).

--- Resumo técnico: ---

Tupla é mais leve e rápida.

Lista é mais flexível e dinâmica.

Use tupla quando precisa garantir integridade dos dados.

Use lista quando precisa de manipulação constante."""

# lanche = (TUPLA) [LISTA] {DICIONÁRIO}
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(sorted(lanche)) #o sorted mostra a tupla em ordem

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi muito!!')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi Muitoo!!!')

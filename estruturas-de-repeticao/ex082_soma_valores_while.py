"""
🧠 O que é uma lista em Python?

Uma lista é uma coleção de dados (valores, textos, números, etc.) armazenados em uma única variável.
Ela é mutável, ou seja, podemos alterar seus elementos — adicionar, remover, trocar, etc.

Sintaxe básica:

lista = [1, 2, 3, 4, 5]

🔹 Como acessar os itens

Cada item da lista tem uma posição (índice), começando em 0:

nomes = ["Ana", "Bruno", "Carlos"]
print(nomes[0])  # Exibe 'Ana'
print(nomes[2])  # Exibe 'Carlos'


Também é possível usar índices negativos:

print(nomes[-1])  # Exibe o último item ('Carlos')

🔹 Como adicionar itens
1. append() → adiciona no final:
frutas = ["maçã", "banana"]
frutas.append("laranja")
print(frutas)  # ['maçã', 'banana', 'laranja']

2. insert(posição, valor) → adiciona em uma posição específica:
frutas.insert(1, "uva")
print(frutas)  # ['maçã', 'uva', 'banana', 'laranja']

3. extend() → adiciona vários elementos de outra lista:
outras = ["pera", "manga"]
frutas.extend(outras)
print(frutas)  # ['maçã', 'uva', 'banana', 'laranja', 'pera', 'manga']

🔹 Como remover itens
1. remove(valor) → remove o primeiro valor encontrado:
frutas.remove("uva")
print(frutas)  # ['maçã', 'banana', 'laranja', 'pera', 'manga']

2. pop() → remove o último item (ou um índice específico):
frutas.pop()       # remove 'manga'
frutas.pop(1)      # remove o item da posição 1 ('banana')
print(frutas)      # ['maçã', 'laranja', 'pera']

3. del → apaga um item ou a lista toda:
del frutas[0]  # remove 'maçã'
print(frutas)  # ['laranja', 'pera']

# del frutas  # apaga toda a lista (cuidado!)

4. clear() → esvazia a lista:
frutas.clear()
print(frutas)  # []

🔹 Alterar valores

Você pode modificar diretamente um item pelo índice:

numeros = [10, 20, 30]
numeros[1] = 50
print(numeros)  # [10, 50, 30]

🔹 Outras operações úteis
Ver tamanho da lista:
len(numeros)  # retorna 3

Ordenar a lista:
numeros = [3, 1, 2]
numeros.sort()
print(numeros)  # [1, 2, 3]

Inverter a ordem:
numeros.reverse()
print(numeros)  # [3, 2, 1]

Ver se um valor está na lista:
if 2 in numeros:
    print("O número 2 está na lista!")

🔹 Exemplo completo prático
# Lista de compras
compras = ["pão", "leite", "café"]

# Adicionar itens
compras.append("açúcar")
compras.insert(1, "arroz")

# Remover item
compras.remove("pão")

# Alterar um item
compras[0] = "macarrão"

# Mostrar lista final
print(compras)
# Saída: ['macarrão', 'café', 'açúcar']

======================================================================================================
======================================================================================================

O QUE É UMA LISTA?

Uma lista é uma coleção ordenada e mutável de objetos. Pode conter qualquer tipo (int, str, float, outras listas, objetos, etc.).
Exemplo:

L = [10, "texto", 3.14, [1,2]]

-=-=-=- Criando listas -=-=-=-
vazia = []
lista = [1, 2, 3]
lista2 = list((4,5,6))      # a partir de um tuple
range_to_list = list(range(5))  # [0,1,2,3,4]
comprehension = [x*x for x in range(5)]  # [0,1,4,9,16]

Acessando elementos (indexação e slicing)

Índices começam em 0. L[0] é o primeiro.

Índices negativos: L[-1] é o último.

Slice: L[start:stop:step] (stop não incluído).

nomes = ["Ana","Beto","Carlos","Dani"]
print(nomes[1])    # 'Beto'
print(nomes[-1])   # 'Dani'
print(nomes[1:3])  # ['Beto','Carlos']
print(nomes[:])    # cópia superficial da lista
print(nomes[::-1]) # lista invertida

Modificar itens
nums = [10,20,30]
nums[1] = 200       # [10,200,30]

# substituição de fatia
nums[0:2] = [1,2,3] # agora [1,2,3,30]

# inserção por slice (posição específica)
nums[1:1] = ["x"]   # insere antes da posição 1

=== Métodos importantes (com exemplos) ===

append(x) — adiciona no fim.

extend(iterable) — acrescenta vários.

insert(i, x) — insere na posição i.

remove(x) — remove a primeira ocorrência (ValueError se não existir).

pop() / pop(i) — remove e retorna (sem índice remove último).

clear() — esvazia.

index(x) — posição da primeira ocorrência (ValueError se não existir).

count(x) — conta quantas vezes aparece.

sort() — ordena in-place.

sorted(lista) — retorna nova lista ordenada.

reverse() — inverte in-place.

copy() — cópia superficial.

frutas = ["maçã","banana"]
frutas.append("laranja")
frutas.extend(["uva","pera"])
frutas.insert(1,"mamão")   # insere
frutas.remove("uva")
ultimo = frutas.pop()      # 'pera'
print(frutas)

Iteração — formas comuns
for x in lista:
    print(x)

for i in range(len(lista)):       # menos preferido
    print(i, lista[i])

# melhor:
for i, x in enumerate(lista, start=0):
    print(i, x)

# iterar duas listas ao mesmo tempo
for a, b in zip(lista1, lista2):
    ...

Compreensão de listas (list comprehensions)

    --- Sintaxe poderosa e idiomática: ---

# todos os quadrados de 0..9
squares = [x*x for x in range(10)]

# com condição
evens = [x for x in range(20) if x % 2 == 0]

# condicional dentro (ternário)
labels = [("par" if x%2==0 else "ímpar") for x in range(6)]

# aninhado
pairs = [(i,j) for i in range(3) for j in range(2)]

Generator expressions (economia de memória)

=== Se não precisa da lista inteira: ===

gen = (x*x for x in range(1000000))
# use sum(gen) ou next(gen) etc. — não armazena todos os elementos

Cópias e referências — cuidado importante!

Listas guardam referências para objetos, não cópias automáticas.

a = [1,2,3]
b = a            # b e a referenciam a mesma lista
b.append(4)
print(a)         # [1,2,3,4]  <- mudança visível em a

# cópia superficial
c = a.copy()
d = list(a)


Shallow vs Deep copy:

copy() é superficial: se elementos são mutáveis (outras listas), ambos compartilham esses elementos internos.

Para copiar totalmente estruturas aninhadas use import copy; deep = copy.deepcopy(obj).

Exemplo do problema comum com multiplicação:

mat = [[0]*3]*3
# matriz parecerá ok, mas cada linha é a *mesma* lista (referência repetida).
mat[0][0] = 1
print(mat)  # [[1,0,0],[1,0,0],[1,0,0]]  <- bug!

# Correto:
mat2 = [[0]*3 for _ in range(3)]
mat2[0][0] = 1
print(mat2) # [[1,0,0],[0,0,0],[0,0,0]]

    --- Listas aninhadas (matrizes) ---

Acesse com mat[i][j] e crie com comprehension (veja acima). Para operações eficientes em matrizes grandes, considere numpy (biblioteca externa).

    --- Ordenação avançada ---
pessoas = [{"nome":"Ana","idade":30},{"nome":"Beto","idade":25}]
# nova lista ordenada por idade:
ordenado = sorted(pessoas, key=lambda x: x['idade'])
# ordenar in-place por nome, ignorando maiúsculas
pessoas.sort(key=lambda p: p['nome'].lower(), reverse=False)

--- Conversões úteis ---
s = "olá mundo"
chars = list(s)            # ['o','l','á',' ',...]
nums = [1,2,3]
s2 = ",".join(map(str, nums))  # "1,2,3"  -> join aceita só strings
t = tuple(nums)
st = set(nums)

=== Uso como pilha e fila ===

Pilha (stack): append() + pop() → LIFO (rápido).

Fila: list.pop(0) funciona, mas é O(n). Para fila eficiente use collections.deque:

from collections import deque
q = deque()
q.append(item)
q.popleft()   # O(1)


Priority queue: use heapq.

Performance (complexidade típica)

list[i] (indexing): O(1)

append(x): amortizado O(1)

pop() (último): O(1); pop(0) ou insert(0,x): O(n)

insert(i,x) (meio): O(n)

remove(x) / x in list: O(n)

slicing cria nova lista: L[a:b] é O(k) (k = tamanho do slice)

    === Armadilhas comuns & boas práticas ===

Mutáveis como valor default em função:

def f(x, lista=[]):   # errado — lista é compartilhada entre chamadas
    lista.append(x)
    return lista

# certo:
def f(x, lista=None):
    if lista is None:
        lista = []
    lista.append(x)
    return lista


Usar list() para copiar em vez de = quando quiser uma nova lista.

sorted() retorna nova lista; list.sort() modifica in-place.

join() só para strings — converta com map(str, ...).

Não use * para criar listas aninhadas (ver exemplo da matriz).

Ferramentas/funcionalidades extra

enumerate(), zip(), any(), all(), reversed(), min(), max(), sum() — úteis com listas.

itertools (combinations, permutations, chain, product) para casos avançados.

functools.reduce() se precisar (muitas vezes sum() ou comprehension é mais legível).

Exemplos práticos comentados

    --- Soma de uma lista: ---

nums = [1,2,3,4]
print(sum(nums))  # 10


    --- Filtrar pares e dobrar: ---

nums = [1,2,3,4,5,6]
res = [x*2 for x in nums if x%2==0]  # [4,8,12]


 --- Achando índice com segurança: ---

try:
    idx = nomes.index("João")
except ValueError:
    idx = -1  # ou tratar como preferir


    --- Flatten (achatar) lista de listas: ---

mat = [[1,2],[3,4],[5]]
flat = [x for row in mat for x in row]  # [1,2,3,4,5]

Exercícios práticos (faça você mesmo) — com soluções

    --- Remover duplicatas mantendo ordem ---

def unique_keep_order(lst):
    seen = set()
    res = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            res.append(x)
    return res


    --- Maior e segundo maior número ---

def two_max(lst):
    if len(lst) < 2: return None
    a, b = float('-inf'), float('-inf')
    for x in lst:
        if x > a:
            a, b = x, a
        elif x > b:
            b = x
    return a, b

    --- Transpor matriz ---

def transpose(mat):
    return [list(row) for row in zip(*mat)]
    
"""

valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

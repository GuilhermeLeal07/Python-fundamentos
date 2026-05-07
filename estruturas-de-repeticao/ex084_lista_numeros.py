"""
    1. O que é um DICIONÁRIO

Um dicionário (dict) é uma coleção de pares “chave: valor”.
Em vez de acessar elementos por índice (como nas listas), você acessa pelo nome da chave.

--  Pense como um “cadastro” de informações.

🔹 Exemplo básico
pessoa = {
    "nome": "Guilherme",
    "idade": 20,
    "cidade": "São Paulo"
}

print(pessoa["nome"])   # Guilherme
print(pessoa["idade"])  # 20


--  Aqui:

"nome", "idade", "cidade" → são chaves

"Guilherme", 20, "São Paulo" → são valores

    2. Criando Dicionários
 - Forma literal (mais comum):
dados = {"nome": "Ana", "idade": 25}

 - Usando dict():
dados = dict(nome="Bruno", idade=30)

 - Criando vazio e adicionando depois:
dados = {}
dados["nome"] = "Carlos"
dados["idade"] = 22

    3. Acessando e modificando valores
pessoa = {"nome": "João", "idade": 25}

print(pessoa["nome"])    # João

pessoa["idade"] = 26     # altera
pessoa["profissão"] = "Programador"  # adiciona nova chave

print(pessoa)
# {'nome': 'João', 'idade': 26, 'profissão': 'Programador'}


⚠️ Se tentar acessar uma chave inexistente com pessoa["altura"], dá erro.

✅ Use .get() para evitar erro:

print(pessoa.get("altura", "Não informada"))

    4. Removendo itens
pessoa = {"nome": "Maria", "idade": 28, "cidade": "RJ"}

# Remove uma chave
del pessoa["cidade"]

# Remove e retorna o valor
idade = pessoa.pop("idade")

# Remove o último par adicionado
pessoa.popitem()

# Esvaziar o dicionário
pessoa.clear()

    5. Métodos úteis
pessoa = {"nome": "Lucas", "idade": 23, "cidade": "SP"}

print(pessoa.keys())     # retorna as chaves
print(pessoa.values())   # retorna os valores
print(pessoa.items())    # retorna pares (chave, valor)

for k, v in pessoa.items():
    print(f"{k} => {v}")


Saída:

nome => Lucas
idade => 23
cidade => SP

    6. Copiar dicionários

⚠️ Assim como nas listas, copiar diretamente cria referência:

a = {"x": 1}
b = a
b["x"] = 999
print(a)  # {'x': 999} 😬


✅ Use .copy() ou dict():

a = {"x": 1}
b = a.copy()
b["x"] = 999
print(a)  # {'x': 1}

🔹 7. Dicionários compostos (lista de dicionários)

Muito usado para armazenar vários registros (como um “banco de dados” em memória).

pessoas = [
    {"nome": "Ana", "idade": 25},
    {"nome": "Bruno", "idade": 30},
    {"nome": "Carla", "idade": 22}
]

for p in pessoas:
    print(f"{p['nome']} tem {p['idade']} anos.")


Saída:

Ana tem 25 anos.
Bruno tem 30 anos.
Carla tem 22 anos.

    8. Dicionários dentro de dicionários
alunos = {
    "A1": {"nome": "Lucas", "nota": 8.5},
    "A2": {"nome": "Marina", "nota": 9.0}
}

print(alunos["A1"]["nome"])  # Lucas


👉 Estrutura típica de sistemas que lidam com cadastros e relatórios.

🔎 9. Outras funções e truques úteis
➕ Mesclar dicionários
a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}

# Python 3.9+
c = a | b
print(c)  # {'x': 1, 'y': 3, 'z': 4}

➕ Atualizar dicionário existente
pessoa = {"nome": "Ana", "idade": 25}
pessoa.update({"idade": 26, "cidade": "SP"})

🔄 Gerar dicionário com loop (dict comprehension)
quadrados = {x: x*x for x in range(5)}
print(quadrados)  # {0:0, 1:1, 2:4, 3:9, 4:16}

    10. Funções úteis com dicionários
pessoa = {"nome": "Guilherme", "idade": 21}

# Tamanho
print(len(pessoa))  # 2

# Verificar se chave existe
print("idade" in pessoa)  # True

# Remover e capturar valor
idade = pessoa.pop("idade")

    11. Ligação com bibliotecas

Os dicionários são usados o tempo todo por várias bibliotecas.

🔸 json — salvar e carregar dicionários
import json

dados = {"nome": "Guilherme", "idade": 20}

# Converter para texto JSON
json_str = json.dumps(dados, indent=4)
print(json_str)

# Salvar em arquivo
with open("dados.json", "w") as f:
    json.dump(dados, f)

# Ler de volta
with open("dados.json", "r") as f:
    novo = json.load(f)
print(novo)

🔸 pandas — transformar dicionários em tabelas
import pandas as pd

dados = {
    "nome": ["Ana", "Bruno", "Carla"],
    "idade": [25, 30, 22],
    "cidade": ["RJ", "SP", "MG"]
}

df = pd.DataFrame(dados)
print(df)


Saída:

    nome  idade cidade
0    Ana     25     RJ
1  Bruno     30     SP
2  Carla     22     MG

🔸 collections — dicionários especiais
from collections import defaultdict, Counter

# defaultdict evita erro com chaves inexistentes
cadastro = defaultdict(int)
cadastro["idade"] += 1
print(cadastro)  # {'idade': 1}

# Counter conta elementos
letras = Counter("banana")
print(letras)  # Counter({'a':3, 'n':2, 'b':1})

⚡ 12. Aplicação prática (mini sistema)
cadastro = []

while True:
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    cidade = input("Cidade: ")

    cadastro.append({"nome": nome, "idade": idade, "cidade": cidade})

    continuar = input("Deseja continuar? [S/N] ").strip().upper()
    if continuar == "N":
        break

print("\n--- CADASTRO ---")
for pessoa in cadastro:
    print(f"{pessoa['nome']} ({pessoa['idade']} anos) - {pessoa['cidade']}")

    13. Quando usar DICIONÁRIOS (vs Listas)

 - Use dicionários quando:

Precisa ligar nomes a valores (como “nome → idade”);

Vai buscar informações específicas com rapidez;

Quer representar entidades reais (pessoa, produto, aluno).

 - Use listas quando:

Os elementos são apenas valores ordenados;

Você não precisa associar cada valor a uma chave.

    14. Misturando tudo: listas + dicionários

Essa é uma das estruturas mais usadas em Python real:

alunos = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Bruno", "nota": 9.0},
    {"nome": "Carla", "nota": 7.0}
]

# Calcular média
media = sum(a["nota"] for a in alunos) / len(alunos)
print(f"Média da turma: {media:.1f}")

"""







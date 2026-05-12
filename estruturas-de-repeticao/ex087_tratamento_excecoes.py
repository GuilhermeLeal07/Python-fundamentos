"""
⚠️ 1️⃣ O que são Erros e Exceções

Quando o Python encontra algo que não consegue executar, ele interrompe o programa e mostra uma mensagem de erro.

Exemplo simples:

print(10 / 0)


💥 Resultado:

ZeroDivisionError: division by zero


👉 Isso é uma exceção: um tipo de erro que interrompe o fluxo normal do programa.

💡 2️⃣ Tipos comuns de exceções
Exceção	Quando acontece
ZeroDivisionError	Quando divide por zero
ValueError	Quando converte um valor inválido
TypeError	Quando usa o tipo de dado errado
IndexError	Quando acessa um índice inexistente em uma lista
KeyError	Quando acessa uma chave inexistente em um dicionário
FileNotFoundError	Quando tenta abrir um arquivo que não existe
NameError	Quando tenta usar uma variável que não foi definida
🧠 3️⃣ Como tratar exceções — try / except

A estrutura básica é:

try:
    # código que pode causar erro
except:
    # o que fazer se o erro ocorrer

🔹 Exemplo:
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except:
    print("❌ Ocorreu um erro.")


💬 Problema: esse except é genérico demais (captura qualquer erro).

Vamos melhorar.

✅ 4️⃣ Tratando exceções específicas
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except ValueError:
    print("❌ Você deve digitar apenas números.")
except ZeroDivisionError:
    print("❌ Não é possível dividir por zero.")


🎯 Assim, o Python sabe como reagir a cada erro.

🔄 5️⃣ Usando else e finally

Esses dois blocos tornam o controle ainda mais refinado.

try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except ValueError:
    print("❌ Digite um número válido.")
except ZeroDivisionError:
    print("❌ Não divida por zero!")
else:
    print(f"✅ Resultado: {resultado}")
finally:
    print("🔚 Fim do programa.")


🧩 Explicação:

Bloco	Função
try	Código que pode gerar erro
except	Captura e trata erros
else	Executa se nenhum erro ocorrer
finally	Executa sempre, com ou sem erro
🧰 6️⃣ Capturando a mensagem de erro

Você pode capturar o erro em uma variável para exibir detalhes técnicos.

try:
    n = int(input("Digite um número: "))
    print(10 / n)
except Exception as erro:
    print(f"⚠️ Ocorreu um erro: {erro}")


Saída (por exemplo):

⚠️ Ocorreu um erro: division by zero


Isso é muito útil em debugs e logs.

🧮 7️⃣ Criando exceções personalizadas (nível avançado)

Você pode criar seu próprio tipo de erro para situações específicas.

class NumeroNegativoError(Exception):
    # Erro lançado quando o número é negativo. #
    pass

def fatorial(n):
    if n < 0:
        raise NumeroNegativoError("Fatorial não definido para números negativos.")
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

try:
    print(fatorial(-5))
except NumeroNegativoError as e:
    print(f"❌ Erro: {e}")


🧠 Aqui, criamos uma classe de exceção personalizada que herda de Exception.

⚙️ 8️⃣ Boas práticas profissionais

✅ Evite usar except: sozinho.
Use exceções específicas sempre que possível.

✅ Não esconda erros importantes.
Tratar o erro deve ajudar o programa a reagir, não apenas “silenciar” o problema.

✅ Use finally para fechar conexões, arquivos ou liberar recursos.

✅ Crie mensagens de erro amigáveis, especialmente em programas interativos.

📚 9️⃣ Exemplo prático completo — com tudo junto
def dividir(a, b):
    # Divide dois números e trata exceções. #
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("❌ Erro: divisão por zero não é permitida.")
    except TypeError:
        print("❌ Erro: use apenas números.")
    else:
        print(f"✅ Resultado: {resultado}")
    finally:
        print("🔚 Operação finalizada.\n")


# Testes
dividir(10, 2)
dividir(10, 0)
dividir(10, "a")


Saída:

✅ Resultado: 5.0
🔚 Operação finalizada.

❌ Erro: divisão por zero não é permitida.
🔚 Operação finalizada.

❌ Erro: use apenas números.
🔚 Operação finalizada.

🏁 10️⃣ Resumo final
Conceito	Função
try	Tenta executar o código
except	Captura o erro
else	Executa se não houver erro
finally	Executa sempre, mesmo com erro
raise	Lança uma exceção manualmente
Exception	Classe base para todos os erros em Python
"""

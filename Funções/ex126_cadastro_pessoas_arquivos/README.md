# 📂 Cadastro de Pessoas com Arquivos

Este diretório contém a segunda etapa do sistema de cadastro de pessoas desenvolvido durante os estudos de Funções, Modularização e Manipulação de Arquivos em Python.

## 📖 Descrição do desafio

**Correspondente ao Desafio 115B do Curso de Python – Gustavo Guanabara.**

Nesta etapa, o objetivo é expandir o sistema criado anteriormente, adicionando persistência de dados por meio de arquivos texto.

O programa verifica automaticamente se o arquivo de cadastro existe, cria-o caso necessário e permite cadastrar e listar pessoas utilizando operações de leitura e escrita em arquivos.

## 📚 Sobre o projeto

Foi desenvolvido um sistema simples capaz de armazenar registros de pessoas em um arquivo `.txt`, mantendo os dados mesmo após o encerramento do programa.

O projeto foi organizado em funções reutilizáveis, facilitando futuras expansões.

## 🚀 Conteúdos abordados

* Manipulação de arquivos
* Leitura de arquivos texto
* Escrita em arquivos texto
* Criação automática de arquivos
* Tratamento de exceções (`try` / `except`)
* Modularização
* Reutilização de funções

## 🧠 Objetivo

Desenvolver a capacidade de:

* Trabalhar com arquivos em Python.
* Armazenar informações de forma permanente.
* Separar responsabilidades em funções.
* Tratar possíveis erros durante operações com arquivos.
* Construir sistemas mais organizados e reutilizáveis.

## 🗂️ Estrutura

Os arquivos seguem o padrão:

```text
ex126_cadastro_pessoas_arquivos/
├── README.md
├── desafio115b.py
├── menu.py
├── arquivo.txt
└── funcoes.py
```

## 💡 Observações

* O arquivo de cadastro é criado automaticamente caso não exista.
* Os registros são armazenados utilizando o formato `nome;idade`.
* O projeto utiliza funções específicas para leitura, escrita e cadastro.
* O tratamento de exceções torna a aplicação mais segura durante o acesso aos arquivos.

## 📌 Próximo passo

Adicionar melhorias na interface do sistema, validação de entradas e organização em pacotes, tornando a aplicação mais próxima de um sistema profissional.

---

✍️ **Desenvolvido como parte dos estudos de Funções, Modularização e Manipulação de Arquivos em Python.**

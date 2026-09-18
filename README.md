# 🎓 Sistema de Alunos em Python

Projeto pessoal desenvolvido para praticar e aplicar conceitos de **Python, Programação Orientada a Objetos, SQL e persistência de dados**.

O projeto acompanha minha evolução nos estudos de programação. Em vez de substituir as versões anteriores, os principais estágios do sistema foram preservados através do histórico do Git e de tags.

## 📌 Sobre o projeto

O sistema permite realizar operações básicas de gerenciamento de alunos, como:

- Cadastro de alunos
- Cadastro de alunos Premium
- Consulta por RG
- Listagem de alunos
- Registro de pagamento
- Controle de adimplência
- Persistência dos dados utilizando SQLite

Alunos Premium possuem uma regra específica no sistema e não realizam pagamento de mensalidade.

## 🚀 Evolução do projeto

### v0.1 — POO

Primeira versão preservada do projeto.

Nesta etapa foram utilizados:

- Classes e objetos
- Herança
- Sobrescrita de métodos
- Polimorfismo
- Dicionário para armazenamento dos objetos em memória

Os dados eram perdidos quando o programa era encerrado.

### v0.2 — Refatoração

Reorganização da estrutura do sistema com separação de responsabilidades.

Foram adicionadas melhorias como:

- Funções específicas para entrada e validação de dados
- Tratamento de `ValueError`
- Validação de RG
- Separação do menu
- Criação da função principal `Main()`
- Redução de código repetido

### v0.3 — SQLite

Migração do armazenamento em memória para um banco de dados SQLite.

Nesta etapa foram aplicados:

- Criação e conexão com banco SQLite
- `INSERT` para cadastro
- `SELECT` para consultas
- `UPDATE` para pagamentos
- `fetchone()` e `fetchall()`
- Queries parametrizadas
- `commit()`
- Persistência dos alunos após o encerramento do programa

## 🛠️ Tecnologias

- Python
- SQLite
- SQL
- Git
- GitHub

## 📂 Estrutura atual

```text
sistema-alunos-python/
├── main.py
├── README.md
└── .gitignore
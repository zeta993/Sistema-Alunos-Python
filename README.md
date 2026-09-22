# 🎓 Sistema de Gerenciamento de Alunos

Sistema desenvolvido em **Python** para gerenciamento de alunos, criado inicialmente durante meus estudos de programação e posteriormente expandido como projeto pessoal.

O projeto registra minha evolução prática em desenvolvimento de software, partindo de uma implementação com **Programação Orientada a Objetos e armazenamento em memória**, passando por refatorações e persistência com **SQLite**, até a implementação de **interface e recursos de análise de dados**.

---

## 📌 Sobre o projeto

O sistema permite cadastrar e gerenciar alunos, mantendo suas informações de forma persistente em um banco de dados **SQLite**.

A aplicação foi desenvolvida de forma incremental, com foco na prática de **Programação Orientada a Objetos**, manipulação de banco de dados e organização do código em diferentes responsabilidades.

---

## ⚙️ Funcionalidades

- Cadastro de alunos
- Consulta de alunos cadastrados
- Atualização de informações
- Exclusão de registros
- Persistência de dados com SQLite
- Interface para utilização do sistema
- Tratamento e análise dos dados cadastrados
- Geração de gráficos a partir dos dados do sistema

---

## 🚀 Evolução do projeto

O projeto foi desenvolvido em etapas, preservando versões anteriores para demonstrar a evolução da aplicação e dos conceitos utilizados.

### v0.1 — Programação Orientada a Objetos

Primeira versão do sistema, desenvolvida com foco na aplicação dos conceitos de **POO**.

Os dados eram mantidos em memória durante a execução do programa, permitindo praticar:

- Classes e objetos
- Construtores
- Métodos
- Encapsulamento
- Herança
- Organização da lógica da aplicação

### v0.2 — Refatoração

Nesta etapa, o código passou por melhorias de organização e estrutura.

O objetivo foi separar melhor as responsabilidades e preparar a aplicação para a implementação de persistência de dados.

### v0.3 — SQLite

A aplicação passou a utilizar **SQLite** para armazenamento persistente das informações.

Com essa evolução, os dados deixaram de existir somente durante a execução do programa e passaram a ser armazenados em banco de dados.

Foram implementadas operações de:

- Cadastro
- Consulta
- Atualização
- Exclusão

Essa etapa permitiu aplicar na prática conceitos de **SQL, persistência de dados e integração entre Python e banco de dados**.

### Interface e análise de dados

Nas etapas seguintes, o projeto recebeu uma interface integrada à lógica da aplicação e ao banco de dados.

Também foram adicionados recursos para tratamento e análise das informações cadastradas, utilizando **Pandas** e geração de gráficos para visualização dos dados.

---

## 🛠️ Tecnologias utilizadas

- **Python**
- **SQLite**
- **SQL**
- **Programação Orientada a Objetos (POO)**
- **Pandas**
- **Git**
- **GitHub**

---

## 📂 Estrutura atual

```text
Sistema-alunos-phyton/
│
├── main.py
├── interface.py
├── graficos.py
├── README.md
└── .gitignore
```

### `main.py`

Contém a lógica principal da aplicação, incluindo as estruturas responsáveis pelo gerenciamento dos alunos e interação com o banco de dados.

### `interface.py`

Responsável pela interface utilizada para interação com as funcionalidades do sistema.

### `graficos.py`

Responsável pelo tratamento e visualização dos dados, incluindo recursos de análise e geração de gráficos.

---

## 🎯 Objetivo do projeto

Este projeto tem como principal objetivo colocar em prática os conhecimentos adquiridos durante meus estudos de desenvolvimento de software.

Além do resultado final, o repositório busca registrar minha evolução técnica, mostrando como uma aplicação inicialmente simples pode ser progressivamente refatorada e expandida com novos conceitos, tecnologias e funcionalidades.

---

## 🔄 Em desenvolvimento

O projeto continua sendo utilizado para estudos e implementação de novos conhecimentos conforme avanço na graduação e nos estudos independentes.

Novas funcionalidades e melhorias poderão ser adicionadas ao longo do desenvolvimento.

---

## 👨‍💻 Autor

**Vinicius Dias**

Estudante de Análise e Desenvolvimento de Sistemas, com foco em desenvolvimento de software e backend.

- GitHub: `zeta993`
- LinkedIn: `vinicius-dias-34126a2b6`
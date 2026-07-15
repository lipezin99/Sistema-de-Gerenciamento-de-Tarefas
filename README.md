# Sistema de Gerenciamento de Tarefas

## Autor

Felipe Peixinho

## Descrição do Projeto

Este projeto consiste em um sistema simples de gerenciamento de tarefas desenvolvido em Python.

O objetivo é permitir o controle de tarefas através de operações CRUD (Create, Read, Update e Delete), possibilitando adicionar, editar, concluir e remover tarefas.

O projeto também possui testes automatizados utilizando Pytest para garantir o funcionamento correto das principais funcionalidades do sistema.

---

## Funcionalidades

O sistema permite:

* Adicionar novas tarefas;
* Visualizar tarefas cadastradas;
* Editar informações de uma tarefa;
* Concluir tarefas;
* Remover tarefas.

---

## Tecnologias Utilizadas

* Python
* Pytest

---

## Estrutura do Projeto

```
Projeto unifecaf
│
├── src
│   ├── __init__.py
│   ├── crud.py
│   └── tarefa.py
│
├── tests
│   └── test_crud.py
│
├── main.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Instalação

Clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
```

Acesse a pasta do projeto:

```bash
cd "Projeto unifecaf"
```

Crie o ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente virtual:

Windows:

```bash
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## Execução do Sistema

Para executar o programa:

```bash
python main.py
```

---

## Execução dos Testes

O projeto possui testes automatizados utilizando Pytest.

Para executar os testes:

```bash
pytest
```

Resultado esperado:

```
4 passed
```

Os testes verificam:

* Criação de tarefas;
* Edição de tarefas;
* Conclusão de tarefas;
* Remoção de tarefas.

---

## Organização do Código

O projeto foi dividido em módulos para facilitar a manutenção:

### tarefa.py

Responsável pela definição da estrutura de uma tarefa, contendo suas informações principais.

### crud.py

Responsável pelas operações de gerenciamento das tarefas:

* Adicionar;
* Editar;
* Concluir;
* Remover.

### tests/

Contém os testes automatizados responsáveis por validar o funcionamento das operações do sistema.

---

## Testes Realizados

Todos os testes automatizados foram executados com sucesso:

```
4 passed
```

Isso confirma que as funcionalidades principais do sistema estão funcionando corretamente.

---

## Conclusão

O projeto apresenta uma aplicação de gerenciamento de tarefas utilizando Python, aplicando organização de código, operações CRUD e testes automatizados para garantir a qualidade e funcionamento das funcionalidades implementadas.

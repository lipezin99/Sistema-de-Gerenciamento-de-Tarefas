# Sistema de Gerenciamento de Tarefas

## Autor

Felipe Peixinho

## Descrição do Projeto

Este projeto consiste em um sistema simples de gerenciamento de tarefas desenvolvido em Python.

O objetivo é permitir o controle de tarefas através de operações CRUD (Create, Read, Update e Delete), possibilitando adicionar, editar, concluir e remover tarefas.

O projeto também possui testes automatizados utilizando Pytest para garantir o funcionamento correto das principais funcionalidades do sistema.

---

## Metodologia Ágil Utilizada

O projeto foi conduzido utilizando **Kanban**, através da aba **Projects**
do GitHub, com colunas **A Fazer**, **Em Progresso** e **Concluído**. Essa
abordagem permitiu visualizar o fluxo de trabalho em tempo real, identificar
gargalos e priorizar tarefas críticas — atendendo diretamente à necessidade
do cliente (TechFlow Solutions / startup de logística) de acompanhar o
desenvolvimento de forma contínua e transparente.

Cada tarefa do quadro corresponde a uma etapa do desenvolvimento
(planejamento, estrutura do projeto, implementação do CRUD, testes,
documentação etc.), e o histórico de commits reflete a evolução incremental
típica de metodologias ágeis.

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


## Gestão de Mudanças

Durante o desenvolvimento do projeto, identificamos a necessidade de uma
pequena alteração no escopo inicial: a adição da funcionalidade de
**priorização de tarefas**, permitindo classificar cada tarefa como Alta,
Média ou Baixa prioridade.

### Justificativa

O cliente (startup de logística) precisa acompanhar o fluxo de trabalho em
tempo real e **priorizar tarefas críticas** — requisito citado no desafio
original. A versão inicial do CRUD não contemplava esse controle, então
avaliamos que era necessário incluir esse atributo para atender ao objetivo
do sistema.

### Como a mudança foi conduzida

1. Um novo card foi criado no quadro Kanban (coluna **A Fazer**) descrevendo
   a nova funcionalidade;
2. O card foi movido para **Em Progresso** durante a implementação;
3. Foi realizado um novo commit implementando o atributo `prioridade` na
   classe `Tarefa` e ajustando o `crud.py` para permitir filtrar/ordenar por
   prioridade;
4. O card foi movido para **Concluído** após os testes automatizados
   confirmarem o funcionamento;
5. Esta seção do README foi atualizada para documentar a mudança.

Essa simulação demonstra como metodologias ágeis lidam bem com mudanças de
escopo: em vez de travar o projeto, a alteração foi absorvida em um novo
ciclo de trabalho, sem comprometer as entregas já concluídas.
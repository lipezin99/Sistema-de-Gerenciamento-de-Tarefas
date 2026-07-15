from src.crud import (
    tarefas,
    adicionar_tarefa,
    editar_tarefa,
    remover_tarefa,
    concluir_tarefa,
)


def setup_function():
    tarefas.clear()


def test_adicionar_tarefa():
    adicionar_tarefa("Estudar Python")

    assert len(tarefas) == 1
    assert tarefas[0].titulo == "Estudar Python"


def test_editar_tarefa():
    adicionar_tarefa("Tarefa antiga")

    editar_tarefa(1, "Tarefa nova")

    assert tarefas[0].titulo == "Tarefa nova"


def test_concluir_tarefa():
    adicionar_tarefa("Projeto")

    concluir_tarefa(1)

    assert tarefas[0].concluida is True


def test_remover_tarefa():
    adicionar_tarefa("Excluir")

    remover_tarefa(1)

    assert len(tarefas) == 0

    def test_prioridade_tarefa():
    crud = CRUD()
    crud.adicionar_tarefa("Entregar relatório", prioridade="Alta")
    tarefas_altas = crud.listar_por_prioridade("Alta")
    assert len(tarefas_altas) == 1
    assert tarefas_altas[0].titulo == "Entregar relatório"
from src.tarefa import Tarefa

tarefas = []

def adicionar_tarefa(titulo):
    tarefas.append(Tarefa(titulo))
    print("Tarefa adicionada com sucesso!")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\n===== LISTA DE TAREFAS =====")
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i}. {tarefa}")

def editar_tarefa(indice, novo_titulo):
    indice -= 1
    if 0 <= indice < len(tarefas):
        tarefas[indice].titulo = novo_titulo
        print("Tarefa atualizada!")
    else:
        print("Índice inválido.")

def remover_tarefa(indice):
    indice -= 1
    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)
        print("Tarefa removida!")
    else:
        print("Índice inválido.")

def concluir_tarefa(indice):
    indice -= 1
    if 0 <= indice < len(tarefas):
        tarefas[indice].concluida = True
        print("Tarefa concluída!")
    else:
        print("Índice inválido.")

        def listar_por_prioridade(self, prioridade: str):
    return [t for t in self.tarefas if t.prioridade == prioridade]
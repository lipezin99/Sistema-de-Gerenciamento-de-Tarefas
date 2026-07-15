class Tarefa:
    def __init__(self, titulo: str, prioridade: str = "Média"):
        self.titulo = titulo
        self.concluida = False
        self.prioridade = prioridade  # Alta, Média ou Baixa

    def concluir(self):
        self.concluida = True
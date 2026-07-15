class Tarefa:
    def __init__(self, titulo):
        self.titulo = titulo
        self.concluida = False

    def __str__(self):
        status = "✓" if self.concluida else "✗"
        return f"{self.titulo} [{status}]"
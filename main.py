from src.crud import *

while True:
    print("\n====== GERENCIADOR DE TAREFAS ======")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Editar tarefa")
    print("4 - Remover tarefa")
    print("5 - Concluir tarefa")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_tarefa(input("Título: "))
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        listar_tarefas()
        editar_tarefa(int(input("Número da tarefa: ")), input("Novo título: "))
    elif opcao == "4":
        listar_tarefas()
        remover_tarefa(int(input("Número da tarefa: ")))
    elif opcao == "5":
        listar_tarefas()
        concluir_tarefa(int(input("Número da tarefa: ")))
    elif opcao == "6":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida.")
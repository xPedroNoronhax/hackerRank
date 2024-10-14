def main():
    tasks = {}
    print("Bem vindo a lista de tarefas")

    while True:
        show_menu()
        choice = input("Opção: ")
        if choice == '0':
            print("Programa encerrado")
            break
        if choice not in ["1","2","3","4"]:
            print("Escolha uma opçao de 1 a 4.")
            continue
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            list_task(tasks)
        elif choice == "4":
            conclude_task(tasks)

        


def show_menu():
    print("Escolha a opção desejada (1-4) e 0 para sair")
    print("1 - Adicionar tarefas")
    print("2 - Remover tarefas")
    print("3 - Mostrar tarefas")
    print("4 - Concluir uma tarefa")

def add_task(tasks):
    new_task = input("Qual tarefa você deseja adicionar? ")
    tasks[new_task] = "Pendente"
    print(f"{new_task} consta agora em lista de tarefas")


def remove_task(tasks):
    if not tasks:
        print("Não há tarefas para serem removidas")
    else:
        list_task(tasks)
        remove_task = input("Qual tarefa você deseja remover?")
        if remove_task in tasks:
            del tasks[remove_task]
            print(f"{remove_task}: tarefa removida")
        else:
            print("Tarefa não encontrada")

def list_task(tasks):
    if not tasks:
        print("Não há tarefas a serem exibidas")
    else:
        for task,status in tasks.items():
            print(f"{task}:{status}")


def conclude_task(tasks):
    list_task(tasks)
    close_task = input("Qual tarefa você deseja concluir?")
    if close_task in tasks:
        if tasks[close_task] == "Pendente":
            tasks[close_task] = "Concluída"
            print(f"{close_task}: tarefa concluída")
        else:
            print("Tarefa ja esta concluída.")
    else:
        print("Tarefa não encontrada")

if __name__ == "__main__":
    main()
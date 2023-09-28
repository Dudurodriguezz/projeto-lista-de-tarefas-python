git init
# todo.py

class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def list_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            status = "Concluída" if task.completed else "Pendente"
            print(f"{i}. {task.description} - {status}")

    def complete_task(self, task_index):
        if 0 < task_index <= len(self.tasks):
            self.tasks[task_index - 1].completed = True
            print(f"Tarefa {task_index} marcada como concluída.")
        else:
            print("Índice de tarefa inválido.")

if __name__ == "__main__":
    todo_list = TodoList()

    while True:
        print("\n==== Lista de Tarefas ====")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            description = input("Digite a descrição da tarefa: ")
            todo_list.add_task(description)
        elif choice == "2":
            todo_list.list_tasks()
        elif choice == "3":
            task_index = int(input("Digite o número da tarefa a ser marcada como concluída: "))
            todo_list.complete_task(task_index)
        elif choice == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")


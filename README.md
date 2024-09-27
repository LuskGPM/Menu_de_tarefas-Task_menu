# Português
# Gerenciador de Tarefas CLI

Este é um **Gerenciador de Tarefas** simples desenvolvido em Python. Ele permite que os usuários gerenciem suas tarefas, adicionando, removendo, marcando tarefas como concluídas e listando tanto as tarefas pendentes quanto as concluídas. O programa é executado no terminal e oferece um menu interativo para o gerenciamento de tarefas.

## Funcionalidades

- Adicionar novas tarefas à lista de pendentes.
- Remover tarefas da lista de pendentes por número.
- Listar todas as tarefas pendentes.
- Marcar tarefas como concluídas (mover da lista de pendentes para a lista de concluídas).
- Visualizar todas as tarefas concluídas.
- Sair do programa.

## Como Usar

1. Clone o repositório:
    ```bash
    git clone https://github.com/seuusuario/gerenciador-tarefas-cli.git
    cd gerenciador-tarefas-cli
    ```

2. Execute o programa:
    ```bash
    python gerenciador_tarefas.py
    ```

3. O menu apresentará as seguintes opções:
    - `1. Adicionar tarefa`: Permite adicionar uma nova tarefa.
    - `2. Remover tarefa`: Permite remover uma tarefa, seja pelo número ou pelo nome.
    - `3. Listar tarefas`: Exibe todas as suas tarefas pendentes.
    - `4. Marcar tarefa como concluída`: Move uma tarefa da lista de pendentes para a lista de concluídas.
    - `5. Exibir tarefas concluídas`: Mostra a lista de tarefas que você marcou como concluídas.
    - `6. Sair`: Encerra o programa.

## Visão Geral do Código

### Menu Principal
O menu principal permite que o usuário selecione uma opção usando números entre 1 e 6. Ele garante que somente entradas válidas sejam aceitas, evitando erros.

### Gerenciamento de Tarefas
As tarefas são armazenadas em duas listas:
- `task_list`: Armazena as tarefas pendentes.
- `completed_task_list`: Armazena as tarefas concluídas.

### Funções
- `display_tasks()`: Recebe uma lista de tarefas e um título como entrada e exibe as tarefas. Caso a lista esteja vazia, informa o usuário.

## Exemplo

Ao executar o programa, o seguinte menu aparecerá:

---------- MENU ----------
1. Adicionar tarefa
2. Remover tarefa
3. Listar tarefas
4. Marcar tarefa como concluída
5. Exibir tarefas concluídas
6. Sair


Você pode interagir com o programa selecionando o número correspondente à ação que deseja realizar.

## Melhorias Futuras

- Adicionar persistência das tarefas (salvando as tarefas em um arquivo ou banco de dados).
- Permitir a edição de tarefas.
- Adicionar a função de desfazer marcações de concluídas.
- Implementar níveis de prioridade para as tarefas.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.



# English
# CLI Task Manager

This is a simple **Task Manager** developed in Python. It allows users to manage their tasks by adding, removing, marking tasks as completed, and listing both pending and completed tasks. The program runs in the terminal and provides an interactive menu for task management.

## Features

- Add new tasks to the pending list.
- Remove tasks from the pending list by number.
- List all pending tasks.
- Mark tasks as completed (move from the pending list to the completed list).
- View all completed tasks.
- Exit the program.

## How to Use

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/cli-task-manager.git
    cd cli-task-manager
    ```

2. Run the program:
    ```bash
    python task_manager.py
    ```

3. The menu will present the following options:
    - `1. Add task`: Allows adding a new task.
    - `2. Remove task`: Allows removing a task by its number or name.
    - `3. List tasks`: Displays all your pending tasks.
    - `4. Mark task as completed`: Moves a task from the pending list to the completed list.
    - `5. Display completed tasks`: Shows the list of tasks you have marked as completed.
    - `6. Exit`: Closes the program.

## Code Overview

### Main Menu
The main menu allows users to select an option using numbers between 1 and 6. It ensures that only valid inputs are accepted, preventing errors.

### Task Management
Tasks are stored in two lists:
- `task_list`: Stores the pending tasks.
- `completed_task_list`: Stores the completed tasks.

### Functions
- `display_tasks()`: Takes a task list and a title as input, then displays the tasks. If the list is empty, it notifies the user.

## Example

When running the program, the following menu will appear:

---------- MENU ----------
1. Add task
2. Remove task
3. List tasks
4. Mark task as completed
5. Display completed tasks
6. Exit


You can interact with the program by selecting the number corresponding to the action you want to perform.

## Future Improvements

- Add task persistence (saving tasks to a file or database).
- Allow task editing.
- Add the ability to undo completed tasks.
- Implement priority levels for tasks.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

# Função para exibir tarefas de uma lista específica (pendentes ou concluídas)
def exibir_tarefas(lista_def, titulo):
    # Se a lista estiver vazia, informa não haver tarefas
    if len(lista_def) == 0:
        print(f'Não há {titulo.lower()}.')
    else:
        print(f'\n{titulo:-^30}')
        for i, tarefa in enumerate(lista_def, start=1):
            print(f'{i}. {tarefa}')


# Função para validação de entrada numérica
def validar_numero_input(mensagem, limite):
    while True:
        escolha = input(mensagem)
        if escolha.isdigit() and 0 < int(escolha) <= limite:
            return int(escolha)
        else:
            print("Entrada inválida. Tente novamente.")


# Função para continuar o programa
def continuar():
    input('Pressione Enter para continuar...')


# Listas de tarefas
lista_tarefa = ['Lutar', 'Ir para academia']
lista_tarefa_conclusas = ['Trabalho da faculdade', 'fazer o café']

while True:
    print(f'\n{" MENU ":-^30}')
    print('''1. Adicionar tarefa
2. Remover Tarefa
3. Listar tarefa
4. Marcar tarefa concluída
5. Exibir tarefas concluídas
6. Sair''')

    escolha_user = validar_numero_input('Escolha uma opção: ', 6)

    if escolha_user == 1:
        nova_tarefa = input('\nDigite nova tarefa: ')
        lista_tarefa.append(nova_tarefa)
        print('Tarefa adicionada com sucesso!')
        continuar()

    elif escolha_user == 2:
        if lista_tarefa:
            exibir_tarefas(lista_tarefa, ' Suas tarefas ')
            tarefa_remover = validar_numero_input('Digite o número da tarefa que deseja excluir: ', len(lista_tarefa))
            tarefa_excluida = lista_tarefa.pop(tarefa_remover - 1)
            print(f'Tarefa "{tarefa_excluida}" removida com sucesso!')
        else:
            print('Você não possui tarefas pendentes.')
        continuar()

    elif escolha_user == 3:
        exibir_tarefas(lista_tarefa, ' Suas tarefas ')
        continuar()

    elif escolha_user == 4:
        if lista_tarefa:
            exibir_tarefas(lista_tarefa, ' Suas tarefas ')
            tarefa_concluir = validar_numero_input('Digite o número da tarefa que deseja marcar como concluída: ',
                                                   len(lista_tarefa))
            tarefa_concluida = lista_tarefa.pop(tarefa_concluir - 1)
            lista_tarefa_conclusas.append(tarefa_concluida)
            print(f'Tarefa "{tarefa_concluida}" marcada como concluída.')
        else:
            print('Você não possui tarefas pendentes.')
        continuar()

    elif escolha_user == 5:
        exibir_tarefas(lista_tarefa_conclusas, ' Tarefas concluídas ')
        continuar()

    elif escolha_user == 6:
        print('Saindo do programa...')
        break

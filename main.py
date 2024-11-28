tarefas = []
estados = []

def adicionar_tarefa(nome):
    if nome.strip():  # Verifica se o nome não está vazio ou com apenas espaços
        tarefas.append(nome)
        estados.append("pendente")
        print(f'Tarefa "{nome}" adicionada com sucesso!')
    else:
        print("O nome da tarefa não pode estar vazio!")

def marcar_concluida(nome):
    if nome in tarefas:
        indice = tarefas.index(nome)
        estados[indice] = "concluída"
        print(f'Tarefa "{nome}" marcada como concluída!')
    else:
        print(f'Tarefa "{nome}" não encontrada!')

def remover_tarefa(nome):
    if nome in tarefas:
        indice = tarefas.index(nome)
        tarefas.pop(indice)
        estados.pop(indice)
        print(f'Tarefa "{nome}" removida com sucesso!')
    else:
        print(f'Tarefa "{nome}" não encontrada!')

def listar_tarefas():
    print("\nTarefas pendentes:")
    for i in range(len(tarefas)):
        if estados[i] == "pendente":
            print(f'- {tarefas[i]}')
    print("\nTarefas concluídas:")
    for i in range(len(tarefas)):
        if estados[i] == "concluída":
            print(f'- {tarefas[i]}')

def pesquisar_tarefa(nome):
    if nome in tarefas:
        indice = tarefas.index(nome)
        estado = estados[indice]
        print(f'Tarefa encontrada: "{nome}" - Estado: {estado}')
    else:
        print(f'Tarefa "{nome}" não encontrada!')

def menu():
    while True:
        print("\n1. Adicionar tarefa")
        print("2. Marcar tarefa como concluída")
        print("3. Remover tarefa")
        print("4. Listar tarefas")
        print("5. Pesquisar tarefa")
        print("6. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome da tarefa: ")
            adicionar_tarefa(nome)
        elif opcao == "2":
            nome = input("Digite o nome da tarefa a ser concluída: ")
            marcar_concluida(nome)
        elif opcao == "3":
            nome = input("Digite o nome da tarefa a ser removida: ")
            remover_tarefa(nome)
        elif opcao == "4":
            listar_tarefas()
        elif opcao == "5":
            nome = input("Digite o nome da tarefa para pesquisa: ")
            pesquisar_tarefa(nome)
        elif opcao == "6":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

menu()
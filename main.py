import json
from funcs import *


# opções válidas do menu que o usuário pode selecionar
opcoes_validas_menu = ["1", "2", "3", "4", "5"]



# loop principal do programa
while True:


    # exibe o menu principal do programa
    exibe_menu_principal()


    # entra em um loop onde o usuário deve selecioanar uma opção válida no menu para que possa sair do
    # loop
    while True:

        escolha_usuario = str(input("Escolha uma opção: ")).strip()

        if escolha_usuario in opcoes_validas_menu:

            break

        print("\033[1;31mOpção inválida. Tente novamente com uma opção válida. \033[m")

    


    # Usuário seleciona a opção "1" = Adicionar Tarefa
    if escolha_usuario == "1":

        tarefa = str(input("Digite a tarefa: ")).strip() + "\n"

        try:

            with open("tarefas a fazer.json", "r", encoding="utf-8") as arquivo:

                lista_tarefas = json.load(arquivo)

        except (FileNotFoundError, json.JSONDecodeError):

            lista_tarefas = []

        lista_tarefas.append(tarefa)


        with open("tarefas a fazer.json", "w", encoding="utf-8") as arquivo:

            json.dump(lista_tarefas, arquivo, ensure_ascii=False, indent=4)

    # Usuário seleciona opção "2" = remover tarefa
    elif escolha_usuario == "2":

        pass
    
    # Usuário seleciona opção "3" = mover tarefa
    elif escolha_usuario == "3:":

        pass


    # Usuário seleciona opção "4" = listar tarefas
    elif escolha_usuario == "4":

        lista_de_tarefas = ["tarefas a fazer.json", "tarefas fazendo no momento.json", "tarefas feitas.json"]

        exibe_menu_tarefas()

        while True:

            escolha_usuario = str(input("Escolha qual lista de tarefas você deseja ver: ")).strip()

            if escolha_usuario in ["1", "2", "3"]:

                escolha_usuario = int(escolha_usuario) - 1

                break

            print("\033[1;31mOpção inválida. Tente novamente com uma opção válida. \033[m")

        lista_de_tarefas_a_visualizar = lista_de_tarefas[escolha_usuario]

        try:

            with open("tarefas a fazer.json", "r", encoding="utf8") as arquivo:
                
                lista_tarefas = json.load(arquivo)

                print(f'''Tarefas em "{lista_de_tarefas_a_visualizar}" ''')


                for indice, tarefa in enumerate(lista_tarefas):

                    print(f"{indice + 1} - {tarefa}")

        except (FileNotFoundError, json.JSONDecodeError):

            print("\033[1;31m A lista de tarefas está vazia ou não existe.\033[m")

            
        

    # Usuário seleciona opção "5" = sair do programa
    elif escolha_usuario == "5":

        quit()


    # Usuário seleciona opção inválida
    else:
        
        pass



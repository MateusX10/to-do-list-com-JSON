import json
from funcs import *


# opções válidas do menu que o usuário pode selecionar
opcoes_validas_menu = ["1", "2", "3", "4", "5"]



with open("tarefas fazendo no momento.json", "a+", encoding="utf-8") as arquivo:

    pass


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

        lista_de_tarefas = ["tarefas a fazer.json", "tarefas fazendo no momento.json", "tarefas feitas"]

        exibe_menu_tarefas()

        while True:

            escolha_usuario = str(input("Qual lista de tarefas deseja remover? ")).strip()

            if escolha_usuario in ["1", "2", "3"]:

                break

            print("\033[1;31mOpção inválida. Tente novamente com uma opção válida. \033[m")

        lista_de_tarefas_a_ter_o_item_removido = lista_de_tarefas[int(escolha_usuario) - 1]

        with open(lista_de_tarefas_a_ter_o_item_removido, "r", encoding="utf-8") as arquivo:

            lista_tarefas = json.load(arquivo)

        for posicao, tarefa in enumerate(lista_tarefas):

            print(f"{posicao + 1} - {tarefa}")

        numero_da_tarefa_a_ser_removida = int(input("Número da tarefa a ser removida: ")) - 1

        while True:

            if (numero_da_tarefa_a_ser_removida + 1) in range(1, len(lista_tarefas) + 1):

                break

            print("\033[1;31mOpção inválida. Tente novamente com uma opção válida. \033[m")

        lista_tarefas.pop(numero_da_tarefa_a_ser_removida)


        with open(lista_de_tarefas_a_ter_o_item_removido, "w", encoding="utf-8") as arquivo:

            json.dump(lista_tarefas, arquivo, ensure_ascii=False, indent=4)

            

    
    # Usuário seleciona opção "3" = mover tarefa
    elif escolha_usuario == "3":

        lista_de_tarefas = ["tarefas a fazer.json", "tarefas fazendo no momento.json", "tarefas feitas.json"]
        exibe_menu_tarefas()

        while True:

            escolha_usuario = str(input("Escolha qual lista de tarefas você deseja mover: ")).strip()

            if escolha_usuario in ["1", "2", "3"]:

                escolha_usuario = int(escolha_usuario) - 1

                break

            print("\033[1;31mOpção inválida. Tente novamente com uma opção válida. \033[m")


        lista_tarefas = lista_de_tarefas[escolha_usuario]


        with open(lista_tarefas, "r+", encoding="utf-8") as arquivo:

            lista_tarefas_extraidas = json.load(arquivo)

            for posicao, tarefa in enumerate(lista_tarefas_extraidas):

                print(f"{posicao + 1} - {tarefa}")

        while True:

            tarefa_a_ser_movida = int(input("Digite o número da tarefa que deseja mover: ")) - 1

            if (tarefa_a_ser_movida + 1) in range(1, len(lista_tarefas_extraidas) + 1):

                break
            print("\033[1;31mOpção inválida. Tente novamente com uma opção válida. \033[m")

        tarefa_a_ser_movida = lista_tarefas_extraidas[tarefa_a_ser_movida]

        lista_tarefas_extraidas.remove(tarefa_a_ser_movida)

        with open(lista_tarefas, "w", encoding="utf-8") as arquivo:
            
            json.dump(lista_tarefas_extraidas, arquivo, ensure_ascii=False, indent=4)

        exibe_menu_tarefas()

        while True:

            escolha_usuario = str(input("Escolha para onde deseja mover a tarefa: ")).strip()

            if escolha_usuario in ["1", "2", "3"]:

                escolha_usuario = int(escolha_usuario) - 1

                break

            print("\033[1;31mOpção inválida. Tente novamente com uma opção válida. \033[m")
        

        destino_da_tarefa_a_ser_movida = lista_de_tarefas[escolha_usuario]


        try:

            with open(destino_da_tarefa_a_ser_movida, "r", encoding="utf-8") as arquivo:

                lista_tarefas_destino = json.load(arquivo)


        except (FileNotFoundError, json.JSONDecodeError):

            lista_tarefas_destino = []


        lista_tarefas_destino.append(tarefa_a_ser_movida)

        with open(destino_da_tarefa_a_ser_movida, "w", encoding="utf-8") as arquivo:

            json.dump(lista_tarefas_destino, arquivo, ensure_ascii=False, indent=4)


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

            with open(lista_de_tarefas_a_visualizar, "r", encoding="utf8") as arquivo:
                
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



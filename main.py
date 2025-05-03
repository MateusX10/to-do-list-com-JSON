import json
from funcs import *


# opções válidas do menu que o usuário pode selecionar
opcoes_validas_menu = ["1", "2", "3", "4", "5"]



# loop principal do programa
while True:


    # exibe o menu principal do programa
    exibe_menu()


    # entra em um loop onde o usuário deve selecioanar uma opção válida no menu para que possa sair do
    # loop
    while True:

        escolha_usuario = str(input("Escolha uma opção: ")).strip()

        if escolha_usuario in opcoes_validas_menu:

            break

        print("\033[1;31mOpção inválida. Tente novamente com uma opção válida. \033[m")

    


    # Usuário seleciona a opção "1" = Adicionar Tarefa
    if escolha_usuario == "1":

        pass


    # Usuário seleciona opção "2" = remover tarefa
    elif escolha_usuario == "2":

        pass
    
    # Usuário seleciona opção "3" = mover tarefa
    elif escolha_usuario == "3:":

        pass


    # Usuário seleciona opção "4" = listar tarefas
    elif escolha_usuario == "4":

        pass

    # Usuário seleciona opção "5" = sair do programa
    elif escolha_usuario == "5":

        quit()


    # Usuário seleciona opção inválida
    else:
        
        pass



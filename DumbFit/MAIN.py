from func import *
limpador()
carregar_alunos()

while True:

    # UI
    mostrador()
    x = int(input("Digite o menu que deseja abrir: "))
    limpador()

    # 1 - Cadastrar Aluno
    if x == 1:
        limpador()
        cadastrador()

    # 2 - Imprimir Cadastros
    elif x == 2:
        limpador()
        impressora_menu()

    # 3 - Buscar Aluno por ID
    elif x == 3:
        limpador()
        buscador_id()

    # 4 - Filtar Alunos por IMC
    elif x == 4:
        limpador()
        buscador_imc()

    # 5 - Salvar e Sair
    elif x == 5:
        salvar_alunos()
        break

    # INPUT_ERROR!
    else:
        print("Digite uma opcao valida!")

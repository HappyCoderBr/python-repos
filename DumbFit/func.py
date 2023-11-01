'''func'''
import os
import json

alunos = []


def mostrador():
    '''mostrador da GUI'''
    print('''
************************************************
*               CADASTRADOR DUMBFIT            *  
************************************************
          
          
MENU:         
1 - Cadastrar Aluno
2 - Imprimir Cadastros
3 - Buscar Aluno por ID
4 - Filtar Alunos por IMC
5 - Salvar e Sair
          ''')


def voltar_menu():
    '''func que volta ao menu'''
    input("Deseja voltar ao menu? (ENTER)")
    limpador()


def limpador():
    '''limpa o terminal e sai do main looping'''
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def cadastrador():
    '''Cadastrar Aluno (MENU: 1)'''
    print("CADASTRAMENTO\n\n\n")
    while True:
        nome_i = str(input("Nome: "))
        idade_i = int(input("Idade: "))
        peso_i = float(input("Peso(kg): "))
        altura_i = float(input("Altura(m): "))
        sexo_i = str(input("Sexo(M/F): "))
        mensalidade_i = int(input("Mensalidade: "))

        print(f"\nAluno:    {nome_i}    cadastrado com sucesso!\n")

        aluno = {
            "id": str(len(alunos) + 1).zfill(5),

            # "id": len(alunos) + 1,
            "nome": nome_i,
            "idade": idade_i,
            "peso": peso_i,
            "altura": altura_i,
            "imc": int(peso_i/(altura_i*altura_i)),
            "sexo": sexo_i,
            "mensalidade": mensalidade_i

        }

        alunos.append(aluno)

        prosseguir_cadastrador = input(
            "Deseja prosseguir o cadastramento? (s/n): ")
        if prosseguir_cadastrador != "s":
            limpador()
            break
        limpador()


def impressora_menu():
    '''Imprimir Cadastros (MENU: 2)'''
    print(f"ALUNOS CADASTRADOS: {len(alunos)}\n\n\n")
    if len(alunos) == 0:
        print("Nenhum aluno foi registrado ainda")
    for aluno in alunos:
        print(f'''
ID:           {aluno["id"]}
Aluno:        {aluno["nome"]}
Idade:        {aluno["idade"]} 
Peso:         {aluno["peso"]} Kg
Altura:       {aluno["altura"]} m
IMC:          {aluno["imc"]}
Sexo:         {aluno["sexo"]}
Mensalidade:  {aluno["mensalidade"]}

''')
    voltar_menu()


def buscador_id():
    '''busca alunos no cadastro pelo ID'''
    print("BUSCADOR de ID:\n\n\n")
    while True:
        id_i = str(input("Digite o ID do aluno: "))
        counter_id = 0
        for aluno in alunos:
            if id_i == aluno["id"]:
                counter_id = 1
                print(f'''
ID:           {aluno["id"]}
Aluno:        {aluno["nome"]}
Idade:        {aluno["idade"]} 
Peso:         {aluno["peso"]} Kg
Altura:       {aluno["altura"]} m
IMC:          {aluno["imc"]}
Sexo:         {aluno["sexo"]}
Mensalidade:  {aluno["mensalidade"]}


    ''')
        if counter_id == 0:
            print("\nNenhum aluno foi encontrado com esse ID!\n")

        prosseguir_buscador_id = input(
            "Deseja prosseguir a busca por ID? (s/n): ")
        if prosseguir_buscador_id != "s":
            limpador()
            break
        limpador()


def buscador_imc():
    '''Filtar Alunos por IMC (MENU: 4)'''
    print("BUSCADOR de IMC:\n\n\n")
    while True:
        imc_i = float(input("Digite qual IMC procurar: "))
        counter_imc = 0
        for aluno in alunos:
            if imc_i == aluno["imc"]:
                counter_imc = 1
                print(f'''
ID:           {aluno["id"]}
Aluno:        {aluno["nome"]}
Idade:        {aluno["idade"]} 
Peso:         {aluno["peso"]} Kg
Altura:       {aluno["altura"]} m
IMC:          {aluno["imc"]}
Sexo:         {aluno["sexo"]}
Mensalidade:  {aluno["mensalidade"]}

    ''')
        if counter_imc == 0:
            print("\nNenhum aluno foi encontrado com esse IMC!\n")

        prosseguir_buscador_imc = input(
            "Deseja prosseguir a busca por IMC? (s/n): ")
        if prosseguir_buscador_imc != "s":
            limpador()
            break
        else:
            limpador()


def carregar_alunos():
    '''Carrega os dados dos alunos do arquivo alunos.json'''
    global alunos
    try:
        with open('alunos.json', 'r', encoding="utf-8") as file_read:
            alunos = json.load(file_read)
            print("Dados dos alunos carregados com sucesso!")
    except FileNotFoundError:
        print("Arquivo 'alunos.json' não encontrado.")


def salvar_alunos():
    '''Salva os dados dos alunos no arquivo alunos.json'''
    with open('alunos.json', 'w', encoding="utf-8") as file_saver:
        json.dump(alunos, file_saver, indent=4, separators=[',', ':'])
    print("Dados dos alunos salvos com sucesso!")

'''translator'''
import os
from deep_translator import GoogleTranslator
import nltk
from termcolor import cprint


def limpador():
    '''limpa o terminal e sai do main looping'''
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


#!!! SCRIPT SHOULD BE IN THE SAME FOLDER AS THE FILES, script wont be translated


while True:
    resposta = 's'  # Defina 'resposta' antes do segundo loop while
    while True:
        limpador()
        diretorio = input("Digite o local da pasta sem aspas: ")
        print(f"\nLocal selecionada: {diretorio}\n")
        if os.path.isdir(diretorio):
            break
        else:
            print("O diretório fornecido não existe.")
            resposta = input("Deseja tentar novamente? (s/n): ")
            if resposta.lower() != 's':
                break
    if resposta != 's':
        limpador()
        print("Tradutor Exterminado")
        break

    #!!! SPECIFY the folder that files are
    all_files = os.listdir(diretorio)

    files_list = []
    for names in all_files:
        #!!! SPECIFY file format
        if names.endswith(".txt"):
            files_list.append(names)

    x = 1
    str_translated = 'TRANSLATED'
    cprint(
        f"\n----------------  Files selected:  {len(files_list)}  ----------------\n", "black", "on_white", attrs=["bold"])

    while x <= len(files_list):

        with open(f"{files_list[x-1]}", "r", encoding="utf-8") as readfile:
            file1_stuff = readfile.read()
            file1_stuff = nltk.tokenize.sent_tokenize(file1_stuff)

        with open(f"{str_translated}_{files_list[x-1]}", "w", encoding="utf-8") as writefile:
            for sentence in file1_stuff:
                #!!! SPECIFY the target language
                translated = GoogleTranslator(
                    source='auto', target='pt').translate(sentence)
                writefile.write(translated)

        with open(f"{str_translated}_{files_list[x-1]}", "r", encoding="utf-8") as readwfile:
            file2_stuff = readwfile.read()

        cprint(
            f"\nFile name:                 {files_list[x-1]}", "light_yellow")
        cprint(
            f"Translated file name:      {str_translated}_{files_list[x-1]}", "magenta")
        cprint(f"Translated file lenght:    {len(file2_stuff)}", "cyan")
        cprint(
            f"Completed:                 {x}/{len(files_list)}\n", "light_green")

        x = x+1

    cprint(
        f"---------------  Files translated:  {len(files_list)}  ---------------\n", "white", "on_light_green", attrs=["bold"])

    denovo = input("Deseja executar o programado em outro diretorio? (s/n)")
    if denovo == 's':
        limpador()
    else:
        limpador()
        print("Tradutor Exterminado")
        break

#!!! CHECK LINES 10,17,35   <3
#!!! SCRIPT SHOULD BE IN THE SAME FOLDER AS THE FILES, script wont be translated

import sys
from termcolor import colored, cprint
import nltk
from deep_translator import GoogleTranslator
import os

#!!! SPECIFY the folder that files are
all_files = os.listdir(
    r"C:\Users\loren\OneDrive\Área de Trabalho\scriptmae - Copia")


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

    cprint(f"\nFile name:                 {files_list[x-1]}", "light_yellow")
    cprint(
        f"Translated file name:      {str_translated}_{files_list[x-1]}", "magenta")
    cprint(f"Translated file lenght:    {len(file2_stuff)}", "cyan")
    cprint(
        f"Completed:                 {x}/{len(files_list)}\n", "light_green")

    x = x+1

cprint(
    f"---------------  Files translated:  {len(files_list)}  ---------------\n", "white", "on_light_green", attrs=["bold"])

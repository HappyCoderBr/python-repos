import nltk
from deep_translator import GoogleTranslator
import os


all_files = os.listdir(
    r"C:\Users\loren\OneDrive\Área de Trabalho\scriptmae - Copia")  #pathway dir

x = 1
traduzida = 'TRADUZIDA'  #updated file name
while x <= len(all_files):

    with open(f"{all_files[x-1]}", "r", encoding="utf-8") as readfile:
        file1_stuff = readfile.read()
        file1_stuff = nltk.tokenize.sent_tokenize(file1_stuff)
        print(all_files[x-1])
        print(len(file1_stuff))

    with open(f"{traduzida}_{all_files[x-1]}", "w", encoding="utf-8") as writefile:
        for sentence in file1_stuff:
            translated = GoogleTranslator(
                source='auto', target='pt').translate(sentence)
            writefile.write(translated)

    with open(f"{traduzida}_{all_files[x-1]}", "r", encoding="utf-8") as readwfile:
        file2_stuff = readwfile.read()
        print(len(file2_stuff))

    x = x+1

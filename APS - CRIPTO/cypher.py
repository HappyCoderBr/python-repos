''' 
    UNIP-APS-CRIPTO
            antes de executar o script instale a bilioteca:
                pip install cryptography
'''

import os
import base64
from cryptography.fernet import Fernet


def limpador():
    '''limpa o terminal'''
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def continuar():
    '''continuar ou nao'''
    print("\nAperte ENTER para continuar")
    input()


def gerar_chave():
    '''cria uma chave de 32 bytes aleatorios'''
    chave = base64.urlsafe_b64encode(os.urandom(32))
    return chave


def criptografar(chave, frase):
    '''criptografa uma frase digitada'''
    f = Fernet(chave)
    frase_criptografada = f.encrypt(frase.encode())
    return frase_criptografada


def descriptografar(chave, frase_criptografada):
    '''desciptografa uma frase digitada'''
    f = Fernet(chave)
    frase_descriptografada = f.decrypt(frase_criptografada).decode()
    return frase_descriptografada


def main():
    '''loop principal que se executa ate usuario desejar'''
    chave = gerar_chave()
    while True:
        limpador()
        print('''\033[1;32m MENU:
              
1 - criptografar uma frase
2 - descriptografar uma frase
3 - sair.\n''')
        opcao = input()

        if opcao == '1':
            limpador()
            print("Digite a frase que você deseja criptografar (até 128 caracteres):\n")
            frase = input()

            if len(frase) > 128:
                print("A frase é muito longa. Tente novamente.\n")
                continue
            frase_criptografada = criptografar(chave, frase)
            print("\nFrase criptografada:", frase_criptografada.decode('utf-8'))
            continuar()

        elif opcao == '2':
            limpador()
            print("Digite a frase criptografada que você deseja descriptografar:\n")
            frase_criptografada = input().encode()
            try:
                frase_descriptografada = descriptografar(
                    chave, frase_criptografada)
                print("\nFrase descriptografada:", frase_descriptografada)
            except:
                print(
                    "Não foi possível descriptografar a frase. Verifique se a frase criptografada está correta.\n")
            continuar()

        elif opcao == '3':
            limpador()
            print("Programa finalizado!")
            break

        else:
            print("Opção inválida. Tente novamente.\n")


if __name__ == "__main__":
    main()

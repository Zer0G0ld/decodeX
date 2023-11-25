# Authors : Zer0
# Sobre : Projeto OpenSource de quebra de senha visando
# ajudar aqueles que querem aprender sobre criptografia 
# e os White Hat que visam ajudar a previnir futuros ataques

import hashlib
import os

def md5(text):
    return hashlib.md5(text.encode()).hexdigest()

def sha256(text):
    return hashlib.sha256(text.encode()).hexdigest()

def sha1(text):
    return hashlib.sha1(text.encode()).hexdigest()

def break_hash():
    # Caminho para as pastas
    current_folder = os.path.dirname(os.path.abspath(__file__))
    wordlist_folder = os.path.join(current_folder, 'wordlist')
    hashs_folder = os.path.join(current_folder, 'hashs')

    # Verifica se a pasta existem, se não, cria
    for folder in [wordlist_folder, hashs_folder]:
        if not os.path.exist(folder):
            os.makedirs(folder)

    # Caminho para o arquivo de saida


if __name__ == "__main__":
    output_file = input("Digite o nome do arquivo de saída (incluindo a extensão .txt): ")

    print('''

    [ 1 ] MD5
    [ 2 ] SHA-256
    [ 3 ] SHA-17

    ''')

    inputUser = int(input(">> "))

    if inputUser == 1:
        break_hash(output_file, md5)

    elif inputUser == 2:
        break_hash(output_file, sha256)

    elif inputUser == 3:
        break_hash(output_file, sha1)

    else:
        print("Escolha inválida.")

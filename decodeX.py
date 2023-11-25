import hashlib
import os
import datetime

def md5(text):
    return hashlib.md5(text.encode()).hexdigest()

def sha256(text):
    return hashlib.sha256(text.encode()).hexdigest()

def sha1(text):
    return hashlib.sha1(text.encode()).hexdigest()

def sha224(text):
    return hashlib.sha224(text.encode()).hexdigest()

def sha3_512(text):
    return hashlib.sha3_512(text.encode()).hexdigest()

def break_hash(encryption_function):
    # Caminho para as pastas
    current_folder = os.path.dirname(os.path.abspath(__file__))
    wordlist_folder = os.path.join(current_folder, 'wordlist')
    hashs_folder = os.path.join(current_folder, 'hashs')

    # Verifica se a pasta existe, se não, cria
    for folder in [wordlist_folder, hashs_folder]:
        if not os.path.exists(folder):
            os.makedirs(folder)

    # Nome do arquivo de saída baseado na criptografia escolhida e na data atual
    date_today = datetime.date.today().strftime("%Y-%m-%d")
    output_file = f"{encryption_function.__name__}_{date_today}.txt"
    exit_path = os.path.join(hashs_folder, output_file)

    with open(exit_path, 'w') as output_file:
        for filename in os.listdir(wordlist_folder):
            wordlist_path = os.path.join(wordlist_folder, filename)
            with open(wordlist_path, 'r') as word_file:
                words = [line.strip() for line in word_file.readlines()]
            
            for word in words:
                word_hash = encryption_function(word)
                output_file.write(f"{word_hash} == {word}\n")
                print(f"[+] Hash Adicionada: {word_hash} == {word} [+]")

if __name__ == "__main__":
    print('''
         #                           #         m    m
      mmm#   mmm    mmm    mmm    mmm#   mmm    #  #
     #" "#  #"  #  #"  "  #" "#  #" "#  #"  #    ##
     #   #  #""""  #      #   #  #   #  #""""   m""m
     "#m##  "#mm"  "#mm"  "#m#"  "#m##  "#mm"  m"  "m

    [ 1 ] MD5
    [ 2 ] SHA-256
    [ 3 ] SHA-1
    [ 4 ] SHA-224
    [ 5 ] SHA3-512

    ''')

    inputUser = int(input(">> "))

    if inputUser == 1:
        break_hash(md5)

    elif inputUser == 2:
        break_hash(sha256)

    elif inputUser == 3:
        break_hash(sha1)

    elif inputUser == 4:
        break_hash(sha224)

    elif inputUser == 5:
        break_hash(sha3_512)

    else:
        print("Escolha inválida.")


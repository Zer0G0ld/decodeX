# Authors : Zer0
# Sobre : Projeto OpenSource de quebra de senha visando
# ajudar aqueles que querem aprender sobre criptografia 
# e os White Hat que visam ajudar a previnir futuros ataques

import sys
import os
import glob

# Adiciona o caminho dos modulos ao PYTHONPATH
current_dir = os.path.dirname(os.path.abspath(__file__))
modules_dir = os.path.join(current_dir, 'modules')
sys.path.append(modules_dir)

# Importa todos os módulos da pasta 'Modules' 
module_files = glob.glob(os.path.join(modules_dir, "*.py"))

for module_file in module_files:
    module_name = os.path.splitext(os.path.basename(module_file))[0]
    __import__ (module_name)

def menu():
    print('''

    [ 1 ] MD5
    [ 2 ] SHA-256
    [ 3 ] SHA-1

    ''')

    try:
        inputUser = int(input(">> "))
    except Exception as Error:
        print("Erro ao tentar entender o que você digitou : " + str(Error))

menu()

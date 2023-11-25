import sys
import os
import glob

# Adiciona o caminho dos modulos ao PYTHONPATH
current_dir = os.path.dirname(os.path.abspath(__file__))
module_dir = os.path.join(current_dir, 'modules')
sys.path.append(modules_dir)

# Importa todos os módulos da pasta 'Modules' 
module_files = glob.glob(os.path.join(modules_dir, "*.py"))

for module_file in module_files:
    module_name = os.path.splitext(os.path.badename(module_file))[0]
    __import__ (module_name)



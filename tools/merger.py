import os
import re
import sys

def merge(source_dir, main_file):

    
    
    # Récupération des fichiers .py dans le dossier cible
    local_files = [
        f for f in os.listdir(target_dir) 
        if f.endswith('.py') and 
        os.path.isfile(os.path.join(target_dir, f))
    ]
    
    if main_file not in local_files:
        print(f"Erreur: {main_file} non trouvé")
        sys.exit(1)

    # Nouveau : Dictionnaire des fonctions par module
    full_path_files = {f: os.path.join(target_dir, f) for f in local_files}
    local_modules = {os.path.splitext(f)[0]: f for f in local_files}
    local_functions = {}
    
    for module_name, file in local_modules.items():
        with open(full_path_files[file], 'r') as f:
            content = f.read()
        # Détection des fonctions avec regex
        functions = re.findall(r'^def\s+(\w+)', content, flags=re.MULTILINE)
        local_functions[module_name] = functions

    # Analyse des dépendances (inchangé)
    dependencies = {f: set() for f in local_files}
    pattern_import = re.compile(r'^import\s+([\w ,]+)')
    pattern_from = re.compile(r'^from\s+([\w]+)\s+import')

    for file in local_files:
        with open(full_path_files[file], 'r') as f:
            content = f.readlines()
        
        for line in content:
            line_clean = line.strip().split('#')[0]
            
            if line_clean.startswith('import '):
                match = pattern_import.match(line_clean)
                if match:
                    modules = [m.strip() for m in match.group(1).split(',')]
                    for mod in modules:
                        if mod in local_modules:
                            dependencies[file].add(local_modules[mod])
            
            elif line_clean.startswith('from '):
                match = pattern_from.match(line_clean)
                if match:
                    mod = match.group(1)
                    if mod in local_modules:
                        dependencies[file].add(local_modules[mod])

    # Tri topologique (inchangé)
    visited = set()
    order = []
    
    def visit(file):
        if file not in visited:
            visited.add(file)
            for dep in dependencies[file]:
                visit(dep)
            order.append(file)
    
    visit(main_file)

    # Traitement des lignes avec remplacement
    external_imports = set()
    merged_code = []
    
    for file in order:
        with open(full_path_files[file], 'r') as f:
            content = f.readlines()
        
        for line in content:
            code_part = line.split('#')[0].rstrip()
            comment_part = line[line.find('#'):] if '#' in line else ''
            
            # Nouveau : Remplacement module.fonction -> fonction
            modified = False
            for module in local_functions:
                for func in local_functions[module]:
                    pattern = re.compile(rf'\b{module}\.{func}\b')
                    new_code, count = pattern.subn(func, code_part)
                    if count > 0:
                        code_part = new_code
                        modified = True
            
            if modified:
                line = code_part + ('  ' + comment_part if comment_part else '') + '\n'

            # Gestion des imports (inchangé)
            if code_part.startswith(('import ', 'from ')):
                modules = []
                if code_part.startswith('import '):
                    parts = code_part[6:].split(',')
                    modules = [p.strip().split()[0] for p in parts]
                elif code_part.startswith('from '):
                    match = pattern_from.match(code_part)
                    if match:
                        modules = [match.group(1)]
                
                is_external = all(mod not in local_modules for mod in modules)
                if is_external:
                    external_imports.add(line.strip())
            else:
                merged_code.append(line)

    # Écriture finale
    with open('../build/lvc.py', 'w') as f:
        f.write('\n'.join(sorted(external_imports))) 
        f.write('\n\n')
        f.writelines(merged_code)







if __name__ == '__main__':

    if len(sys.argv) != 3:
            print("Usage: python merger.py <source_dir> <fichier_principal.py>")
            sys.exit(1)
        
    target_dir = sys.argv[1]
    main_file = sys.argv[2]


    merge(target_dir, main_file)




    # os.system("cython --embed -o tmp/final.c tmp/final.py")
    # os.system("gcc -I/usr/include/python3.12 -o tmp/final tmp/final.c -lpython3.12")



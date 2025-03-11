#!/usr/bin/env python3
import os
import sys
import re

def is_import_line(line):
    """Retourne True si la ligne est une instruction d'import."""
    stripped = line.strip()
    return stripped.startswith("import ") or stripped.startswith("from ")

def extract_module_from_import(line):
    """Extrait le nom du module d'une ligne d'import."""
    stripped = line.strip()
    if stripped.startswith("import "):
        # Exemple : "import module", "import module as alias" ou "import module1, module2"
        modules_part = stripped[len("import "):]
        first_module = modules_part.split(",")[0].strip()
        return first_module.split()[0]
    elif stripped.startswith("from "):
        # Exemple : "from module import quelque_chose"
        parts = stripped.split()
        if len(parts) >= 2:
            return parts[1]
    return None

def extract_definitions(lines):
    """Extrait l'ensemble des définitions (classes et fonctions) d'un fichier."""
    defs = set()
    pattern = re.compile(r'^\s*(def|class)\s+(\w+)\s*[\(:]')
    for line in lines:
        m = pattern.match(line)
        if m:
            defs.add(m.group(2))
    return defs

def replace_internal_references(line, internal_defs):
    """
    Remplace dans une ligne toutes les occurences de module.nom par nom,
    pour chaque module interne dont on connaît les définitions.
    """
    for module, names in internal_defs.items():
        for name in names:
            # Recherche "module.name" avec des limites de mots
            pattern = re.compile(r'\b' + re.escape(module) + r'\.' + re.escape(name) + r'\b')
            line = pattern.sub(name, line)
    return line

def extract_main_blocks(lines, modules_internes, external_imports, internal_defs):
    """
    Parcourt les lignes d'un fichier pour extraire le contenu en supprimant
    les imports internes et en remplaçant les références internes.
    Si un bloc d'exécution (if __name__ == "__main__":) est détecté, il est extrait.
    
    Retourne un tuple (new_lines, main_blocks) où new_lines contient le contenu
    sans les blocs d'exécution et main_blocks est une liste des blocs extraits.
    """
    new_lines = []
    main_blocks = []
    # Regex pour détecter le point d'entrée
    pattern_main = re.compile(r'^(\s*)if\s+__name__\s*==\s*[\'"]__main__[\'"]\s*:')
    i = 0
    while i < len(lines):
        line = lines[i]
        m = pattern_main.match(line)
        if m:
            # On détecte le bloc d'exécution
            main_indent = len(m.group(1))
            block_lines = [line]
            i += 1
            # On récupère les lignes indentées faisant partie du bloc
            while i < len(lines):
                next_line = lines[i]
                # On inclut les lignes vides
                if next_line.strip() == "":
                    block_lines.append(next_line)
                    i += 1
                    continue
                indent = len(next_line) - len(next_line.lstrip())
                if indent > main_indent:
                    block_lines.append(next_line)
                    i += 1
                else:
                    break
            main_blocks.append("".join(block_lines))
        else:
            if is_import_line(line):
                mod = extract_module_from_import(line)
                if mod in modules_internes:
                    i += 1
                    continue
                else:
                    external_imports.add(line.strip())
                    i += 1
                    continue
            # Remplacement des références internes dans la ligne
            new_line = replace_internal_references(line, internal_defs)
            new_lines.append(new_line)
            i += 1
    return new_lines, main_blocks

def main():
    if len(sys.argv) != 3:
        print("Usage: python merge_scripts.py <dossier> <fichier_sortie.py>")
        sys.exit(1)
    
    dossier = sys.argv[1]
    fichier_sortie = sys.argv[2]
    
    if not os.path.isdir(dossier):
        print(f"Erreur : {dossier} n'est pas un dossier valide.")
        sys.exit(1)
    
    # Récupération de tous les fichiers .py du dossier
    fichiers_py = [f for f in os.listdir(dossier) if f.endswith(".py")]
    if not fichiers_py:
        print("Aucun fichier .py trouvé dans le dossier.")
        sys.exit(1)
    
    # Ensemble des modules internes (noms de fichiers sans extension)
    modules_internes = {os.path.splitext(f)[0] for f in fichiers_py}
    
    # Dictionnaire associant chaque module à ses définitions (fonctions/classes)
    internal_defs = {}
    # Contenu brut de chaque fichier
    file_contents = {}
    # Ensemble des imports externes
    external_imports = set()
    # Contenu traité de chaque fichier
    merged_contents = {}
    # Liste globale des blocs d'exécution extraits
    all_main_blocks = []
    
    # Lecture des fichiers et extraction des définitions
    for fichier in sorted(fichiers_py):
        chemin = os.path.join(dossier, fichier)
        with open(chemin, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        file_contents[fichier] = lines
        module_name = os.path.splitext(fichier)[0]
        if module_name in modules_internes:
            internal_defs[module_name] = extract_definitions(lines)
    
    # Traitement de chaque fichier : extraction des blocs main et remplacement des références
    for fichier, lines in file_contents.items():
        new_lines, main_blocks = extract_main_blocks(lines, modules_internes, external_imports, internal_defs)
        merged_contents[fichier] = new_lines
        all_main_blocks.extend(main_blocks)
    
    # Écriture du fichier fusionné
    with open(fichier_sortie, 'w', encoding='utf-8') as out:
        # D'abord, écrire les imports externes dédupliqués
        for imp in sorted(external_imports):
            out.write(imp + "\n")
        out.write("\n")
        
        # Ensuite, concaténer le contenu de chaque fichier
        for fichier, lines in merged_contents.items():
            out.write(f"# Début du fichier {fichier}\n")
            out.write("".join(lines))
            out.write(f"\n# Fin du fichier {fichier}\n\n")
        
        # Enfin, placer les blocs d'exécution à la fin du fichier fusionné
        if all_main_blocks:
            out.write("# Point d'entrée d'exécution\n")
            for block in all_main_blocks:
                out.write(block)
                out.write("\n")

if __name__ == '__main__':
    main()

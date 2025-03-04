import re

# Lire le contenu des deux fichiers
with open('versionner.py', 'r') as file1:
    content1 = file1.read()

with open('modules.py', 'r') as file2:
    content2 = file2.read()

# Remplacer les références de la forme `modules.fonction` par `fonction`
content1_modified = re.sub(r'modules\.(\w+)', r'\1', content1)

# Combiner les contenus
combined_content = content2 + '\n' + content1_modified

# Écrire le contenu combiné dans un nouveau fichier
with open('combined_script.py', 'w') as combined_file:
    combined_file.write(combined_content)

print("Les fichiers ont été fusionnés avec succès dans 'combined_script.py'.")



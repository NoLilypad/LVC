#!/bin/bash

# Vérifie si un argument a été fourni
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 script.py"
    exit 1
fi

python merger.py "$1"


# Récupère le script Python
script_python="tmp/final.py"

# Vérifie si le fichier existe
if [ ! -f "$script_python" ]; then
    echo "Le fichier $script_python n'existe pas."
    exit 1
fi

# Extrait le nom du fichier sans l'extension pour nommer l'exécutable
nom_executable="${script_python%.py}"

# Convertit le script Python en C avec Cython
cython --embed -o "${nom_executable}.c" "$script_python"

# Vérifie si la conversion a réussi
if [ $? -ne 0 ]; then
    echo "La conversion du script Python en C a échoué."
    exit 1
fi

# Compile le fichier .c avec les options spécifiées
gcc -I/usr/include/python3.12 -o "$nom_executable" "${nom_executable}.c" -lpython3.12

# Vérifie si la compilation a réussi
if [ $? -eq 0 ]; then
    echo "Compilation réussie. L'exécutable est nommé $nom_executable."
else
    echo "La compilation a échoué."
    exit 1
fi

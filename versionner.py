import os
import shutil
import sys
import modules

VERDIR = 'ver'

def uk():
    print('???')


# Dictionnaire des fonctions et leur commandes associées
functionToCommands = {
    modules.init: ['init', 'i'],
    uk: []
}

# Créer un dictionnaire pour mapper chaque commande/alias à sa fonction
commandMap = {}
for fonction, commands in functionToCommands.items():
    for command in commands:
        commandMap[command] = fonction


def main():
    # Get first arg
    arg = sys.argv[1]
    commandMap[arg](VERDIR)
    


if __name__ == "__main__":
    #main()
    pass
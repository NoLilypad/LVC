import sys

import misc 
import init
import remove


CONFIG = {
    'VERSION': '3.0',
    'HASH_ALGO': 'sha256',
}



def loadCommands():
    # Dictionnaire des fonctions et leur commandes associées
    functionToCommands = {
        init.init: ['init','i'],
        remove.remove: ['remove','r']
    }

    # Créer un dictionnaire pour mapper chaque commande/alias à sa fonction
    commandMap = {}
    for fonction, comms in functionToCommands.items():
        for command in comms:
            commandMap[command] = fonction
    return commandMap



def main():
    commandMap = loadCommands()
    args = sys.argv

    if len(args) == 1:
        misc.home(CONFIG)
        return

    command = args[1]
    arguments = args[2:]

    if command not in commandMap:
        misc.unknownCommand(CONFIG)
        return
    else:
        commandMap[command](CONFIG)
        return
    


if __name__ == "__main__":
    main()

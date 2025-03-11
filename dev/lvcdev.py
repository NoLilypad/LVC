import sys

from misc import Misc

from init import Init
from help import Help

CONFIG = {
    #'LVC_DIR': '.lvc',
    #'DATA_FILE': 'data',
    'VERSION': '2.0',
    #'IGNORE_FILE': '.lvcignore',
    'HASH_ALGO': 'sha256',
    #'VERSIONS_DIR': 'versions',
    #'OBJECTS_DIR' : 'objects'
}



def loadCommands():
    # Dictionnaire des fonctions et leur commandes associées
    functionToCommands = {
        Init: ['init', 'i'],
        Help: ['help', 'h']
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
        commandObject = Misc(CONFIG)
        commandObject.home()
        return

    commandName = args[1]
    arguments = args[2:]

    if commandName not in commandMap:
        commandObject = Misc(CONFIG)
        commandObject.unknownCommand()
        return
    else:
        commandObject = commandMap[commandName](CONFIG)
        commandObject.command(arguments)
        return
    


if __name__ == "__main__":
    main()

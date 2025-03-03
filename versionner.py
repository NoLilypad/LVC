import os
import shutil
import sys
import modules


CONFIG = {
    'VERDIR': '.ver',
    'DATAFILE': 'data'
}





def loadCommands():
    # Dictionnaire des fonctions et leur commandes associées
    functionToCommands = {
        modules.init: ['init', 'i'],
        modules.version: ['version','v'],
        modules.destroy: ['destroy', 'd'],
        modules.list: ['list', 'l'],
        modules.switch: ['switch','s']
    }

    # Créer un dictionnaire pour mapper chaque commande/alias à sa fonction
    commandMap = {}
    for fonction, commands in functionToCommands.items():
        for command in commands:
            commandMap[command] = fonction
    return commandMap




def main(commandMap):
    # Gets arguments
    args = sys.argv
    # If called without arguments
    if len(args) == 1:
        modules.home()
        return
    command = args[1]
    arguments = args[2:]
    if command not in commandMap:
        modules.unknownCommand()
        return
    else:
        commandMap[command](CONFIG, arguments)
        return
    


if __name__ == "__main__":
    commandMap = loadCommands()
    main(commandMap)
    
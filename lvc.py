import os
import shutil
import sys
import commands


CONFIG = {
    'LVC_DIR': '.lvc',
    'DATA_FILE': 'data',
    'VERSION': '2.0',
    'IGNORE_FILE': 'ignore',
    'HASH_ALGO': 'sha256',
    'VERSIONS_DIR': 'versions',
    'OBJECTS_DIR' : 'objects'
}





def loadCommands():
    # Dictionnaire des fonctions et leur commandes associées
    functionToCommands = {
        commands.init: ['init', 'i'],
        commands.version: ['version','v'],
        commands.destroy: ['destroy', 'd'],
        commands.list: ['list', 'l'],
        commands.switch: ['switch','s']
    }

    # Créer un dictionnaire pour mapper chaque commande/alias à sa fonction
    commandMap = {}
    for fonction, comms in functionToCommands.items():
        for command in comms:
            commandMap[command] = fonction
    return commandMap




def main(commandMap):
    # Gets arguments
    args = sys.argv
    # If called without arguments
    if len(args) == 1:
        commands.home(CONFIG)
        return
    command = args[1]
    arguments = args[2:]
    if command not in commandMap:
        commands.unknownCommand()
        return
    else:
        commandMap[command](CONFIG, arguments)
        return
    


if __name__ == "__main__":
    commandMap = loadCommands()
    main(commandMap)
    
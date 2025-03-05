import os
import shutil
import sys

import misc
import init
import destroy
import version
import list
import switch



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
        init.init: ['init', 'i'],
        version.version: ['version','v'],
        destroy.destroy: ['destroy', 'd'],
        list.list: ['list', 'l'],
        switch.switch: ['switch','s']
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
        misc.home(CONFIG)
        return
    command = args[1]
    arguments = args[2:]
    if command not in commandMap:
        misc.unknownCommand()
        return
    else:
        commandMap[command](CONFIG, arguments)
        return
    


if __name__ == "__main__":
    commandMap = loadCommands()
    main(commandMap)
    
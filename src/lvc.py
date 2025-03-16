import sys

import misc 
import initProject
import removeProject
import addVersion
import listVersions
import switchVersions
import help

CONFIG = {
    'VERSION': '3.0',
    'HASH_ALGO': 'sha256',
}



def loadCommands():
    # Dictionnaire des fonctions et leur commandes associées
    functionToCommands = {
        initProject.initProject: ['init','i'],
        removeProject.removeProject: ['remove','r'],
        addVersion.addVersion: ['version','v'],
        listVersions.listVersions: ['list','l'],
        switchVersions.switchVersions: ['switch','s'],
        help.help: ['help','h']
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
        commandMap[command](CONFIG, arguments)
        return
    


if __name__ == "__main__":
    main()

from datetime import datetime
import csv
import fnmatch
import hashlib
import os
import re
import shutil
import sys
import time


def home(CONFIG):
    version = CONFIG['VERSION']
    workingDirectory = os.getcwd()
    lvcDirectory = os.path.join(workingDirectory, CONFIG['LVC_DIR'])

    # Checks if versionner directory exists
    isInit = os.path.isdir(lvcDirectory)
    if isInit:
        message = 'Activé dans le dossier courant'
    else:
        message = "Pas activé dans le dossier courant"

    print(f'[LVC version {version}] {message}')
    print("Type 'lvc help' or 'lvc h' for help ")

def unknownCommand():
    print('Unknown command')

def help(CONFIG, arguments):
    version = CONFIG['VERSION']
    print(f'[LVC version {version}] ')
    print("""
          lvc    [init|version <comment>|list|switch <ID>|destroy|help]
          
        * init              : initialize lvc in the current directory. Add -n to avoid adding a .lvcignore file
        * version <comment> : creates a new snapshot of the working directory, with a optional comment
        * list              : lists all versions in working directory
        * switch  <ID>      : switches to version with version ID given with list
        * destroy           : deactivates lvc in current directory
        * help              : displays this help   """)




def destroy(CONFIG, arguments):
    workingDirectory = os.getcwd()
    lvcDirectory = os.path.join(workingDirectory, CONFIG['LVC_DIR'])
    isInit = os.path.isdir(lvcDirectory)
    if isInit:
        shutil.rmtree(lvcDirectory)
        print('Repo erased')
        return
    else:
        print('No repo in current directory')
        return
    

    

def readIgnore(ignoreFilePath):
    with open(ignoreFilePath, 'r') as ignore_file:
        ignorePatterns = [line.strip() for line in ignore_file if line.strip()]
    
    for pattern in ignorePatterns:
        try:
            pass
        except re.error:
            continue
    return ignorePatterns



def getElements(directory, ignorePatterns):
    elements = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            completePath = os.path.join(root,file)
            relPath = os.path.relpath(completePath, directory)
            # Gestion de IGNORE_FILE
            if not any((relPath.endswith(pattern) or (pattern.endswith('/') and pattern in relPath)) for pattern in ignorePatterns):
                elements.append(relPath)
    return sorted(elements)

def getFileHash(filePath, algorithm='sha256'):
    hashFunction = hashlib.new(algorithm)
    with open(filePath,'rb') as file:
        # Read the file in chunks of 8192 bytes
        while chunk := file.read(8192):
            hashFunction.update(chunk)
    return(hashFunction.hexdigest())

def getVersionHash(elementsInfo, algorithm='sha256'):
    hashFunction = hashlib.new(algorithm)
    for element in elementsInfo:
        hashFunction.update(element[0].encode('utf-8'))
        hashFunction.update(element[1].encode('utf-8'))
    hashFunction.update(str(time.time()).encode('utf-8'))
    return(hashFunction.hexdigest())

def createObject(elementPath, elementHash, objectsDirectory):
    with open(elementPath, 'rb') as file:
                data = file.readlines()
    with open(os.path.join(objectsDirectory, elementHash), 'wb') as file:
        file.writelines(data)

def createFile(elementPath, elementHash, objectsDirectory):
    with open(os.path.join(objectsDirectory, elementHash), 'rb') as file:
                data = file.readlines()
    with open(elementPath, 'wb') as file:
        file.writelines(data)

def createObjects(objectsDirectory, elementsInfo):
    for element in elementsInfo:
        elementPath, elementHash = element
        elementObjectPath = os.path.join(objectsDirectory, elementHash)
        if not os.path.isfile(elementObjectPath):
            createObject(elementPath, elementHash, objectsDirectory)

def createVersionFile(versionPath, elementsInfo):
    with open(versionPath, 'w') as file:
        writer = csv.writer(file)
        for element in elementsInfo:
            elementPath, elementHash = element
            writer.writerow([elementHash, elementPath])

def readVersionFile(versionPath):
    data = []
    with open (versionPath,'r',newline='') as file:
        reader = csv.reader(file)
        for line in reader:
            data.append(line)
    return(data)
             

def writeVersion(filePath, data):
    with open(filePath, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)



def readVersions(filePath):
    data = []
    with open(filePath, 'r', newline='') as file:
        reader = csv.reader(file)
        for line in reader:
            data.append(line)
    return data










def list(CONFIG, arguments):
    HASH_ALGO = CONFIG['HASH_ALGO']
    workingDirectory = os.getcwd()
    lvcDirectory = os.path.join(workingDirectory, CONFIG['LVC_DIR'])
    dataFilePath = os.path.join(workingDirectory, CONFIG['LVC_DIR'], CONFIG['DATA_FILE'])
    versionsDirectory = os.path.join(workingDirectory, CONFIG['LVC_DIR'], CONFIG['VERSIONS_DIR'])
    objectsDirectory = os.path.join(workingDirectory, CONFIG['LVC_DIR'], CONFIG['OBJECTS_DIR'])
    ignoreFilePath = os.path.join(workingDirectory, CONFIG['IGNORE_FILE'])

    # Checks if versionner directory exists
    isInit = os.path.isdir(lvcDirectory)
    if not isInit:
        print('No repo in current folder')
        return
    
    # Reads version file
    data = readVersions(dataFilePath)

    # Formats data for display
    formattedData = []
    IdBuffer = []
    for version in data:
        idLength = 8
        versionId = version[0][:idLength]
        while versionId in IdBuffer:
            idLength += 1
            versionId = version[0][:idLength]
        versionId = versionId + ' ' * (10 - len(versionId))    # Prendre en compte le changement de tailler pour l'espacement des string
        IdBuffer.append(versionId)
        comment = version[1]
        created = datetime.fromtimestamp(int(version[2]))
        createdFormatted = created.strftime('%Y-%m-%d %H:%M:%S')

        formattedData.append([versionId, comment, createdFormatted])

    # Prints formatted versions
    print('VERSION ID  CREATED              COMMENT')
    for version in formattedData:
        print(f'{version[0]}  {version[2]} {version[1]}')




def init(CONFIG, arguments):
    HASH_ALGO = CONFIG['HASH_ALGO']
    workingDirectory = os.getcwd()
    lvcDirectory = os.path.join(workingDirectory, CONFIG['LVC_DIR'])
    dataFilePath = os.path.join(workingDirectory, CONFIG['LVC_DIR'], CONFIG['DATA_FILE'])
    versionsDirectory = os.path.join(workingDirectory, CONFIG['LVC_DIR'], CONFIG['VERSIONS_DIR'])
    objectsDirectory = os.path.join(workingDirectory, CONFIG['LVC_DIR'], CONFIG['OBJECTS_DIR'])
    ignoreFilePath = os.path.join(workingDirectory, CONFIG['IGNORE_FILE'])

    # Get no ignore flag
    if len(arguments) >= 1 and arguments[0] == '-n':    
        noIgnore = True
    else:
        noIgnore = False

    # Checks if versionner directory exists
    isInit = os.path.isdir(lvcDirectory)
    if isInit:
        print('Repo already created in current folder')
        return
    
    # Creates LV_DIR
    os.mkdir(lvcDirectory)

    # Creates the data file
    with open(dataFilePath,'w') as file:
        file.writelines('')

    # Creates the versions directory
    os.mkdir(versionsDirectory)

    # Creates the objects directory
    os.mkdir(objectsDirectory)

    # Creates a .ignore file
    if not noIgnore:
        with open(ignoreFilePath,'w') as file:
            file.writelines('.lvc/ \n')

    print('Repo created in current directory')




def switch(CONFIG, arguments):
    HASH_ALGO = CONFIG['HASH_ALGO']
    workingDirectory = os.getcwd()
    lvcDirectory = os.path.join(workingDirectory, CONFIG['LVC_DIR'])
    dataFilePath = os.path.join(workingDirectory, CONFIG['LVC_DIR'], CONFIG['DATA_FILE'])
    versionsDirectory = os.path.join(workingDirectory, CONFIG['LVC_DIR'], CONFIG['VERSIONS_DIR'])
    objectsDirectory = os.path.join(workingDirectory, CONFIG['LVC_DIR'], CONFIG['OBJECTS_DIR'])
    ignoreFilePath = os.path.join(workingDirectory, CONFIG['IGNORE_FILE'])

    # Récupération du version Id
    if len(arguments) >= 1:
        versionShortId = arguments[0]
    else:
        print('Need version ID to switch')
        return
    
    # Checks if versionner directory existsME
    isInit = os.path.isdir(lvcDirectory)
    if not isInit:
        print('No repo in current folder')
        return
    
    # Vérifie le format de la version ID donné
    if len(versionShortId) < 8:
        print('Not a version')
        return
    
    # Récupère les versions
    versions = readVersions(dataFilePath)
    
    # Trouve la version
    # TROUVER UNE MEILLEURE MANIERE DE FAIRE
    version = False
    for ver in versions:
        if ver[0].startswith(versionShortId):
            version = ver
            break
    if version == False:
        print('Not a version')
        return
    
    versionHash = version[0]

    # Récupère les infos d'arborescence de la version
    versionTree = readVersionFile(os.path.join(versionsDirectory, versionHash))

    # Get ignore patterns list
    ignorePatterns = []
    if os.path.isfile(ignoreFilePath):
        ignorePatterns = readIgnore(ignoreFilePath)
    

    # Récupère les fichiers actuels
    currentTree = getElements(workingDirectory, ignorePatterns)
    
    # Efface les dossiers courants
    for element in currentTree:
        fullPath = os.path.join(workingDirectory, element)
        os.remove(fullPath)

    for element in versionTree:
        elementFullPath = os.path.join(workingDirectory, element[1])
        elementHash = element[0]
        createFile(elementFullPath, elementHash, objectsDirectory)

    print('Done')
    
    
    




def version(CONFIG, arguments):
    HASH_ALGO = CONFIG['HASH_ALGO']
    workingDirectory = os.getcwd()
    lvcDirectory = os.path.join(workingDirectory, CONFIG['LVC_DIR'])
    dataFilePath = os.path.join(workingDirectory, CONFIG['LVC_DIR'], CONFIG['DATA_FILE'])
    versionsDirectory = os.path.join(workingDirectory, CONFIG['LVC_DIR'], CONFIG['VERSIONS_DIR'])
    objectsDirectory = os.path.join(workingDirectory, CONFIG['LVC_DIR'], CONFIG['OBJECTS_DIR'])
    ignoreFilePath = os.path.join(workingDirectory, CONFIG['IGNORE_FILE'])
    # Récupération du commentaire
    if len(arguments) >= 1:
        comment = arguments[0]
    else:
        comment = ''
    # Checks if versionner directory exists
    isInit = os.path.isdir(lvcDirectory)
    if not isInit:
        print('No repo in current folder')
        return
    
    # Get ignore patterns list
    ignorePatterns = []
    if os.path.isfile(ignoreFilePath):
        ignorePatterns = readIgnore(ignoreFilePath)
    
    # Get files list
    elements = getElements(workingDirectory, ignorePatterns)


    # Hashes files
    elementsInfo = []
    for element in elements:
        elementPath = os.path.join(workingDirectory, element)
        hash = getFileHash(elementPath, HASH_ALGO)
        elementsInfo.append((element, hash))

    # Generates version hash
    versionHash = getVersionHash(elementsInfo, HASH_ALGO)

    # Copies file in objects if not already present
    createObjects(objectsDirectory, elementsInfo)

    # Writes version data in version file
    versionPath = os.path.join(versionsDirectory, versionHash)
    createVersionFile(versionPath, elementsInfo)


    # Writes version in data
    writeVersion(dataFilePath, [versionHash, comment, int(time.time())])






CONFIG = {
    'LVC_DIR': '.lvc',
    'DATA_FILE': 'data',
    'VERSION': '2.0',
    'IGNORE_FILE': '.lvcignore',
    'HASH_ALGO': 'sha256',
    'VERSIONS_DIR': 'versions',
    'OBJECTS_DIR' : 'objects'
}





def loadCommands():
    # Dictionnaire des fonctions et leur commandes associées
    functionToCommands = {
        init: ['init', 'i'],
        version: ['version','v'],
        destroy: ['destroy', 'd'],
        list: ['list', 'l'],
        switch: ['switch','s'],
        help: ['help', 'h']
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
        home(CONFIG)
        return
    command = args[1]
    arguments = args[2:]
    if command not in commandMap:
        unknownCommand()
        return
    else:
        commandMap[command](CONFIG, arguments)
        return
    


if __name__ == "__main__":
    commandMap = loadCommands()
    main(commandMap)
    
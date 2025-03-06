import os
import utils

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
    
    # Checks if versionner directory exists
    isInit = os.path.isdir(lvcDirectory)
    if not isInit:
        print('No repo in current folder')
        return
    
    # Vérifie le format de la version ID donné
    if len(versionShortId) < 8:
        print('Not a version')
        return
    
    # Récupère les versions
    versions = utils.readVersions(dataFilePath)
    
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
    versionTree = utils.readVersionFile(os.path.join(versionsDirectory, versionHash))

    # Get ignore patterns list
    ignorePatterns = []
    if os.path.isfile(ignoreFilePath):
        ignorePatterns = utils.readIgnore(ignoreFilePath)
    

    # Récupère les fichiers actuels
    currentTree = utils.getElements(workingDirectory, ignorePatterns)
    
    # Efface les dossiers courants
    for element in currentTree:
        fullPath = os.path.join(workingDirectory, element)
        os.remove(fullPath)

    for element in versionTree:
        elementFullPath = os.path.join(workingDirectory, element[1])
        elementHash = element[0]
        utils.createFile(elementFullPath, elementHash, objectsDirectory)

    print('Done')
    
    
    



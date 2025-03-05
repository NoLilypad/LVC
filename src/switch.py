import os
import shutil
import utils


def switch(CONFIG, arguments):
    LVC_DIR = CONFIG['LVC_DIR']
    DATA_FILE = CONFIG['DATA_FILE']
    HASH_ALGO = CONFIG['HASH_ALGO']
    VERSIONS_DIR = CONFIG['VERSIONS_DIR']
    OBJECTS_DIR = CONFIG['OBJECTS_DIR']
    workingDirectory = os.getcwd()
    # Récupération du commentaire
    if len(arguments) >= 1:
        comment = arguments[0]
    else:
        comment = ''
    # Checks if versionner directory exists
    isInit = os.path.isdir(f'{workingDirectory}/{LVC_DIR}')
    if not isInit:
        print('No repo in current folder')
        return
    
    # Get ignore patterns list
    ignoreFilePath = os.path.join(workingDirectory, IGNORE_FILE)
    if os.path.isfile(ignoreFilePath):
        ignorePatterns = utils.readIgnore(ignoreFilePath)
    
    # Get files list
    elements = utils.getElements(workingDirectory, ignorePatterns)


    # Hashes files
    elementsInfo = []
    for element in elements:
        hash = utils.getFileHash(workingDirectory, element, HASH_ALGO)
        elementsInfo.append((element, hash))

    # Generates version hash
    versionHash = utils.getVersionHash(elementsInfo, HASH_ALGO)

    # Copies file in objects if not already present
    for element in elementsInfo:
        elementPath, elementHash = element
        elementObjectPath = os.path.join(workingDirectory, LVC_DIR, OBJECTS_DIR, elementHash)
        if not os.path.isfile(elementObjectPath):
            utils.createObject(elementPath, elementHash, os.path.join(workingDirectory, LVC_DIR, OBJECTS_DIR))


    # Writes version data in version file
    with open(os.path.join(workingDirectory, LVC_DIR, VERSIONS_DIR, versionHash), 'w') as file:
        for element in elementsInfo:
            elementPath, elementHash = element
            file.writelines(f'{elementHash}|{elementPath}\n') 

    # Writes version in data
    with open(os.path.join(workingDirectory, LVC_DIR, DATA_FILE), 'a') as file:
        file.writelines(f'{versionHash}|{comment}\n')


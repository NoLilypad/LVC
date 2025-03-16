import os
import shutil
import utils
import time


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
        ignorePatterns = utils.readIgnore(ignoreFilePath)
    
    # Get files list
    elements = utils.getElements(workingDirectory, ignorePatterns)


    # Hashes files
    elementsInfo = []
    for element in elements:
        elementPath = os.path.join(workingDirectory, element)
        hash = utils.getFileHash(elementPath, HASH_ALGO)
        elementsInfo.append((element, hash))

    # Generates version hash
    versionHash = utils.getVersionHash(elementsInfo, HASH_ALGO)

    # Copies file in objects if not already present
    utils.createObjects(objectsDirectory, elementsInfo)

    # Writes version data in version file
    versionPath = os.path.join(versionsDirectory, versionHash)
    utils.createVersionFile(versionPath, elementsInfo)


    # Writes version in data
    utils.writeVersion(dataFilePath, [versionHash, comment, int(time.time())])



import os
import shutil
import utils


def version(CONFIG, arguments):
    LVC_DIR = CONFIG['LVC_DIR']
    DATA_FILE = CONFIG['DATA_FILE']
    HASH_ALGO = CONFIG['HASH_ALGO']
    VERSIONS_DIR = CONFIG['VERSIONS_DIR']
    OBJECTS_DIR = CONFIG['OBJECTS_DIR']
    IGNORE_FILE = CONFIG['IGNORE_FILE']
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
    ignorePatterns = []
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
    utils.createObjects(workingDirectory, LVC_DIR, OBJECTS_DIR, elementsInfo)


    # Writes version data in version file
    utils.createVersionFile(workingDirectory, LVC_DIR, VERSIONS_DIR, versionHash, elementsInfo)


    # Writes version in data
    utils.writeVersion(workingDirectory, LVC_DIR, DATA_FILE, versionHash, comment)


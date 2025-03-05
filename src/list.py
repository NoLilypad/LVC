import os
import shutil



def list(CONFIG, arguments):
    HASH_ALGO = CONFIG['HASH_ALGO']
    workingDirectory = os.getcwd()
    lvcDirectory = os.path.join(workingDirectory)
    dataFilePath = os.path.join(workingDirectory, CONFIG['LVC_DIR'], CONFIG['DATA_FILE'])
    versionsDirectory = os.path.join(workingDirectory, CONFIG['LVC_DIR'], CONFIG['VERSIONS_DIR'])
    objectsDirectory = os.path.join(workingDirectory, CONFIG['LVC_DIR'], CONFIG['OBJECTS_DIR'])
    ignoreFilePath = os.path.join(workingDirectory, CONFIG['IGNORE_FILE'])

    # Checks if versionner directory exists
    isInit = os.path.isdir(lvcDirectory)
    if not isInit:
        print('No repo in current folder')
        return

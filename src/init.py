import os
import shutil



def init(CONFIG, arguments):
    HASH_ALGO = CONFIG['HASH_ALGO']
    workingDirectory = os.getcwd()
    lvcDirectory = os.path.join(workingDirectory)
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
    isInit = os.path.isdir(os.path.join(workingDirectory, LVC_DIR))
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




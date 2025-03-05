import os
import shutil



def init(CONFIG, arguments):
    LVC_DIR = CONFIG['LVC_DIR']
    DATA_FILE = CONFIG['DATA_FILE']
    VERSIONS_DIR = CONFIG['VERSIONS_DIR']
    OBJECTS_DIR = CONFIG['OBJECTS_DIR']
    IGNORE_FILE = CONFIG['IGNORE_FILE']
    workingDirectory = os.getcwd()
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
    os.mkdir(os.path.join(workingDirectory, LVC_DIR))

    # Creates the data file
    with open(os.path.join(workingDirectory, LVC_DIR, DATA_FILE),'w') as file:
        file.writelines('')

    # Creates the versions directory
    os.mkdir(os.path.join(workingDirectory, LVC_DIR, VERSIONS_DIR))

    # Creates the objects directory
    os.mkdir(os.path.join(workingDirectory, LVC_DIR, OBJECTS_DIR))

    # Creates a .ignore file
    if not noIgnore:
        with open(os.path.join(workingDirectory, IGNORE_FILE),'w') as file:
            file.writelines('.lvc/ \n')

    print('Repo created in current directory')




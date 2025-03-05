import os
import shutil



def list(CONFIG, arguments):
    LVC_DIR = CONFIG['LVC_DIR']
    DATA_FILE = CONFIG['DATA_FILE']
    HASH_ALGO = CONFIG['HASH_ALGO']
    VERSIONS_DIR = CONFIG['VERSIONS_DIR']
    OBJECTS_DIR = CONFIG['OBJECTS_DIR']
    IGNORE_FILE = CONFIG['IGNORE_FILE']
    workingDirectory = os.getcwd()
    # Checks if versionner directory exists
    isInit = os.path.isdir(f'{workingDirectory}/{LVC_DIR}')
    if not isInit:
        print('No repo in current folder')
        return

    # Print first line
    print('VERSION ID   COMMENT')

    with open(os.path.join(workingDirectory,LVC_DIR,DATA_FILE),'r') as file:
        data = file.readlines()    
    for version in data:
        print(f'{version[:8]}     {version[9:][:-1]}')
    
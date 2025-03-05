import os
import shutil
import time
import uuid
import fnmatch
import re

import utils

def home(CONFIG):
    version = CONFIG['VERSION']
    print(f'LVC version {version}')

def unknownCommand():
    print('Unknown command')




def init(CONFIG, arguments):
    LVC_DIR = CONFIG['LVC_DIR']
    DATA_FILE = CONFIG['DATA_FILE']
    VERSIONS_DIR = CONFIG['VERSIONS_DIR']
    OBJECTS_DIR = CONFIG['OBJECTS_DIR']
    workingDirectory = os.getcwd()
    # Checks if versionner directory exists
    isInit = os.path.isdir(os.path.join(workingDirectory, LVC_DIR))
    if isInit:
        print('Repo already created in current folder')
        return
    
    
    os.mkdir(os.path.join(workingDirectory, LVC_DIR))
    # Creates the data file
    with open(os.path.join(workingDirectory, LVC_DIR, DATA_FILE),'w') as file:
        file.writelines('')
    # Creates the versions directory
    os.mkdir(os.path.join(workingDirectory, LVC_DIR, VERSIONS_DIR))
    # Creates the objects directory
    os.mkdir(os.path.join(workingDirectory, LVC_DIR, OBJECTS_DIR))
    print('Repo created in current directory')

def destroy(CONFIG, arguments):
    LVC_DIR = CONFIG['LVC_DIR']
    workingDirectory = os.getcwd()
    # Checks if versionner directory exists
    isInit = os.path.isdir(os.path.join(workingDirectory, LVC_DIR))
    if isInit:
        shutil.rmtree(os.path.join(workingDirectory, LVC_DIR))
        print('Repo erased')
        return
    else:
        print('No repo in current directory')
        return



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

    
    

    
    
    
        
    
    


            


    

def list():
    pass



def switch():
    pass


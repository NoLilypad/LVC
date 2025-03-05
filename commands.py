import os
import shutil
import time
import uuid
import fnmatch
import re

import utils

def home(CONFIG):
    version = CONFIG['VERSION']
    print(f'Versionner {version}')

def unknownCommand():
    print('Unknown command')




def init(CONFIG, arguments):
    VERDIR = CONFIG['VERDIR']
    DATAFILE = CONFIG['DATAFILE']
    VERSIONS_DIR = CONFIG['VERSIONS_DIR']
    OBJECTS_DIR = CONFIG['OBJECTS_DIR']
    workingDirectory = os.getcwd()
    # Checks if versionner directory exists
    isInit = os.path.isdir(os.path.join(workingDirectory, VERDIR))
    if isInit:
        print('Repo already created in current folder')
        return
    
    
    os.mkdir(os.path.join(workingDirectory, VERDIR))
    # Creates the data file
    with open(os.path.join(workingDirectory, VERDIR, DATAFILE),'w') as file:
        file.writelines('')
    # Creates the versions directory
    os.mkdir(os.path.join(workingDirectory, VERDIR, VERSIONS_DIR))
    # Creates the objects directory
    os.mkdir(os.path.join(workingDirectory, VERDIR, OBJECTS_DIR))
    print('Repo created in current directory')

def destroy(CONFIG, arguments):
    VERDIR = CONFIG['VERDIR']
    workingDirectory = os.getcwd()
    # Checks if versionner directory exists
    isInit = os.path.isdir(os.path.join(workingDirectory, VERDIR))
    if isInit:
        shutil.rmtree(os.path.join(workingDirectory, VERDIR))
        print('Repo erased')
        return
    else:
        print('No repo in current directory')
        return



def version(CONFIG, arguments):
    VERDIR = CONFIG['VERDIR']
    DATAFILE = CONFIG['DATAFILE']
    HASH_ALGO = CONFIG['FILE_HASH_ALGO']
    VERSIONS_DIR = CONFIG['VERSIONS_DIR']
    OBJECTS_DIR = CONFIG['OBJECTS_DIR']
    workingDirectory = os.getcwd()
    # Récupération du commentaire
    if len(arguments) >= 1:
        comment = arguments[0]
    else:
        comment = ''
    # Checks if versionner directory exists
    isInit = os.path.isdir(f'{workingDirectory}/{VERDIR}')
    if not isInit:
        print('No repo in current folder')
        return
    
    # Get files list and hash
    elements = utils.getElements(workingDirectory)
    elementsInfo = []
    for element in elements:
        hash = utils.getFileHash(workingDirectory, element, HASH_ALGO)
        fileInfo = (element, hash)
        elementsInfo.append(fileInfo)

    # Generates version id 
    versionId = utils.getVersionHash(elementsInfo, HASH_ALGO)

    # # Copies file in cache if not already present
    for element in elementsInfo:
        elementPath, elementHash = element
        print(elementPath)
        if not os.path.isfile(os.path.join(workingDirectory, VERDIR, OBJECTS_DIR, elementHash)):
            with open(os.path.join(workingDirectory, elementPath), 'r') as file:
                data = file.readlines()
            print(data)
            with open(os.path.join(VERDIR, OBJECTS_DIR, elementHash), 'w') as file:
                file.writelines(data)
    
    # Writes version data in version file
    with open(os.path.join(workingDirectory, VERDIR, VERSIONS_DIR, versionId), 'w') as file:
        for element in elementsInfo:
            elementPath, elementHash = element
            file.writelines(f'{elementHash}|{elementPath}\n') 

    # Writes version in data
    with open(os.path.join(workingDirectory, VERDIR, DATAFILE), 'a') as file:
        file.writelines(f'{versionId}|{comment}\n')

    
    

    
    
    
        
    
    


            


    

def list():
    pass



def switch():
    pass


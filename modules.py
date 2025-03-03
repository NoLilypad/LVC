import os
import shutil
import time
import uuid

def home():
    print('Versionner 1.0')

def unknownCommand():
    print('Unknown command')



def init(CONFIG, arguments):
    VERDIR = CONFIG['VERDIR']
    DATAFILE = CONFIG['DATAFILE']
    # Get working directory
    workingDirectory = os.getcwd()
    # Checks if versionner directory exists
    isInit = os.path.isdir(f'{workingDirectory}/{VERDIR}')
    if isInit:
        print('Repo already created in current folder')
        return
    os.mkdir(f'{workingDirectory}/{VERDIR}')
    with open(f'{workingDirectory}/{VERDIR}/{DATAFILE}','w') as file:
        file.writelines('')
    print('Repo created in current directory')

def destroy(CONFIG, arguments):
    VERDIR = CONFIG['VERDIR']
    # Get working directory
    workingDirectory = os.getcwd()
    # Checks if versionner directory exists
    isInit = os.path.isdir(f'{workingDirectory}/{VERDIR}')
    if isInit:
        shutil.rmtree(f'{workingDirectory}/{VERDIR}')
        print('Repo erased')
        return
    else:
        print('No repo in current directory')
        return
    


def version(CONFIG, arguments):
    comment = arguments[0]
    VERDIR = CONFIG['VERDIR']
    DATAFILE = CONFIG['DATAFILE']
    # Get working directory
    workingDirectory = os.getcwd()
    # Checks if versionner directory exists
    isInit = os.path.isdir(f'{workingDirectory}/{VERDIR}')
    if not isInit:
        print('No repo in current folder')
        return
    # Lists all files and directories
    objects = os.listdir(workingDirectory)
    objects.remove(VERDIR)
    # Creates version ID
    versionId = str(uuid.uuid4())[:8]
    # Writes in data
    with open(f'{workingDirectory}/{VERDIR}/{DATAFILE}','a') as file:
        file.writelines(f'{versionId}:{comment}\n')
    # Creates directory for files in VERDIR
    versionDirectoryPath = f'{workingDirectory}/{VERDIR}/{versionId}'
    os.mkdir(versionDirectoryPath)
    # Copies files in version directory
    for object in objects:
        objectPath = f'{workingDirectory}/{object}'
        if os.path.isfile(objectPath):
            shutil.copy2(objectPath, versionDirectoryPath)
        if os.path.isdir(objectPath):
            shutil.copytree(objectPath, f'{versionDirectoryPath}/{object}', copy_function=shutil.copy2)
    print('Done ! ')

    



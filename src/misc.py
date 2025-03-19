import os

from utils import isProjectVersioned
from Project import Project

def home(CONFIG):
    workingDirectory = os.getcwd()
    hashAlgorithm = CONFIG['HASH_ALGO'] 
    
    project = Project(workingDirectory, hashAlgorithm)

    if not project:
        print('[NO] No project in current directory')
    else:
        print(f'[INIT] Project initialized at : {workingDirectory}')
        if isProjectVersioned(project):
            print('[UP] Project directory versionned')
        else:
            print('[LATE] Project directory not up to last version')



    print(f" LVC version {CONFIG['VERSION']} Type 'lvc help' or 'lvc h' for help ")


def unknownCommand(CONFIG):
    print('Unknown command')

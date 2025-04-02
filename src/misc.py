import os

from utils import isProjectVersioned
from Project import Project

def home(CONFIG):
    workingDirectory = os.getcwd()
    hashAlgorithm = CONFIG['HASH_ALGO'] 
    
    project = Project(workingDirectory, hashAlgorithm)

    print(f"[LVC] LVC version {CONFIG['VERSION']} Type 'lvc help' or 'lvc h' for help ")

    if not project:
        print('[NO] No project in current directory')
    else:
        print(f'[INIT] Project initialized at : {workingDirectory}')
        if project.isVersioned():
            print('[UP]   Project directory versionned')
            head = project.getHead()
            print(f'[HEAD] {head}')
        else:
            print('[LATE] Project directory not up to last version')





def unknownCommand(CONFIG):
    print('Unknown command')

import os

from Project import Project

def home(CONFIG):
    workingDirectory = os.getcwd()
    hashAlgorithm = CONFIG['HASH_ALGO'] 
    
    project = Project(workingDirectory, hashAlgorithm)

    if not project:
        print('No project in current directory')
    else:
        print(f'Project initialized at : {workingDirectory}')



    print(f"[LVC version {CONFIG['VERSION']}] Type 'lvc help' or 'lvc h' for help ")


def unknownCommand(CONFIG):
    print('Unknown command')

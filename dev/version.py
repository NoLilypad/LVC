import os 

from project import Project


def version(CONFIG):
    HASH_ALGO = CONFIG['HASH_ALGO']
    
    workingDirectory = os.getcwd()

    project = Project(workingDirectory)
    
    if project:
        print('LVC project already setup in current directory')
        return
    
    project.build()

    print('LVC project builded in current directory')
import os 

from Project import Project


def initProject(CONFIG, arguments):    
    workingDirectory = os.getcwd()
    hashAlgorithm = CONFIG['HASH_ALGO'] 
    
    project = Project(workingDirectory, hashAlgorithm)
    
    if project:
        print('LVC project already setup in current directory')
        return
    
    project.write()

    print('LVC project builded in current directory')
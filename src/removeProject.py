import os 

from Project import Project


def removeProject(CONFIG, arguments):    
    workingDirectory = os.getcwd()
    hashAlgorithm = CONFIG['HASH_ALGO'] 
    
    project = Project(workingDirectory, hashAlgorithm)
    
    if not project:
        print('No LVC project in current directory')
        return
    
    project.erase()

    print('LVC project removed')
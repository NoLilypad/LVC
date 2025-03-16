import os

import Project


def listVersions(CONFIG, arguments):
    workingDirectory = os.getcwd()
    hashAlgorithm = CONFIG['HASH_ALGO'] 


    project = Project(workingDirectory, hashAlgorithm)
    
    if not project:
        print('No LVC project in current directory')
        return

    print(project.getVersion())
import os
import shutil

from Project import Project
from Version import Version


def version(CONFIG):
    workingDirectory = os.getcwd()
    hashAlgorithm = CONFIG['HASH_ALGO'] 
    
    project = Project(workingDirectory, hashAlgorithm)
    
    if not project:
        print('No LVC project in current directory')
        return
    
    head = project.getHead()

    version = Version(head, project)

    version.create(workingDirectory)

    # project.writeVersion(version)




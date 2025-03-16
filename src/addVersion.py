import os
import shutil

from Project import Project
from Version import Version


def addVersion(CONFIG, arguments):
    workingDirectory = os.getcwd()
    hashAlgorithm = CONFIG['HASH_ALGO'] 
    
    project = Project(workingDirectory, hashAlgorithm)
    
    if not project:
        print('No LVC project in current directory')
        return
    
    if len(arguments) >= 1:
        comment = arguments[0]
    else:
        comment = ''

    
    head = project.getHead()

    version = Version([head], comment, project)

    ignorePatterns = project.getIgnorePatterns()

    version.addElementsFromDirectory(workingDirectory, ignorePatterns)

    version.generateHash()

    project.writeVersion(version)

    project.setHead(version.hash)


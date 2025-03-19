import os
import shutil

from Project import Project
from Version import Version


def test(CONFIG, arguments):
    workingDirectory = os.getcwd()
    hashAlgorithm = CONFIG['HASH_ALGO'] 

    project = Project(workingDirectory, hashAlgorithm)
    
    if not project:
        print('No LVC project in current directory')
        return
    
    versions = project.getVersions()
    for version in versions:
        # version.addElementsFromVersionFile(os.path.join(project.versionsDirectory, version.hash))
        # version.generateHash()
        print(version.hashID)
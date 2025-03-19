import os
import shutil

from Project import Project
from Version import Version

import utils

def merge(CONFIG, arguments):
    workingDirectory = os.getcwd()
    hashAlgorithm = CONFIG['HASH_ALGO'] 
    
    project = Project(workingDirectory, hashAlgorithm)

    if not project:
        print('No LVC project in current directory')
        return

    if len(arguments) >= 1:
        versionId = arguments[0]
    else:
        print('Version needed to merge')
        return

    if len(versionId) < 8:
        print('Not a version')
        return
    
    if not utils.isProjectVersioned(project): 
        print('Project directory not updated to a version \n<lvc v> to create a new version')
        return
    
    versions = project.getVersions()
    if not any(version.hash.startswith(versionId) for version in versions):
        print('Not a version')
        return
    
    versionB = next((ver for ver in versions if ver.hash.startswith(versionId)), None)

    # version = Version([project.head], comment, project)
    
    
    

    
    

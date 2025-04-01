import os
import shutil

from Project import Project
from Version import Version

from utils import find_closest_common_ancestors

def test(CONFIG, arguments):
    workingDirectory = os.getcwd()
    hashAlgorithm = CONFIG['HASH_ALGO'] 

    project = Project(workingDirectory, hashAlgorithm)
    
    if not project:
        print('No LVC project in current directory')
        return
    
    versions = project.getVersions()
    for version in versions:
        print(version.hashID)

    find_closest_common_ancestors(versions[0], versions[1], project)
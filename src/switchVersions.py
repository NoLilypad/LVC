import os

from Project import Project
from Version import Version

def switchVersions(CONFIG, arguments):
    workingDirectory = os.getcwd()
    hashAlgorithm = CONFIG['HASH_ALGO'] 
    
    project = Project(workingDirectory, hashAlgorithm)

    if not project:
        print('No LVC project in current directory')
        return
    
    if len(arguments) == 1:
        versionId = arguments[0]
    else:
        print('Need version ID to switch')
        return

    if len(versionId) < 8:
        print('Not a version')
        return

    versions = project.getVersions()

    # Find a better way
    version = False
    for ver in versions:
        if ver.hash.startswith(versionId):
            version = ver
            break
    if version == False:
        print('Not a version')
        return
    
    versionFile = os.path.join(project.versionsDirectory, version.hash)
    
    version.addElementsFromVersionFile(versionFile)
    
    localVersion = Version(['Placeholder'],'placeholder', project)

    ignorePatterns = project.getIgnorePatterns()

    localVersion.addElementsFromDirectory(workingDirectory, ignorePatterns)

    for element in localVersion.elements:
        os.remove(os.path.join(workingDirectory, element.path))

    for element in version.elements:
        with open(os.path.join(project.objectsDirectory, element.hash), 'rb') as file:
            data = file.readlines()
        with open(os.path.join(workingDirectory, element.path), 'wb') as file:
            file.writelines(data)

    project.setHead(version.hash)

    



import os
from datetime import datetime

from Project import Project


def listVersions(CONFIG, arguments):
    workingDirectory = os.getcwd()
    hashAlgorithm = CONFIG['HASH_ALGO'] 


    project = Project(workingDirectory, hashAlgorithm)
    
    if not project:
        print('No LVC project in current directory')
        return

    versions = project.getVersions()

    # Formatting versions data to print
    formattedData = []
    for version in versions:
        versionId = version.hashID + ' ' * (10 - len(version.hashID))    
        comment = version.comment
        created = datetime.fromtimestamp(int(float(version.timestamp)))
        createdFormatted = created.strftime('%Y-%m-%d %H:%M:%S')

        formattedData.append([versionId, createdFormatted, comment])



    # Printing versions data
    print('VERSION ID  CREATED              COMMENT')
    for version in formattedData:
        print(f'{version[0]}  {version[1]}  {version[2]}')



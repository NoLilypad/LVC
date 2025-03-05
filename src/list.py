import os
import shutil
import utils
from datetime import datetime



def list(CONFIG, arguments):
    HASH_ALGO = CONFIG['HASH_ALGO']
    workingDirectory = os.getcwd()
    lvcDirectory = os.path.join(workingDirectory, CONFIG['LVC_DIR'])
    dataFilePath = os.path.join(workingDirectory, CONFIG['LVC_DIR'], CONFIG['DATA_FILE'])
    versionsDirectory = os.path.join(workingDirectory, CONFIG['LVC_DIR'], CONFIG['VERSIONS_DIR'])
    objectsDirectory = os.path.join(workingDirectory, CONFIG['LVC_DIR'], CONFIG['OBJECTS_DIR'])
    ignoreFilePath = os.path.join(workingDirectory, CONFIG['IGNORE_FILE'])

    # Checks if versionner directory exists
    isInit = os.path.isdir(lvcDirectory)
    if not isInit:
        print('No repo in current folder')
        return
    
    # Reads version file
    data = utils.readVersion(dataFilePath)

    # Formats data for display
    formattedData = []
    IdBuffer = []
    for version in data:
        idLength = 8
        versionId = version[0][:idLength]
        while versionId in IdBuffer:
            idLength += 1
            versionId = version[0][:idLength]
        versionId = versionId + ' ' * (10 - len(versionId))    # Prendre en compte le changement de tailler pour l'espacement des string
        IdBuffer.append(versionId)
        comment = version[1]
        created = datetime.fromtimestamp(int(version[2]))
        createdFormatted = created.strftime('%Y-%m-%d %H:%M:%S')

        formattedData.append([versionId, comment, createdFormatted])

    # Prints formatted versions
    print('VERSION ID  CREATED              COMMENT')
    for version in formattedData:
        print(f'{version[0]}  {version[2]} {version[1]}')


import os

class Command:
    def __init__(self, CONFIG):
        self.HASH_ALGO = CONFIG['HASH_ALGO']
        self.version = CONFIG['VERSION']    
        self.workingDirectory = os.getcwd()
        self.lvcDirectoryName = CONFIG['LVC_DIR']
        self.lvcDirectoryPath = os.path.join(self.workingDirectory, CONFIG['LVC_DIR'])
        self.dataFilePath = os.path.join(self.workingDirectory, CONFIG['LVC_DIR'], CONFIG['DATA_FILE'])
        self.versionsDirectoryPath = os.path.join(self.workingDirectory, CONFIG['LVC_DIR'], CONFIG['VERSIONS_DIR'])
        self.objectsDirectoryPath = os.path.join(self.workingDirectory, CONFIG['LVC_DIR'], CONFIG['OBJECTS_DIR'])
        self.ignoreFilePath = os.path.join(self.workingDirectory, CONFIG['IGNORE_FILE'])

    def isInit(self):
        # Checks if versionner directory exists in current directory
        return os.path.isdir(self.lvcDirectoryPath)

        
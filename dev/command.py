import os

class Command:
    def __init__(self, CONFIG):
        self.HASH_ALGO = CONFIG['HASH_ALGO']
        self.version = CONFIG['VERSION']    
        self.workingDirectory = os.getcwd()

    def isInit(self):
        # Checks if versionner directory exists in current directory
        return os.path.isdir(self.lvcDirectoryPath)

        
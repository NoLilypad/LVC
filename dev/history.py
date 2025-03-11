import os

class History:
    def __init__(self, directory, lvcDirectoryName):
        self.directory = directory
        self.versions = []

    def __str__(self):
        return(self.directory)
    
    # Creates history directory and tree
    def initDump(self):
            # Creates LV_DIR
        os.mkdir(os.path.join(self.directory, self.lvcDirectoryName))

        # Creates the data file
        with open(self.dataFilePath,'w') as file:
            file.writelines('')

        # Creates the versions directory
        os.mkdir(self.versionsDirectoryPath)

        # Creates the objects directory
        os.mkdir(self.objectsDirectoryPath)


        


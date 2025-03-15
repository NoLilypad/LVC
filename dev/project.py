import os
import shutil 


class Project:
    def __init__(self, workingDirectory):
        self.directory = workingDirectory
        self.lvcDirectory = os.path.join(workingDirectory,'.lvc')
        self.dataFile = os.path.join(self.lvcDirectory,'data')
        self.versionsDirectory = os.path.join(self.lvcDirectory,'versions')
        self.objectsDirectory = os.path.join(self.lvcDirectory,'objects')

    def __bool__(self):
        return  os.path.isdir(self.lvcDirectory)

    def __str__(self):
        return self.directory
    
    def build(self):
        os.mkdir(self.lvcDirectory)
        os.mkdir(self.versionsDirectory)
        os.mkdir(self.objectsDirectory)
        with open(self.dataFile,'w') as file:
            file.writelines('')

    def erase(self):
        shutil.rmtree(self.lvcDirectory)

        
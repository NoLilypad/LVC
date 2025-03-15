import os
import shutil 


class Project:
    def __init__(self, workingDirectory, hashAlgorithm):
        self.projectDirectory = workingDirectory
        self.hashAlgorithm = hashAlgorithm
        self.lvcDirectory = os.path.join(workingDirectory,'.lvc')
        self.projectFile = os.path.join(self.lvcDirectory,'project')
        self.versionsDirectory = os.path.join(self.lvcDirectory,'versions')
        self.objectsDirectory = os.path.join(self.lvcDirectory,'objects')
        self.headFile = os.path.join(self.lvcDirectory, 'head')
        self.ignoreFile = os.path.join(self.projectDirectory, '.lvcignore')
        self.configFile = os.path.join(self.lvcDirectory, 'config')

    def __bool__(self):
        return  os.path.isdir(self.lvcDirectory)

    def __str__(self):
        return self.projectDirectory
    
    def build(self):
        os.mkdir(self.lvcDirectory)
        os.mkdir(self.versionsDirectory)
        os.mkdir(self.objectsDirectory)
        with open(self.projectFile,'w') as file:
            file.writelines('')
        with open(self.headFile,'w') as file:
            file.writelines('')
        with open(self.configFile,'w') as file:
            file.writelines('')


    def erase(self):
        shutil.rmtree(self.lvcDirectory)

    def getHead(self):
        with open(self.headFile, 'r') as file:
            head = file.readline().strip()
        return head

    def getIgnorePatterns(self):
        if os.path.isfile(self.ignoreFile):
            with open(self.ignoreFile, 'r') as file:
                ignorePatterns = [line.strip() for line in file if line.strip()]
            return ignorePatterns
        else:
            return []
        
    def addVersion(self, version):
        pass




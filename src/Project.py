import os
import shutil 
import csv

from Version import Version

class Project:
    def __init__(self, workingDirectory, hashAlgorithm='sha256'):
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
    
    def write(self):
        os.mkdir(self.lvcDirectory)
        os.mkdir(self.versionsDirectory)
        os.mkdir(self.objectsDirectory)
        with open(self.projectFile,'w') as file:
            file.writelines('')
        with open(self.headFile,'w') as file:
            file.writelines('FIRST_ANCESTOR')
        with open(self.configFile,'w') as file:
            file.writelines('')


    def erase(self):
        shutil.rmtree(self.lvcDirectory)

    def getHead(self):
        with open(self.headFile, 'r') as file:
            head = file.readline().strip()
        return head

    def setHead(self, ref):
        with open(self.headFile, 'w') as file:
            file.writelines(ref)

    def getIgnorePatterns(self):
        if os.path.isfile(self.ignoreFile):
            with open(self.ignoreFile, 'r') as file:
                ignorePatterns = [line.strip() for line in file if line.strip()]
            return ignorePatterns
        else:
            return []
        
    def writeVersion(self, version):
        # Write version data in project file
        versionData = [version.hash, version.ancestors, version.comment, version.timestamp]
        with open(self.projectFile, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(versionData)

        # Creates version file in versions directory
        versionFile = os.path.join(self.versionsDirectory, version.hash)    
        with open(versionFile, 'w') as file:
            writer = csv.writer(file)
            for element in version.elements:
                writer.writerow([element.hash, element.path])


        # Creates elements in objects directory
        for element in version.elements:
            with open(element.path, 'rb') as file:
                data = file.readlines()
            with open(os.path.join(self.objectsDirectory, element.hash), 'wb') as file:
                file.writelines(data)


    def getVersions(self):
        versions = []
        with open (self.projectFile,'r',newline='') as file:
            reader = csv.reader(file)
            for line in reader:
                version = Version(ancestors=line[1], project=self, comment=line[2], timestamp=line[3], hash=line[0])
                versions.append(version)
        return(versions)

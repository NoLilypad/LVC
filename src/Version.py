import os
import hashlib
import time
import csv
import ast

from Element import Element

class Version:
    def __init__(self, ancestors, elements, comment, project, hash, hashID, timestamp): 
        self.ancestors = ancestors
        self.comment = comment
        self.elements = elements
        self.project = project
        self.hash = hash
        self.hashID = hashID
        self.timestamp = timestamp

    def __str__(self):
        return(self.hash)


    # For creating a version from the files on disk in the working directory
    @classmethod
    def fromDirectory(cls, directory, ancestors, comment, project):
        # Gets ignore patterns
        ignorePatterns = project.getIgnorePatterns()
        # Gets elements
        elements = cls.getElementsFromDirectory(directory, project)
        # Generates hash from elements
        hash, hashID = cls.generateHash(elements, project)
        # Creates timestamp
        timestamp = time.time()
        # Creates version instance
        version = cls(ancestors, elements, comment, project, hash, hashID, timestamp)
        return version

    # For retrieving a version only knowing its hash
    @classmethod
    def fromHash(cls, hash, project):
        with open (project.projectFile,'r',newline='') as file:
            reader = csv.reader(file)
            for line in reader:
                if line[0] == hash:
                    foundVersion = True
                    hash = line[0]
                    hashID = line[1]
                    # ast to read list from string, e.g. "['ancestor1', 'ancestor2']"
                    ancestors = ast.literal_eval(line[2])
                    comment = line[3]
                    timestamp = line[4]
        versionFilePath = os.path.join(project.versionsDirectory, hash)
        elements = cls.getElementsFromVersionFile(versionFilePath)
        version = cls(ancestors, elements, comment, project, hash, hashID, timestamp)
        return version
    
    # For getting version with Project.getVersions
    @classmethod
    def fromProject(cls, ancestors, comment, project, hash, hashID, timestamp):        
        versionFilePath = os.path.join(project.versionsDirectory, hash)
        elements = cls.getElementsFromVersionFile(versionFilePath)
        version = cls(ancestors, elements, comment, project, hash, hashID, timestamp)
        return version

    @classmethod
    def generateHash(cls, elements, project):
        # Generate version hash
        hashFunction = hashlib.new(project.hashAlgorithm)
        for element in elements:
            hashFunction.update(element.path.encode('utf-8'))
            hashFunction.update(element.hash.encode('utf-8'))
        hash = hashFunction.hexdigest()

        # Get version ID (shortened hash)
        versions = project.getVersions()
        versionsHashID = []
        # for version in versions:
        #     idLength = 8
        #     versionId = version.hash[:idLength]
        #     while versionId in versionsHashID:
        #         idLength += 1
        #         versionId = version.hash[:idLength] 
        for version in versions:
            versionsHashID.append(version.hashID)

        idLength = 8
        hashID = hash[:idLength]
        while hashID in versionsHashID:
                idLength += 1
                hashID = hash[:idLength]

        return (hash, hashID)


    @classmethod
    def getElementsFromDirectory(cls, directory, project):
        ignorePatterns = project.getIgnorePatterns()
        elements = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                completePath = os.path.join(root,file)
                relPath = os.path.relpath(completePath, directory)
                # Gestion de IGNORE_FILE
                if not any((relPath.endswith(pattern) or (pattern.endswith('/') and pattern in relPath)) for pattern in ignorePatterns):
                    element = Element.fromDirectory(relPath, project.hashAlgorithm)
                    elements.append(element)

        return elements

    @classmethod
    def getElementsFromVersionFile(cls, versionFile):
        elements = []
        with open (versionFile,'r',newline='') as file:
            reader = csv.reader(file)
            for line in reader:
                element = Element.fromHash(path=line[1], hash=line[0])
                elements.append(element)

        return elements
    


     
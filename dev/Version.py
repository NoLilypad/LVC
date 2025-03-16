import os
import hashlib
import time
import csv

from Element import Element

class Version:
    def __init__(self, ancestors, comment, project, hash = '', timestamp = time.time()):
        self.ancestors = ancestors
        self.comment = comment
        self.project = project
        self.elements = []
        self.hash = hash
        self.timestamp = timestamp

    def generateHash(self):
        hashFunction = hashlib.new(self.project.hashAlgorithm)
        for element in self.elements:
            hashFunction.update(element.path.encode('utf-8'))
            hashFunction.update(element.hash.encode('utf-8'))
            # hashFunction.update(str(time.time()).encode('utf-8'))
        self.hash = hashFunction.hexdigest()


    def addElementsFromDirectory(self, directory, ignorePatterns):

        for root, dirs, files in os.walk(directory):
            for file in files:
                completePath = os.path.join(root,file)
                relPath = os.path.relpath(completePath, directory)
                # Gestion de IGNORE_FILE
                if not any((relPath.endswith(pattern) or (pattern.endswith('/') and pattern in relPath)) for pattern in ignorePatterns):
                    element = Element(relPath, self.project.hashAlgorithm)
                    element.generateHash()
                    self.elements.append(element)

    def addElementsFromVersionFile(self, versionFile):
        with open (versionFile,'r',newline='') as file:
            reader = csv.reader(file)
            for line in reader:
                element = Element(line[1], self.project.hashAlgorithm)
                element.setHash(line[0])
                self.elements.append(element)
            
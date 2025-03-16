import os
import hashlib
import time
import csv

from Project import Project
from Element import Element

class Version:
    def __init__(self, ancestors, comment, project):
        self.ancestors = ancestors
        self.comment = comment
        self.project = project
        self.elements = []
        self.hash = ''
        self.timestamp = time.time()

    def generateHash(self):
        hashFunction = hashlib.new(self.project.hashAlgorithm)
        for element in self.elements:
            hashFunction.update(element.path.encode('utf-8'))
            hashFunction.update(element.hash.encode('utf-8'))
            # hashFunction.update(str(time.time()).encode('utf-8'))
        self.hash = hashFunction.hexdigest()


    def create(self, directory):
        self.objects = []
        ignorePatterns = self.project.getIgnorePatterns()

        for root, dirs, files in os.walk(directory):
            for file in files:
                completePath = os.path.join(root,file)
                relPath = os.path.relpath(completePath, directory)
                # Gestion de IGNORE_FILE
                if not any((relPath.endswith(pattern) or (pattern.endswith('/') and pattern in relPath)) for pattern in ignorePatterns):
                    element = Element(relPath, self.project.hashAlgorithm)
                    self.elements.append(element)
            
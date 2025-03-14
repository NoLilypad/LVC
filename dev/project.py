import os

class Project:
    def __init__(self, workingDirectory):
        self.directory = workingDirectory
    
    def __str__(self):
        return self.directory
    
    def build(self):
        pass
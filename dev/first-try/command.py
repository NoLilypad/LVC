import os
from history import History

class Command:
    def __init__(self, CONFIG):
        self.HASH_ALGO = CONFIG['HASH_ALGO']
        self.version = CONFIG['VERSION']    
        self.workingDirectory = os.getcwd()


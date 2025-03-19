import hashlib

class Element:
    def __init__(self, path, hashAlgorithm='sha256'):
        self.path = path
        self.hashAlgorithm = hashAlgorithm
        self.hash = ''

    # Redefined eq to compare Elements based on their attributes and not their reference
    def __eq__(self, other):
        if isinstance(other, Element):
            return self.hash == other.hash and self.path == other.path
        return False

    def generateHash(self):
        hashFunction = hashlib.new(self.hashAlgorithm)
        with open(self.path,'rb') as file:
            # Read the file in chunks of 8192 bytes
            while chunk := file.read(8192):
                hashFunction.update(chunk)
        self.hash = hashFunction.hexdigest()

    def setHash(self, hash):
        self.hash = hash

import hashlib

class Element:
    def __init__(self, path, hashAlgorithm):
        self.path = path
        self.hashAlgorithm = hashAlgorithm
        self.hash = self.getHash()

    def getHash(self):
        hashFunction = hashlib.new(self.hashAlgorithm)
        with open(self.path,'rb') as file:
            # Read the file in chunks of 8192 bytes
            while chunk := file.read(8192):
                hashFunction.update(chunk)
        return(hashFunction.hexdigest())

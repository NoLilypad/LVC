import hashlib

class Element:
    def __init__(self, path, hash):
        self.path = path
        self.hash = hash

    # Redefined eq to compare Elements based on their attributes and not their reference
    def __eq__(self, other):
        if isinstance(other, Element):
            return self.hash == other.hash and self.path == other.path
        return False

    # For creating an Element with its path and generating its hash
    @classmethod
    def fromDirectory(cls, path, hashAlgorithm='sha256'):
        hashFunction = hashlib.new(hashAlgorithm)
        with open(path,'rb') as file:
            # Read the file in chunks of 8192 bytes
            while chunk := file.read(8192):
                hashFunction.update(chunk)
        hash = hashFunction.hexdigest()
        return cls(path, hash)

    # For creating an Element when knowing its path and hash
    @classmethod
    def fromHash(cls, path, hash):
        return cls(path, hash)

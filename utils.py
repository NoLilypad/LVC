import os
import shutil
import fnmatch
import re
import hashlib 
import time

'''def readIgnore(workingDirectory, CONFIG):
    ignoreFile = CONFIG['IGNOREFILE']
    with open(os.path.join(workingDirectory, ignoreFile), 'r') as ignore_file:
        ignorePatterns = [line.strip() for line in ignore_file if line.strip()]
    
    for pattern in ignorePatterns:
        try:
            pass
        except re.error:
            continue


    return ignorePatterns'''



def getElements(directory):
    # Collecte des éléments (fichiers et dosiers vides)
    elements = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            completePath = os.path.join(root,file)
            relPath = os.path.relpath(completePath, directory)
            elements.append(relPath)
    return sorted(elements)

def getFileHash(directory, filePath, algorithm='sha256'):
    hashFunction = hashlib.new(algorithm)
    with open(os.path.join(directory,filePath),'rb') as file:
        # Read the file in chunks of 8192 bytes
        while chunk := file.read(8192):
            hashFunction.update(chunk)
    return(hashFunction.hexdigest())

def getVersionHash(elementsInfo):
    sha256 = hashlib.sha256()
    for element in elementsInfo:
        sha256.update(element[0].encode('utf-8'))
        sha256.update(element[1].encode('utf-8'))
    sha256.update(str(time.time()).encode('utf-8'))
    return(sha256.hexdigest())

def copyAndRename(src, dst, newName):
    shutil.copy2(src, dst)
    







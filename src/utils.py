import os
import shutil
import fnmatch
import re
import hashlib 
import time

def readIgnore(ignoreFilePath):
    with open(ignoreFilePath, 'r') as ignore_file:
        ignorePatterns = [line.strip() for line in ignore_file if line.strip()]
    
    for pattern in ignorePatterns:
        try:
            pass
        except re.error:
            continue
    return ignorePatterns



def getElements(directory, ignorePatterns):
    elements = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            completePath = os.path.join(root,file)
            relPath = os.path.relpath(completePath, directory)
            # Gestion de IGNORE_FILE
            if not any((relPath.endswith(pattern) or (pattern.endswith('/') and pattern in relPath)) for pattern in ignorePatterns):
                elements.append(relPath)
    return sorted(elements)

def getFileHash(directory, filePath, algorithm='sha256'):
    hashFunction = hashlib.new(algorithm)
    with open(os.path.join(directory,filePath),'rb') as file:
        # Read the file in chunks of 8192 bytes
        while chunk := file.read(8192):
            hashFunction.update(chunk)
    return(hashFunction.hexdigest())

def getVersionHash(elementsInfo, algorithm='sha256'):
    hashFunction = hashlib.new(algorithm)
    for element in elementsInfo:
        hashFunction.update(element[0].encode('utf-8'))
        hashFunction.update(element[1].encode('utf-8'))
    hashFunction.update(str(time.time()).encode('utf-8'))
    return(hashFunction.hexdigest())

def createObject(elementPath, elementHash, objectsDirectory):
    with open(elementPath, 'rb') as file:
                data = file.readlines()
    with open(os.path.join(objectsDirectory, elementHash), 'wb') as file:
        file.writelines(data)

def createObjects(workingDirectory, LVC_DIR, OBJECTS_DIR, elementsInfo):
    for element in elementsInfo:
        elementPath, elementHash = element
        elementObjectPath = os.path.join(workingDirectory, LVC_DIR, OBJECTS_DIR, elementHash)
        if not os.path.isfile(elementObjectPath):
            createObject(elementPath, elementHash, os.path.join(workingDirectory, LVC_DIR, OBJECTS_DIR))

def createVersionFile(workingDirectory, LVC_DIR, VERSIONS_DIR, versionHash, elementsInfo):
    with open(os.path.join(workingDirectory, LVC_DIR, VERSIONS_DIR, versionHash), 'w') as file:
        for element in elementsInfo:
            elementPath, elementHash = element
            file.writelines(f'{elementHash}|{elementPath}\n') 

def writeVersion(directory, LVC_DIR, DATA_FILE, versionHash, comment):
        with open(os.path.join(directory, LVC_DIR, DATA_FILE), 'a') as file:
            timestamp = int(time.time())
            file.writelines(f'{versionHash}|{timestamp}|{comment}\n')










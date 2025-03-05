import os
import shutil

def destroy(CONFIG, arguments):
    LVC_DIR = CONFIG['LVC_DIR']
    workingDirectory = os.getcwd()
    # Checks if versionner directory exists
    isInit = os.path.isdir(os.path.join(workingDirectory, LVC_DIR))
    if isInit:
        shutil.rmtree(os.path.join(workingDirectory, LVC_DIR))
        print('Repo erased')
        return
    else:
        print('No repo in current directory')
        return
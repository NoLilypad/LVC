import os
import shutil

def destroy(CONFIG, arguments):
    workingDirectory = os.getcwd()
    lvcDirectory = os.path.join(workingDirectory, CONFIG['LVC_DIR'])
    isInit = os.path.isdir(lvcDirectory)
    if isInit:
        shutil.rmtree(lvcDirectory)
        print('Repo erased')
        return
    else:
        print('No repo in current directory')
        return
    

    

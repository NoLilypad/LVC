import os
import shutil

VERDIR = 'ver'

def init():
    # Get working directory
    workingDirectory = os.getcwd()
    # Checks if versionner directory exists
    isInit = os.path.isdir(f'{workingDirectory}/{VERDIR}')
    if isInit:
        print('Repo already created in current folder')
    else:
        os.mkdir(f'{workingDirectory}/{VERDIR}')
        with open('./ver/hello','w') as file:
            file.writelines('')
        print('Repo created in current directory')



init()
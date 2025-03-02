import os
import shutil
import sys

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


def main():
    # Get first arg
    arg = sys.argv[1]
    print("Argument passé",arg)
    if arg == 'init':
        init()


if __name__ == "__main__":
    main()
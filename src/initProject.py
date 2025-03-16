import os 

from Project import Project


def initProject(CONFIG, arguments):    
    workingDirectory = os.getcwd()
    hashAlgorithm = CONFIG['HASH_ALGO'] 

    project = Project(workingDirectory, hashAlgorithm)

    if project:
        print('LVC project already setup in current directory')
        return

    project.write()

    createIgnore =  not (len(arguments) >= 1 and arguments[0] == '-n')  
    if createIgnore:    
        with open(project.ignoreFile,'w') as file:
            file.writelines('.lvc/ \n')
        print('LVC project builded in current directory with .lvcignore')
    else:
        print('LVC project builded in current directory without .lvcignore')
        
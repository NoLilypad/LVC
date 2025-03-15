import os 

from Project import Project


def init(CONFIG):    
    workingDirectory = os.getcwd()

    project = Project(workingDirectory)
    
    if project:
        print('LVC project already setup in current directory')
        return
    
    project.build()

    print('LVC project builded in current directory')
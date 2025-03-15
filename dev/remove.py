import os 

from Project import Project


def remove(CONFIG):    
    workingDirectory = os.getcwd()

    project = Project(workingDirectory)
    
    if not project:
        print('No LVC project in current directory')
        return
    
    project.erase()

    print('LVC project removed')
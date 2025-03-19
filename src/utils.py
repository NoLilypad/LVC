import os

from Project import Project
from Version import Version


def isCurrentDirectoryVersioned(project: Project):
    head = project.getHead()
    projectDirectory = project.projectDirectory
    ignorePatterns = project.getIgnorePatterns()

    localVersion = Version(['Placeholder'],'placeholder', project)
    localVersion.addElementsFromDirectory(projectDirectory, ignorePatterns)

    headVersion = Version(['Placeholder'],'placeholder', project)
    headVersionFile = os.path.join(project.versionsDirectory, head)
    headVersion.addElementsFromVersionFile(headVersionFile)

    return localVersion.elements == headVersion.elements

    
    
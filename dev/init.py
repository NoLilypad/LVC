from command import Command
from history import History

class Init(Command):

    def command(self, arguments):
        # Get no ignore flag
        if len(arguments) >= 1 and arguments[0] == '-n':    
            noIgnore = True
        else:
            noIgnore = False

        # Checks if history is init in working directory
        if self.isInit():
            print('Repo already created in current directory')
            return

        # Creates history using working directory
        history = History(self.workingDirectory)



        print(history)
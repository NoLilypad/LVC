from command import Command
from history import History

class Init(Command):

    def command(self, arguments):
        # Get no ignore flag
        if len(arguments) >= 1 and arguments[0] == '-n':    
            noIgnore = True
        else:
            noIgnore = False

        

        # Creates history using working directory
        history = History(self.workingDirectory)

        history.initDump()

        print(history)
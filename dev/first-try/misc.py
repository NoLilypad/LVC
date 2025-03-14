import os

from command import Command
from history import History

class Misc(Command):

    def home(self):
        # Checks if versionner directory exists
        if History.isInit(self.workingDirectory):
            message = 'Activé dans le dossier courant'
        else:
            message = "Pas activé dans le dossier courant"

        print(f'{message} \nLVC version {self.version}')
        print("Type 'lvc help' or 'lvc h' for help ")

    def unkownCommand(self, arguments):
        print('Unknown command')


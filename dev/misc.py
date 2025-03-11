import os

from command import Command

class misc(Command):

    def home(self):
        # Checks if versionner directory exists
        isInit = os.path.isdir(self.lvcDirectory)
        if isInit:
            message = 'Activé dans le dossier courant'
        else:
            message = "Pas activé dans le dossier courant"

        print(f'[LVC version {self.version}] {message}')
        print("Type 'lvc help' or 'lvc h' for help ")

    def unkownCommand(self, arguments):
        print('Unknown command')


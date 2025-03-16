def home(CONFIG):
    # Checks if versionner directory exists
    # if History.isInit(self.workingDirectory):
    #     message = 'Activé dans le dossier courant'
    # else:
    #     message = "Pas activé dans le dossier courant"

    print(f'\nLVC version {CONFIG["VERSION"]}')
    print("Type 'lvc help' or 'lvc h' for help ")


def unknownCommand(CONFIG):
    print('Unknown command')

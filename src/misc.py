import os

def home(CONFIG):
    version = CONFIG['VERSION']
    workingDirectory = os.getcwd()
    lvcDirectory = os.path.join(workingDirectory, CONFIG['LVC_DIR'])

    # Checks if versionner directory exists
    isInit = os.path.isdir(lvcDirectory)
    if isInit:
        message = 'Activé dans le dossier courant'
    else:
        message = "Pas activé dans le dossier courant"

    print(f'[LVC version {version}] {message}')
    print("Type 'lvc help' or 'lvc h' for help ")

def unknownCommand():
    print('Unknown command')

def help(CONFIG, arguments):
    version = CONFIG['VERSION']
    print(f'[LVC version {version}] ')
    print("""
          lvc    [init|version <comment>|list|switch <ID>|destroy|help]
          
        * init              : initialize lvc in the current directory. Add -n to avoid adding a .lvcignore file
        * version <comment> : creates a new snapshot of the working directory, with a optional comment
        * list              : lists all versions in working directory
        * switch  <ID>      : switches to version with version ID given with list
        * destroy           : deactivates lvc in current directory
        * help              : displays this help   """)




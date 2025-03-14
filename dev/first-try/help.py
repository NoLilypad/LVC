from command import Command

class Help(Command):

    def command(self, arguments):
        print(f'[LVC version {self.version}] ')
        print("""
            lvc    [init|version <comment>|list|switch <ID>|destroy|help]
            
            * init              : initialize lvc in the current directory. Add -n to avoid adding a .lvcignore file
            * version <comment> : creates a new snapshot of the working directory, with a optional comment
            * list              : lists all versions in working directory
            * switch  <ID>      : switches to version with version ID given with list
            * destroy           : deactivates lvc in current directory
            * help              : displays this help   """)




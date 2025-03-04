import os
import shutil
import time
import uuid

def home(CONFIG):
    version = CONFIG['VERSION']
    print(f'Versionner {version}')

def unknownCommand():
    print('Unknown command')


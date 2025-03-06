import os

# Get the current working directory
current_directory = os.getcwd()

# List all files and directories in the current directory
files_and_directories = os.listdir(current_directory)


# Filter out only the files
files = [f for f in files_and_directories if os.path.isfile(os.path.join(current_directory, f))]

# Filter .py files
python_files = [f for f in files if f.endswith('.py')]
python_files.remove('merger.py')

# Creates merged file
with open(os.path.join(current_directory, 'merged.py'), 'w') as file:
    file.writelines('')

# Appends file lines to merged file
for file in python_files:
    pass



# LVC : a Lightweight Version Control

A simple local code version control manager made with Python that can be run as such or easily built into an executable.

## Installation

Clone the repo

```sh
git clone git@github.com:NoLilypad/LVC.git
cd LVC
```

## Building

### Install Python requirements


You may need to use a virtual environment
```sh
pip install -r requirements.txt
```

LVC is fully written in Python, but offers two solutions to compile it using the `tools/makefile`. 


### 1. Build the file [through C](https://cython.org/) :

You might have to install Python dev
```sh
sudo apt update
sudo apt install python3-dev
```
Then build the file

```sh
cd tools
make cython_build 
```
The executable will then be in `build/cython`


### 2. Build the file with [pyinstaller](https://pyinstaller.org/en/stable/)
```sh
cd tools
make pyinstaller_build 
```

The executable will then be in `build/pyinstaller`


## Run

You can either run LVC as a Python script, or use the executable built above.

### 1. Using Python
```sh
python src/lvc.py
```

### 2. Using the executable
```sh
build/cython/lvc        # or
build/pyinstaller/lvc
```
Place the built executable in `/usr/local/bin` to easily call it in any directory

## Usage 

LVC works similarly to git. LVC's *versions* are the equivalent to gits commits, and are a snapshot of a directory's content.


For now, there are no merge functionality. 


## Commands

| Command           | Alias    | Use                                        | arguments|
| :---------------- | :------: | :----                                      | :---:|
| `init`       |   `i`    | initialize version manager in directory    | (optionnal) -n to avoid .lvcignore automatic creation
| `version`         |   `v`    | create a new version                       | comment of version
| `list`            |  `l`     | lists versions                             | -
| `switch`          |  `s`     | switches to specifi version                | version ID
| `destroy`         | `d`      | deletes the config of local version manager|- 
| `help`            | `h`      | print help                                 | -

## Releases

- **v3.0** : Object oriented conception
- **v2.1** : Better build functionality
- **v2.0** : Added caching feature
- **v1.0** : No caching, plain 


## .lvc structure 

```bash
workingDirectory/  
├── .lvc/  
│   ├── project   
│   ├── versions/    
│   │   ├── versionHash1  
│   │   ├── versionHash2  
│   │   └── versionHash3  
│   └── objects/  
│       ├── objectHash1  
│       └── objectHash2  
├── SomeFileToTrack  
└── SomeFolder/  
    └── AnotherFile  
```


Made with [https://www.text-tree-generator.com/](https://www.text-tree-generator.com/)

## Comments

- Building through C results to much lighter executable, but require a few more steps than using pyinstaller
- For now, there are no link between versions, meaning no merge or branch functionality

Performance difference between Pyinstaller and Cython builds using [hyperfine](https://github.com/sharkdp/hyperfine) : 

[Benchmark result](misc/benchmark.png)


## Known issues

- Does not preserve file permissions

## TODO

### Priority

- [X] Modifiy version to store directly hashID
- [X] Fix ancestors storage
- [ ] Write pseudocode for merge and see if it can directly include finding ancestors recursively
- [X] Add caching
- [X] Add linking between versions
- [X] Add ignore method


### Misc

- [X] Refactorise read/write functions of utils
- [ ] Rewrite ignore patterns management in utils.getElements
- [X] Automate C compilation

### Long-term
- [ ] Add branch system
- [ ] Add remote access
- [ ] Add merging functionality
- [ ] Add autocompletion 




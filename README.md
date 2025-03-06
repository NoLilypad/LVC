# LVC : a Lightweight Version Control

A simple local code version control manager made with Python that can be run as such or easily built into an executable.

## Installation

Clone the repo

```sh
git clone git@github.com:NoLilypad/LVC.git
cd LVC
```

## Building

LVC is fully written in Python, but offers two solutions to compile it.


### 1. Build the file with [pyinstaller](https://pyinstaller.org/en/stable/)
```sh
cd src/
pyinstaller --onefile --name=lvc lvc.py
```

### 2. Build the file [through C](https://cython.org/) using the automated compiler script :

More details in comments

```sh
cd src/
./compiler
```

## Run

You can either run LVC as a Python script, or use the executable us built above.

### 1. Using Python
```sh
python src/lvc.py
```

### 2. Using the executable
```sh
src/lvc
```
Place the built executable in `/usr/local/bin` to easily call it in any directory

## Usage 

LVC works similarly to git. LVC's *versions* are the equivalent to gits commits, and are a snapshot of a directory's content.


For now, there are no merge functionality. 


## Commands

| Command           | Alias    | Use | arguments|
| :---------------- | :------: | :---- | :---:|
| `init     `       |   `i`    | initialize version manager un directory | (optionnal) -n to avoid .lvcignore automatic creation
| `version`         |   `v`    | create a new version | comment of version
| `list`            |  `l`     | lists versions | -
| `switch`          |  `s`     | switches to specifi version | version ID
| `destroy`         | `d`      | deletes the config of local version manager|- 
| `help`         | `h`      | print help| -



## Comments

- Building through C results to much lighter executable, but require a few more steps than using pyinstaller
- For now, there are no link between versions, meaning no merge or branch functionality


## Releases

- **v2.0** : Added caching feature
- **v1.0** : No caching


## Structure 

```bash
workingDirectory/  
├── .lvc/  
│   ├── data   
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

## TODO

### Priority

- [X] Add caching
- [ ] Add linking between versions
- [X] Add ignore method

### Misc

- [ ] Refactorise read/write functions of utils
- [ ] Rewrite ignore patterns management in utils.getElements
- [X] Automated C compilation

### Long-term
- [ ] Add remote access
- [ ] Add merging functionality
- [ ] Add autocompletion 




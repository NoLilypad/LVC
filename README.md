# LVC : a Lightweight Version Control

A simple local code version control manager made with Python. 

## Installation


Clone the repository 

```sh
git clone git@github.com:NoLilypad/LVC.git
cd versionner
```

You can then either : 
- Execute LVC using python : 
```sh
python /the/path/to/versionner/lvc.py your_command
```

- Build the file with [pyinstaller](https://pyinstaller.org/en/stable/), then making it a command by placing it in /usr/local/bin for example
```sh
pyinstaller --onefile --name=lvc lvc.py
sudo cp dist/ver /usr/local/bin
```

## Commands

| Command           | Alias    | Use | arguments|
| :---------------- | :------: | :---- | :---|
| `init     `       |   `i`    | initialize version manager un directory | -
| `version`         |   `v`    | create a new version | comment of version
| `list`            |  `l`     | lists versions | -
| `switch`          |  `s`     | switches to specifi version | version ID
| `destroy`         | `d`      | deletes the config of local version manager| - 


## Comments

Currently (1.0) no caching, no branches, no merging, no remote access or .ignore file.


## Releases

- **v1.0** : No caching
- **v2.0** : Added caching feature


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

- [ ] Add caching
- [ ] Add linking between versions
- [X] Add ignore method

### Misc

- [ ] Refactorise read/write functions of utils
- [ ] Rewrite ignore patterns management in utils.getElements

### Long-term
- [ ] Add remote access
- [ ] Add merging functionality
- [ ] Add autocompletion 




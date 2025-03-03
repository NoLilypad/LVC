# Versionner

A simple local version manager

## Installation


Clone the repository 

```sh
git clone git@github.com:NoLilypad/versionner.git
cd versionner
```

You can then either : 
- Execute the versionner using python : 
```sh
python /the/path/to/versionner/versionner.py you_command
```

- Build the file with [pyinstaller](https://pyinstaller.org/en/stable/), then making it a command by placing it in /usr/bin for example
```sh
pyinstaller --onefile --name=ver versionner.py
sudo cp dist/ver /usr/bin
```

## Commands

| Command           | Alias    | Use | arguments|
| :---------------- | :------: | :---- | :---|
| `init     `       |   `i`    | initialize version manager un directory | -
| `version`         |   `v`    | create a new version | comment of version
| `list`            |  `l`     | lists versions | -
| `switch`          |  `s`     | switches to specifi version | version ID
| `destroy`         | `d`      | deletes the config of local version manager| - 





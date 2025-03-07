#!/bin/bash


# Clean builds
make clean c

# Cython build
make cython_build

# Pyinstaller build
make pyinstaller_build

# Checks if hyperfine is installed before executing it
if which hyperfine >/dev/null 2>&1; then
    hyperfine '../build/cython/lvc i; ../build/cython/lvc v; ../build/cython/lvc d' '../build/pyinstaller/lvc i; ../build/pyinstaller/lvc v; ../build/pyinstaller/lvc d'
else
    echo "Hyperfine not installed"
fi




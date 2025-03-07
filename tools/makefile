PYTHON = python3
BUILD_DIR = ../build

all: cython_build

cython_build:
	mkdir -p $(BUILD_DIR)
	$(PYTHON) merger.py ../src/ lvc.py
	$(PYTHON) -m cython --embed -o $(BUILD_DIR)/lvc.c $(BUILD_DIR)/lvc.py
	gcc -I$(shell $(PYTHON) -c "import sysconfig; print(sysconfig.get_path('include'))") -o $(BUILD_DIR)/lvc $(BUILD_DIR)/lvc.c -lpython3.12
pyinstaller_build:
	mkdir -p $(BUILD_DIR)
	$(PYTHON) -m pyinstaller --onefile --name=$(BUILD_DIR)/lvc ../src/lvc.py

clean:
	rm -rf $(BUILD_DIR)

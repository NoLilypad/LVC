PYTHON = python3
BUILD_DIR = ../build

all: cython_build

cython_build:
	mkdir -p $(BUILD_DIR)
	mkdir -p $(BUILD_DIR)/cython
	$(PYTHON) merger.py ../src/ $(BUILD_DIR)/cython/lvc.py
	$(PYTHON) -m cython --embed -o $(BUILD_DIR)/cython/lvc.c $(BUILD_DIR)/cython/lvc.py
	gcc -I$(shell $(PYTHON) -c "import sysconfig; print(sysconfig.get_path('include'))") -o $(BUILD_DIR)/cython/lvc $(BUILD_DIR)/cython/lvc.c -lpython3.12

pyinstaller_build:
	mkdir -p $(BUILD_DIR)
	pyinstaller --distpath $(BUILD_DIR)/pyinstaller --workpath $(BUILD_DIR)/pyinstaller/build --specpath $(BUILD_DIR) --onefile --name=$(BUILD_DIR)/lvc ../src/lvc.py

clean:
	rm -rf $(BUILD_DIR)

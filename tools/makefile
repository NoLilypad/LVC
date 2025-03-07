all:
	python merger.py ../src/ lvc.py
	cython --embed -o ../build/lvc.c ../build/lvc.py
	gcc -I/usr/include/python3.12 -o ../build/lvc ../build/lvc.c -lpython3.12

clean:
	rm -f ../build/lvc.c ../build/lvc.py ../build/lvc

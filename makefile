.PHONY: build install_dependencies install_dev_dependencies clean

build:
	pyinstaller --onefile tmx2map/tmx2map.py

install_dependencies:
	pip install -r requirements.txt

install_dev_dependencies:
	pip install -r dev-requirements.txt

clean:
	rm -rf ./dist
	rm -rf ./build
	rm *.spec
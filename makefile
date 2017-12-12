.PHONY: build install_dependencies install_dev_dependencies package clean

platform = linux
binary_file := tmx2map

ifeq ($(OS),Windows_NT)
    detected_OS := Windows
else
    detected_OS := $(shell uname -s)
endif

ifeq ($(detected_OS),Windows)
	platform := win32
	binary_file := tmx2map.exe
endif
ifeq ($(detected_OS),Darwin)  # Mac OS X
	platform := macos
endif

build:
	pyinstaller --onefile tmx2map/tmx2map.py

install_dependencies:
	pip install -r requirements.txt

install_dev_dependencies:
	pip install -r dev-requirements.txt

package: build
	$(eval version := $(shell ./dist/$(binary_file) -v | grep -o '[0-9]\+.[0-9]\+.[0-9]\+'))
	$(eval zip_file := tmx2map-$(version)-$(platform).zip)
	zip -r $(zip_file) ./examples
	mv $(zip_file) ./dist && cd ./dist && zip $(zip_file) $(binary_file) && mv $(zip_file) ..

clean:
	rm -rf ./dist
	rm -rf ./build
	rm *.spec
	rm *.zip
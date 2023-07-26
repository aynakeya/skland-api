
build: clean
	python3 -m build

install: build
	pip3 install dist/skland_api-*.whl

clean:
	rm -rf build dist
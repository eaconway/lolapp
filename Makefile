.PHONY: compile
compile:
	pip-compile

.PHONY: install
install:
	pip3 install -r requirements.txt

.PHONY: setup
setup: compile install

.PHONY: run
run:
	python3 server.py

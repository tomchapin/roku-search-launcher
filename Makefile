.PHONY: all
default: init install;

ensure-config:
	@cp -n .config.example.yaml .config.yaml || true

init:
	@$(MAKE) ensure-config
	pyenv virtualenv 3.5.3 roku-search-launcher-3.5.3 || true

install:
	pip install -r requirements.txt

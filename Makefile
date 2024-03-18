
mkdocs.yml: template.yml $(shell find ./docs -name 'mkdocs.yml')
	python make.py

build: mkdocs.yml
	mkdocs build

serve: mkdocs.yml
	mkdocs serve

MSG = "update docs"

commit:
	mkdocs build
	git add .
	git commit -am "$(MSG)"
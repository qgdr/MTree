BOOKS = $(shell ls */book.toml | sed 's/\/book.toml//')
build:
	@for book in $(BOOKS); do \
		echo "Building $$book"; \
		mdbook build $$book; \
	done

watch:
	@for book in $(BOOKS); do \
		echo "watching $$book"; \
		mdbook watch $$book; \
	done
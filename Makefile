all:
	@echo "There is no default make target"

clean:
	find . \( -name '*.pyc' -o -name '*~' \) -print0 | xargs -r -0 rm
	find . -name '__pycache__' -type d -print0 | xargs -r -0 rm -r
	find . -name '.pytest_cache' -type d -print0 | xargs -r -0 rm -r
	find . -name '.ruff_cache' -type d -print0 | xargs -r -0 rm -r

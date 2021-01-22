install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

activate:
	source $(poetry env info --path)/bin/activate

lint:
	poetry run flake8 brain_games

.PHONY: install lint build publish
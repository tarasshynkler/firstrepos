DEFAULT_GOAL := all

all: install test run deploy

install:
	@echo "Installing pipenv and dependencies."
	# Ваш код тут
	@pip install pipenv
	@pipenv --python 3.7
	#@pipenv shell
	@pipenv install requests
	@pipenv install ntplib
	@pipenv install pytest

test:
	@echo "Start tests."
	@pipenv run pytest tests.py | tee resultsM.txt

run:
	@echo "Run Python app."
	# Ваш код тут
	@pipenv run python app.py | tee -a resultsM.txt
	@pipenv --rm
deploy:
	@echo "Adding and Committing results.txt to git."
	# Ваш код тут
	@git add resultsM.txt
	@git commit -m "Автоматичний пуш файлу"
	@git push origin master
env:
-include .env

run: env
ifeq ($(APP_ENV), development)
	docker-compose up db-espresso-dev api-dev
else
	docker-compose up db-espresso api
endif

install: env
	docker-compose run api-dev pip install -r requirements.txt -t lib

greet: env
	docker-compose run api-dev espresso hello

clean: env
	sudo rm -rf lib
	sudo rm -rf app/core/databases/mysql-data
	docker rmi --force espresso_api-dev
	docker container prune --force --filter "label=project=espresso"

lint:
	pylint app/*

pydocstyle:
	pydocstyle app/

isort:
	isort app/

black:
	black --line-length 110 --target-version py37
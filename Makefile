env:
-include .env

run: env
ifeq ($(APP_ENV), development)
	docker-compose up espresso-db api-dev
else
	docker-compose up database api
endif

install: env
	docker-compose run api-dev pip install -r requirements.txt -t lib

clean: env
	sudo rm -rf lib
	sudo rm -rf app/core/databases/mysql-data
	docker rmi --force espresso_api-dev
	docker container prune --force --filter "label=project=espresso"
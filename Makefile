env:
-include .env

run: env
ifeq ($(APP_ENV), development)
	docker-compose up database-dev espresso-dev
else
	docker-compose up database espresso
endif
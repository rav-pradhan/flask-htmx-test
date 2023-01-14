debug: seed-db
	docker-compose up

test:
	docker-compose run flask-htmx-prototype poetry run pytest

down:
	docker-compose down --remove-orphans

build:
	docker-compose build

seed-db:
	docker-compose run flask-htmx-prototype poetry run python init_db.py
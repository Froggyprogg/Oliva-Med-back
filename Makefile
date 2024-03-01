PHONY: run
run:
	python manage.py runserver

PHONY: makem
makem:
	python manage.py makemigrations

PHONY: migrate
migrate:
	python manage.py migrate
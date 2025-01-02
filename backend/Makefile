# Makefile for Django project

# Параметры
PYTHON=python
DJANGO_MANAGE=python manage.py

# Общие задачи
install:
    pip install -r requirements.txt

migrate:
    $(DJANGO_MANAGE) migrate

makemigrations:
    $(DJANGO_MANAGE) makemigrations

runserver:
    $(DJANGO_MANAGE) runserver

test:
    $(DJANGO_MANAGE) test

create_superuser:
    $(DJANGO_MANAGE) createsuperuser

clean:
    find . -name '*.pyc' -exec rm -f {} \;

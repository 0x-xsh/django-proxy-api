#!/bin/sh


# run migrations

python manage.py makemigrations


python manage.py migrate --fake 


python manage.py migrate --run-syncdb





export DJANGO_SETTINGS_MODULE=assessement.settings




# start your web application
exec "$@"

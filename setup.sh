# /bin/bash

python manage.py mikemigrations
python manage.py migrate
python manage.py migrate django_celery_results

python manage.py loaddata people
python manage.py loaddata artifacts
python manage.py loaddata books
python manage.py loaddata vehicles






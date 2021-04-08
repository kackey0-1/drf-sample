# drf-sample
[PyLinter Setting](https://qiita.com/navitime_tech/items/0a431a2d74c156d0bda2)

# Setup 
```bash
# Make Migration files
python manage.py migrate

# Migration
python manage.py migrate

# Run Server
python manage.py runserver

# Test that the Celery worker is ready to receive tasks
celery -A app worker --beat -l info

# Test that the Celery task scheduler is ready for action
celery -A app beat -l info

# Execute celery worker & beat
celery -A app worker --beat --loglevel=info
```

## Dockerization
```bash
# docker build
docker build -t drf-sample .

# docker run only first time
docker run -it -p 8000:8000 \
     -e DJANGO_SUPERUSER_USERNAME=admin \
     -e DJANGO_SUPERUSER_PASSWORD=sekret1 \
     -e DJANGO_SUPERUSER_EMAIL=admin@example.com \
     drf-sample
# docker run after first run
docker run -it -p 8000:8000 drf-sample
```

# Docs
- app: settings files
- api: api endpoints
- artifacts: artifacts module
- books: books module
- people: people module


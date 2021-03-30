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

# Test that the Celery worker is ready to receive tasks:
celery -A app worker -l info

# Test that the Celery task scheduler is ready for action:
celery -A app beat -l info
```
# Docs
- app: settings files
- api: api endpoints
- artifacts: artifacts module
- books: books module
- people: people module


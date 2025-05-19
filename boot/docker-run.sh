#!/bin/bash

# Activate virtualenv
source /opt/venv/bin/activate
cd /app

# Apply database migrations
python manage.py migrate --noinput

if [ "$DJANGO_ENV" = "development" ]; then
    python manage.py runserver 0.0.0.0:8000
else
    # Run Gunicorn
    RUNTIME_PORT=${PORT:-8000}
    RUNTIME_HOST=${HOST:-0.0.0.0}
    exec gunicorn my_project.wsgi:application --bind $RUNTIME_HOST:$RUNTIME_PORT
fi
#!/bin/bash

# Activate virtualenv
source /opt/venv/bin/activate
cd /app

# Apply database migrations
python manage.py migrate --noinput

if [ "$DJANGO_ENV" = "development" ]; then
    python manage.py runserver 0.0.0.0:8000
else
    # Create Django superuser
    if [ "$DJANGO_SUPERUSER_EMAIL" ] && [ "$DJANGO_SUPERUSER_PASSWORD" ]; then
        python manage.py shell -c "
from django.contrib.auth import get_user_model;
User = get_user_model();
email = '$DJANGO_SUPERUSER_EMAIL';
if not User.objects.filter(email=email).exists():
    User.objects.create_superuser(email, '$DJANGO_SUPERUSER_PASSWORD')"
    fi
    # Run Gunicorn
    RUNTIME_PORT=${PORT:-8000}
    RUNTIME_HOST=${HOST:-0.0.0.0}
    exec gunicorn my_project.wsgi:application --bind $RUNTIME_HOST:$RUNTIME_PORT
fi
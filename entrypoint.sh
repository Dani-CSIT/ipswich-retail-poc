#!/usr/bin/env bash
set -e

# safety defaults
export PYTHONUNBUFFERED=1

echo "Applying migrations…"
python manage.py migrate --noinput

echo "Collecting static…"
python manage.py collectstatic --noinput

python manage.py seed_demo 

echo "Starting Gunicorn…"
exec gunicorn core.wsgi:application --bind 0.0.0.0:${PORT:-8000}
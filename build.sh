#!/usr/bin/env bash
# build.sh

# Install dependencies
pip install -r requirements.txt

# Collect static files for production
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate

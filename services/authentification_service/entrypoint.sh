#!/bin/sh
set -eu
/venv/bin/python /app/wait_db.py
/venv/bin/python /app/manage.py migrate --noinput
/venv/bin/python /app/manage.py runserver 0.0.0.0:8000

#!/bin/sh
set -eu
echo "TEST BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"
ls -la ..

#/venv/bin/python /app/manage.py migrate --noinput
/venv/bin/python /app/manage.py runserver 0.0.0.0:8000

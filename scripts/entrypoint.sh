#!/bin/sh
APP_PORT=${PORT:-8000}
cd /app/
/env/bin/gunicorn --worker-tmp-dir dev/shm app.wsgi:application --bind "0.0.0.0:${APP_PORT}"
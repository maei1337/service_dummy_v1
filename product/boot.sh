#!/bin/sh -e

current_time=$(date "+%Y.%m.%d-%H.%M.%S")
FLASK_APP=api.py
flask db migrate -m $current_time
flask db upgrade
exec gunicorn --log-level info --log-file=/gunicorn.log --workers 4 --name app -b 0.0.0.0:8001 --reload api:app

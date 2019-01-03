#!/bin/sh -e

current_time=$(date "+%Y.%m.%d-%H.%M.%S")
FLASK_APP=api.py
flask db migrate -m $current_time
flask db upgrade
python api.py

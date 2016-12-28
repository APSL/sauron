#!/bin/bash
set -e
if [ "$1" = 'uwsgi' ]; then
  exec uwsgi --ini=/uwsgi.ini
elif [ "$1" = 'daphne' ]; then
  exec daphne -b 0.0.0.0 -p 8000 --root-path /app main.asgi:channel_layer
# elif [ "$1" = 'cron' ]; then
#   getcrons.py crons.yml > crontab
#   exec go-cron -file="crontab"
fi
exec "$@"
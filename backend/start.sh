#!/usr/bin/env bash
# start-server.sh
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (python manage.py createsuperuser --no-input)
fi
python manage.py migrate
(uwsgi --socket :8010 -b 32768 --wsgi-file backend/wsgi.py) &
nginx -g "daemon off;"
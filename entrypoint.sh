#!/bin/sh
set -e

for i in $(seq 1 10); do
    flask db upgrade && break
    echo "wait bd... $i"
    sleep 3
done

echo "start gunicorn..."
exec gunicorn -w 4 -b 0.0.0.0:4000 'app:create_app()'
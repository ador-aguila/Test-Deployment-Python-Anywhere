#!/bin/sh

until python -c "import psycopg2; psycopg2.connect(host='db', dbname='mydb', user='postgres', password='password')" >/dev/null 2>&1
do
    echo "Waiting for PostgreSQL..."
    sleep 2
done

python manage.py migrate
python manage.py runserver 0.0.0.0:8000
#!/bin/bash

# wait for the database

until python manage.py migrate
do
	echo "Waiting to connect to DB..."
	sleep 1
done

python manage.py loaddata dev.json

python manage.py runserver 0.0.0.0:8000
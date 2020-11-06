#!/bin/bash

echo "Running migrations..."
python manage.py migrate
echo "Creating sample conversation..."
python manage.py create_conversation
echo "Running server..."
python manage.py runserver 0:8000

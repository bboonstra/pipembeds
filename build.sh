#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python3 manage.py collectstatic --no-input  # Change python to python3

# Apply any outstanding database migrations
python3 manage.py makemigrations
python3 manage.py migrate  # Change python to python3

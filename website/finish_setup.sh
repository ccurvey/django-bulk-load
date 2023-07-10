#!/bin/sh

echo "creating databases"

psql postgres << EOF
create database demo3;
create database test_demo3
EOF

python manage.py makemigrations
python manage.py migrate

# replace the cookiecutter stuff in the templates
find demo3/templates -type f -exec sed -i 's/{{cookiecutter.project_name}}/demo3/g' {} +

# Django Project Template

Simple Django project template I pieced together while learning Django. Includes a base template and home page to get 
started with. The base template is based off of one of the Bootstrap examples. 


## How to install

When creating a new project use the `--template` parameter to clone the project template and change `project_name` to 
the name of your project.
 
    $ django-admin startproject project_name --template=http://github.com/donnywdavis/Django_Template/archive/master.zip
    
## Requirements.txt

After installing the project template install the included packages. Modify requirements.txt before running `pip install`
if you don't need all of the included packages.

    $ pip install -r requirements.txt
    
Initial packages that are included:

- [dj-database-url](https://github.com/kennethreitz/dj-database-url)
- [dj-static](https://github.com/kennethreitz/dj-static)
- [Django](https://github.com/django/django)
- [django-crispy-forms](https://github.com/maraujop/django-crispy-forms)
- [gunicorn](https://github.com/benoitc/gunicorn)
- [psycopg2](https://github.com/psycopg/psycopg2)
- [pytz](https://github.com/newvem/pytz)
- [requests](https://github.com/kennethreitz/requests)
- [static3](https://github.com/rmohr/static3)
- [whitenoise](https://github.com/evansd/whitenoise)

## Environment Variables

Use these environment variables to set up the environment to load the proper settings files and the secret key that is
used for validations and security.

- ENVIRONMENT - Set this to either DEVELOPMENT or PRODUCTION
- SECRET_KEY - Set your secret key here to be used by the application

## Procfile

When using the `startproject` command it will replace most instances of `{{ project_name }}` in the project to your
specified project name. It will not update the Procfile however. Replace `{{ project_name }}` in the Procfile with your
project name.

## Settings

The settings files are found in `/project_name/settings/`.

- \__init\__.py loads all of the common.py settings and then based on the `ENVIRONMENT` it will load either production.py
or dev.py.
- common.py contains all of the settings that will be used in both production and development environments.
- production.py contains only the settings that are used in production.
- dev.example.py contains only the settings that are used in development. Rename this file to dev.py so that it will be
found by the application.

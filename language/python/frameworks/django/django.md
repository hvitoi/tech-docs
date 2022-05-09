# Django

```shell
# Install django
pip3 install django

# Available commands
django-admin

# Create new project
django-admin startproject <project-name>

---------------------------------
# Starting the server (at localhost:8000)
python3 manage.py runserver

---------------------------------
# Add a new App to a Project
python3 manage.py startapp <app-name>
- New app must be included in the settings.py INSTALLED_APPS

---------------------------------
# Creating Migrations
python3 manage.py makemigrations        # Check if there are alterations in the model.py files

# Migrate the Database
python3 manage.py migrate

---------------------------------
# Creating a Super User for the Admin Panel
python3 manage.py createsuperuser

# Change password
python3 manage.py changepassword

---------------------------------
# Collecting Static Files Into One Folder
python3 manage.py collectstatic
```

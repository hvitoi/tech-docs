# django-admin

- If you are inside of a project, using the django-admin wrapper `manage.py`

## startproject

```shell
# Create new project
django-admin startproject "<project-name>" # creates a new subfolder
django-admin startproject "<project-name>" "." # installs it in the current existing folder
```

## runserver

```shell
# Starting the server
django-admin runserver # at localhost:8000 by default
django-admin runserver "3000" # specify port
```

## startapp

```shell
# Add a new App to a Project. It is included as a new folder in the root of the project
# The New app must also be included in the settings.py (INSTALLED_APPS variables) with the same name
django-admin startapp <app-name>
```

## makemigrations

```shell
# Creating Migrations
# Check if there are alterations in the model.py files
django-admin makemigrations
```

## migrate

```shell
# Migrate the Database
django-admin migrate
```

## createsuperuser

```shell
# Creating a Super User for the Admin Panel
python3 manage.py createsuperuser
```

## changepassword

```shell
# Change passwords
python3 manage.py changepassword
```

## collectstatic

```shell
# Collecting Static Files Into One Folder
python3 manage.py collectstatic
```

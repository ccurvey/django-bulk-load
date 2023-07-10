# Packages

As pydanny so eloquently put it: *This is what I want.  It might not be what you want.*

Look at Pipfile for specifics, but the general setup is:

## For production

* django + postgres
* mailauth for authentication
* bootstrap-related stuff for styling
* some other useful packages (requests, vanilla views, django-extensions etc)

## For Development

* black
* pytest
* factory-boy

# Project Setup

The core django settings will go in a directory called "website".  Then there
will be an app started with "project_name".

There's some very simple stuff in there, mostly so that I don't have to remember the
structure of things like urls.py and wiring all the urls files together.

If you look at settings.py, you'll see that I like to leave the standard django
settings file alone, then override or add to it at the bottom.  I find that that
makes it easier to see what settings were changed and why.

# How To Use

After running cookiecutter

## Install python packages
```
$ cd demo3
$ sh ./install_packages.sh
```

## Create PG database and superuser

```
$ pipenv shell
$ cd website
$ sh ./finish_setup.sh
```

## Start your server:

```
$ python manage.py runserver
```

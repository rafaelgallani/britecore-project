# Britecore Project - Backend
Developed using [Python 3](https://www.python.org/) with [Django](https://www.djangoproject.com/), as proposed in the project's requirements. [Django REST Framework](https://www.django-rest-framework.org/) and some add-ons were also added to make development faster. 

The chosen database was [PostgreSQL](https://www.postgresql.org/). Reasons: simple to use/setup and open-source ;)

Tests were built and checked with [coverage](https://coverage.readthedocs.io/en/coverage-5.5/), but they don't cover 100% of the existent cases :(

The production image uses [NGINX](https://www.nginx.com/) as a reverse proxy, and to serve the static files.

## Tools:
- `python`: `3.9.1`

You can check the other packages versions in the [`requirements.txt`](https://github.com/rafaelgalani/britecore-project/blob/master/backend/requirements.txt) file.

## Project setup (for Linux/Mac installations - tested in Arch Linux with `zsh`)

First, you need to create a virtual environment to ensure that your Python version will be enforced when installing the packages, and that they will be at the same location. To create a new virtual environment, run this command:

```
$ virtualenv -p $(which python3) venv
```

Now activate the virtual environment - needs to be done for every shell that will run within `python3` context:

```
$ source venv/bin/activate
```

And that's it. You're done. Now it's pretty straightforward - just install the requirements and run the local version:

```
$ pip3 install requirements.txt
$ python3 manage.py runserver
```

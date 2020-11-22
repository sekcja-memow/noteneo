# First steps
We assume you have python 3 instaled with pip.

We're using pipenv for package management and environment isolation. Start with installing dependencies. Make sure it is installed on your system, if not, run:
```sh
pip install pipenv
```

Now, install project dependencies and migrate the database. Don't worry if there is no sqlite database, it will be created in the process.
```sh
pipenv install
python manage.py migrate
```
You are ready to go, to start the app server run:
```sh
python manage.py runserver
```

# Api spec

## Authorization
Send `POST` request to `/auth` endpoint with `username` and `password` keys, and the response will contain the authentication token. Next, you need to attach it as authorization header to each request in form of
```
Authorization: Token YOUR_TOKEN_VALUE
```

# Common dev actions

## Adding superuser to database for tests
Password will be prompted after you run the command.
```sh
python manage.py createsuperuser --username user --email example@mail.com
```

## Generating superuser auth token
```sh
python manage.py drf_create_token user
```


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
Send `POST` request to `/api/users/token/` endpoint with `email` and `password` keys, and the response will contain the authentication token. Next, you need to attach it as authorization header to each request in form of
```
Authorization: Token YOUR_TOKEN_VALUE
```
If everything is `OK` you received:
```
{
    "token": <token>,
    "email": <email>,
    "user_id": <user_id>
}
```

## Create an account
To create an account send `POST` request to `/api/users/register/` endpoint with `email`, `name` and `password` keys, and the response will like this:
```
{
    "email": <email>,
    "name": <name>,
    "image": <default_image_url>,
    "postal_code": <postal_code>,
    "address": <address>,
    "country_code": <country_code>
}
```

## Profile
You can manage user's profile using `/api/users/profile/` endpoint.
Send `GET` request to get authenticated user's details or you can modifiy user's profile using `PUT` or `PATCH` request methods.

Example reponse for `GET` request:
```
{
    "email": <email>,
    "name": <name>,
    "image": <default_image_url>,
    "postal_code": <postal_code>,
    "address": <address>,
    "country_code": <country_code>
}
```

## Reset password
To reset user's password you can use the `/api/users/password-reset/` endpoint and send `POST` request with user's email:

Example usage:
```bash
curl -d "email=<user.email>" -X POST http://127.0.0.1:8000/api/users/password-reset/
```

In response, the user will receive an appropriate token by e-mail.

To confirm password reset you must send `POST` request with the token received by e-mail and new password:
```bash
curl -d "token=<token>>&password=<new_password>" -X POST http://127.0.0.1:8000/api/users/password-reset/confirm/
``` 

# Notes API
Send `GET` request to `/api/notes/` to list all available notes. 

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


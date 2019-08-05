# musicbrainz-django
Project to expose https://musicbrainz.org data. Started in #pycon-au-2019 sprints

## Get Started Developing

``` shell
virtualenv --python=python3 venv
```

## Design Decisions

We are using social-auth-app-django and installed it into our app using https://python-social-auth.readthedocs.io/en/latest/configuration/django.html

And implemengint our own based on https://python-social-auth-docs.readthedocs.io/en/latest/backends/implementation.html

Create a .env file

``` text
SOCIAL_AUTH_MUSICBRAINZ_KEY = yourkey.apps.googleusercontent.com
SOCIAL_AUTH_MUSICBRAINZ_SECRET = YOURSECRET
```

And use the following

``` shell
export $(grep -v '^#' .env | xargs -0)
```

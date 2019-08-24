# musicbrainz-django
Project to expose https://musicbrainz.org data. Started in #pycon-au-2019 sprints

## Design Decisions

We are using social-auth-app-django and installed it into our app using https://python-social-auth.readthedocs.io/en/latest/configuration/django.html

And implement our own based on https://python-social-auth-docs.readthedocs.io/en/latest/backends/implementation.html . Since spotify also uses oauth 2 it was copied as a template.

Create a .env file. In vs code type `code .env` and set up your varibles 1 per line. Get yourself a developer application OAUTH keys from https://musicbrainz.org/account/applications

``` text
SOCIAL_AUTH_MUSICBRAINZ_KEY=
SOCIAL_AUTH_MUSICBRAINZ_SECRET=YOURSECRET
```

And use the following everytime your .env changes to update your Terminal with the correct environmnet varibales.

``` shell
export $(grep -v '^#' .env | xargs -0)
```

## Get Started Developing

Install your dev environment from virtualenv

### virtualenv

his is required once only. Unless you need to delete your venv directory. Note when you update python from 3.7.3 to 3.7.4 you may be best to remove venv and restall dependencies. venv is just a convention name for calling your installation directly. This `venv` folder is on purposely in the gitignore.

``` shell
virtualenv --python=python3.7 venv
```

Every time you log into your terminal. Note . is just short for typing `source`

``` shell
. venv/bin/activate
```

Note your Terminal now having `(venv)`

``` shell
pip install -r requirements.txt
```

The following are the automaic routes that come with python social auth

``` text
^login/(?P<backend>[^/]+)/$ [name='begin']
^complete/(?P<backend>[^/]+)/$ [name='complete']
^disconnect/(?P<backend>[^/]+)/$ [name='disconnect']
^disconnect/(?P<backend>[^/]+)/(?P<association_id>\d+)/$ [name='disconnect_individual']
```

## Known issues

Refresh token is not populated.

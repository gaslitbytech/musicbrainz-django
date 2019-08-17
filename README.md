# musicbrainz-django
Project to expose https://musicbrainz.org data. Started in #pycon-au-2019 sprints

## Get Started Developing

Install venv into this projet. This is on purposely in the gitignore. This is required once only. Unless you need to delete your venv directory. Note when you update python from 3.7.3 to 3.7.4 you may be best to remove venv and restall dependencies. 

``` shell
virtualenv --python=python3 venv
```

Every time you log into your terminal. Note . is just short for `source`

``` shell
. venv/bin/activate
```

``` shell
pip install -r requirements.txt
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

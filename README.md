# musicbrainz-django

Project to expose <https://musicbrainz.org> data. Started in #pycon-au-2019 sprints

This evolved into a test bed of other experiments learing django.

## Design Decisions

We are using social-auth-app-django and installed it into our app using <https://python-social-auth.readthedocs.io/en/latest/configuration/django.html>

And implement our own based on <https://python-social-auth-docs.readthedocs.io/en/latest/backends/implementation.html>. Since spotify also uses oauth 2 it was copied as a template.

To introduce the map using django-leaflet and <https://docs.djangoproject.com/en/3.0/ref/contrib/gis/tutorial/>.

To build on geodjango learning we can use <https://openflights.org/data.html>

Create a .env file. In vs code type `code .env` and set up your varibles 1 per line.

1. Get yourself a developer application OAUTH keys from <https://musicbrainz.org/account/applications>. The redirect URL is <http://localhost:8000/complete/musicbrainz/>

2. Repeat for spotify <https://developer.spotify.com/dashboard/applications>. The redirect URL is <http://localhost:8000/complete/spotify/>

3. Run postgis with docker on port 5430 and create a database called musicbrainz-django

    ``` bash
    MOUNT_DATA_PATH=~/Documents/postgresql-11/data docker run --rm --name alpine-pg11-postgis2dot5 -p 5430:5432 -v $MOUNT_DATA_PATH:/var/lib/postgresql/data mdillon/postgis:11-alpine

    # I have a local postgresql 12 installed on my dev box. Prefer docker with postgis
    /Library/PostgreSQL/12/bin/psql --host=localhost --port=5430 --username=postgres
    postgres=# CREATE DATABASE "musicbrainz-django";
    ```

``` text
SOCIAL_AUTH_MUSICBRAINZ_KEY=
SOCIAL_AUTH_MUSICBRAINZ_SECRET=YOURSECRET
DATABASE_URL=postgres://postgres@localhost:5430/musicbrainz-django
```

And use the following everytime your .env changes to update your Terminal with the correct environmnet varibales.

## Configure Development

Install your dev environment from Pipenv or virtualenv. This project talks through virtualenv though commits a copy of Pipfile's.

### pipenv

``` shell
pipenv install --dev
```

Activate the shell. VS Code terminal may do this for you. Needs to be done every Terminal window.

``` shell
pipenv shell
```

### virtualenv

This is required once only. Unless you need to delete your venv directory. Note when you update python from 3.7.3 to 3.7.4 you may be best to remove venv and restall dependencies. venv is just a convention name for calling your installation directly. This `venv` folder is on purposely in the gitignore.

``` shell
virtualenv --python=python3.7 venv
```

``` shell
export $(grep -v '^#' .env | xargs -0)
```

Every time you log into your terminal. Note . is just short for typing `source`

``` shell
. venv/bin/activate
```

Note your Terminal now having `(venv)`

``` shell
pip install -r requirements.txt
```

### Once per db

Create the schema on the database

``` shell
python manage.py migrate
```

Load the airports

``` shell
python manage.py shell
```

``` python
from world.load import run_airports
run_airports()
```

### Daily Developing

Everytime you start a Terminal

#### pipenv daily

For Pipenv

``` shell
pipenv shell
```

#### virtualenv daily

Every time you log into your terminal. Note . is just short for typing `source`

``` shell
. venv/bin/activate
```

### common

Change to dir to django root

``` shell
cd musicbrainz/
```

### Misc Notes

The following are the automaic routes that come with python social auth.

``` text
^login/(?P<backend>[^/]+)/$ [name='begin']
^complete/(?P<backend>[^/]+)/$ [name='complete']
^disconnect/(?P<backend>[^/]+)/$ [name='disconnect']
^disconnect/(?P<backend>[^/]+)/(?P<association_id>\d+)/$ [name='disconnect_individual']
```

## TODO

1. musicbrains api. Get the refresh token.
2. ~~Use python social auth fork for music brainz <http://localhost:8000/social/complete/musicbrainz/>. Like done in <https://github.com/tourdownunder/django-vue-template>.~~

3. Make thise instructions use Pipenv.

    or just keep requirements.txt upto date using Pipenv.

    ``` sh
    jq -r '.default
            | to_entries[]
            | .key + .value.version' \
        Pipfile.lock > requirements.txt
    ```

4. Consider integration with Song Kick <https://www.songkick.com/developer/getting-started>

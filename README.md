# Malvo

Programming Contest Platform

## Screenshots

- [Screenshot 1](http://imgur.com/44tQMSU)
- [Screenshot 2](http://imgur.com/LvuHf7P)
- [Screenshot 3](http://imgur.com/qdliVUK)
- [Screenshot 4](http://imgur.com/pqQVzzc)
- [Screenshot 5](http://imgur.com/F0t6Ni6)

## Instructions for local development

1. Create a virtualenv instance and activate it.

```bash
virtualenv -p `which python3` venv
source venv/bin/activate
```

2. Setup Postgres database. Before installing `psycopg2` package from requirements you might need to install `libpq-dev` and `python3-dev`.

```bash
sudo apt-get install libpq-dev python3-dev
# Install postgres server and client if you haven't already
sudo apt-get install postgresql-9.4 postgresql-client-9.4
```

   Create a postgres user and database.

```bash
sudo -i -u postgres
createuser -P -s malvo
createdb malvo
```

3. Install dependencies.

```bash
pip install -r requirements.txt
bower install
```

4. Add a `secrets.json` file inside `data/conf`. It should contain the following (for example):

```json
{
  "secret_key": "some-secret-key",
  "db_name": "malvo",
  "db_user": "malvo",
  "db_host": "localhost",
  "db_password": "your-psql-user-password",
  "allowed_hosts": [
    "127.0.0.1",
    "localhost"
  ]
}
```

5. Migrate and create a superuser.

```bash
./manage.py migrate
./manage.py createsuperuser
```

6. Run server.

```bash
./manage.py runserver
```


## Production Deployment

Collect all the static files inside `data/static_root`:

```bash
./manage.py collectstatic
```

You can serve them through a proxy server.

Start application through `gunicorn`.

```bash
gunicorn malvo.wsgi:application --name malvo --bind 0.0.0.0:8000 --workers 3
```

## Heroku Deployment

```bash
heroku create
heroku buildpacks:set heroku/python
heroku buildpacks:add --index 1 heroku/nodejs
heroku config:set MALVO_PLATFORM='heroku'
git push heroku master
heroku run python manage.py migrate
```

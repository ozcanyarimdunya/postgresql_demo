### settings.py
```
ALLOWED_HOSTS = ['*']
...

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',  # set in docker-compose.yml
        'PORT': 5432  # default postgres port
    }
}
```

### migrate
```
docker-compose run web python /code/manage.py migrate --noinput
```

### run
```
doc up --build -d
```
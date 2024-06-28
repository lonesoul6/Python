import environ

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': env('PGDATABASE'),
    'USER': env('PGUSER'),
    'PASSWORD': env('PGPASSWORD'),
    'HOST': env('PGHOST'),
    'PORT': env.int('PGPORT', default=5432),
    'OPTIONS': {
      'sslmode': 'require',
    },
  }
}


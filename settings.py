# Add these at the top of your settings.py
from os import getenv
from dotenv import load_dotenv
import psycopg2

# Load environment variables from .env file
load_dotenv()

# Define your database connection parameters from environment variables
db_params = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': getenv('PGDATABASE'),
    'USER': getenv('PGUSER'),
    'PASSWORD': getenv('PGPASSWORD'),
    'HOST': getenv('PGHOST'),
    'PORT': getenv('PGPORT', 5432),
    'OPTIONS': {
      'sslmode': 'require',
    }
}}



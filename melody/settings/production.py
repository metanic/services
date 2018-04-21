import dj_database_url

from melody.settings.defaults import env_value

# We specifically allow `import *` in this case to pull in expected settings
from melody.settings.defaults import *  # noqa

DEBUG = False

ALLOWED_HOSTS = ['services.melody.monokro.me']
FRONTEND_URL = 'melody.monokro.me'
MELODY_REDIRECT_URL = 'https://melody.monokro.me/'
ROOT_URLCONF = 'melody.core.urls.production'
SECRET_KEY = env_value('secret_key')
STATIC_URL = env_value('static_url')

DATABASES = {
    'default': dj_database_url.config(conn_max_age=500),
}
import os


def env_value(name, default=None):
    name = name.upper()
    return os.environ.get(f'MELODY_${name}', os.environ.get(name, default))


def project_path(*paths):
    return os.path.join(os.getcwd(), *paths)


EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'
DEFAULT_FROM_EMAIL = 'services@melody.monokro.me'
DATE_FORMAT = 'Y-m-d'
USE_L10N = True

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.admin',

    'anymail',
    'channels',
    'rest_framework',

    'melody.accounts',
    'melody.collector',
    'melody.core',
    'melody.posts',
    'melody.realtime',
]

MIDDLEWARE = [
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    'melody.core.middleware.CORSMiddleware',
]

TEMPLATES = [
    {
        'APP_DIRS': True,
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS':
            {
                'context_processors':
                    [
                        'django.contrib.auth.context_processors.auth',
                        'django.contrib.messages.context_processors.messages',
                        'melody.core.context_processors.frontend_url',
                    ],
            }
    },
]

CHANNEL_LAYERS = {
    'default':
        {
            'BACKEND': 'asgiref.inmemory.ChannelLayer',
            'ROUTING': 'melody.realtime.routing.routes',
        }
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES':
        ['rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'],
}

ANYMAIL = {
    'MAILGUN_API_KEY': env_value('MAILGUN_API_KEY'),
    'MAILGUN_SENDER_DOMAIN': 'melody.local',
}

COLLECTION_SERIALIZER_TYPES = {
    'post': ('melody.posts.api.serializers', 'PostSerializer'),
}

CORS_ALLOWED_HEADERS = [
    'Accept',
    'Content-Type',
    'Authorization',
]

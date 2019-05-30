from .base import *

secrets = json.load(open(os.path.join(SECRET_DIR, 'dev.json')))
DEBUG = True

ALLOWED_HOSTS = secrets['ALLOWED_HOSTS']

# dev 에서만 사용되는 app
INSTALLED_APPS += [
    'django_extensions',
    'storages',
    'django_celery_beat',
    'django_celery_results',
]

# static file 을 aws S3 를 통해 불러오게 한다.
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'config.storages.S3StaticStorage'

# WSGI(이곳에는 적어주지 않아도 잘 동작한다.
# 아마도 request 를 받을 때는 wsgi -> settings 방향이고 respond 나 다른 경우는 반대 방향으로 추측된다
WSGI_APPLICATION = 'config.wsgi.dev.application'

# DB
DATABASES = secrets['DATABASES']

# CELERY + Redis
CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'

# # CELERY_BEAT
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TAST_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Seoul' # Celery beat가 스케줄러이기 때문에 시간에 대한 정의를 해야함

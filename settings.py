
import os, json

# go through environment variables and override them
def get_from_env(var, default):
    if os.environ.has_key(var):
        return os.environ[var]
    else:
        return default

DEBUG = (get_from_env('DEBUG', '1') == '1')
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Ben Adida', 'ben@adida.net'),
)

MANAGERS = ADMINS

# is this the master Helios web site?
MASTER_HELIOS = (get_from_env('MASTER_HELIOS', '0') == '1')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'helios',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

SOUTH_DATABASE_ADAPTERS = {'default':'south.db.postgresql_psycopg2'}

# override if we have an env variable
if get_from_env('DATABASE_URL', None):
    import dj_database_url
    DATABASES['default'] =  dj_database_url.config()
    DATABASES['default']['ENGINE'] = 'dbpool.db.backends.postgresql_psycopg2'
    DATABASES['default']['OPTIONS'] = {'MAX_CONNS': 1}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
STATIC_URL = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = get_from_env('SECRET_KEY', 'replaceme')

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader'
)

MIDDLEWARE_CLASSES = (
    # make all things SSL
    'sslify.middleware.SSLifyMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware'
)

ROOT_URLCONF = 'urls'

ROOT_PATH = os.path.dirname(__file__)
TEMPLATE_DIRS = (
    ROOT_PATH,
    os.path.join(ROOT_PATH, 'templates')
)

INSTALLED_APPS = (
#    'django.contrib.auth',
#    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    ## needed for queues
    'djcelery',
    'kombu.transport.django',
    ## needed for schema migration
    'south',
    ## HELIOS stuff
    'helios_auth',
    'helios',
    'server_ui',
)

##
## HELIOS
##


MEDIA_ROOT = ROOT_PATH + "media/"

# a relative path where voter upload files are stored
VOTER_UPLOAD_REL_PATH = "voters/%Y/%m/%d"


# Change your email settings
DEFAULT_FROM_EMAIL = get_from_env('DEFAULT_FROM_EMAIL', 'ben@adida.net')
DEFAULT_FROM_NAME = get_from_env('DEFAULT_FROM_NAME', 'Ben for Helios')
SERVER_EMAIL = '%s <%s>' % (DEFAULT_FROM_NAME, DEFAULT_FROM_EMAIL)

LOGIN_URL = '/auth/'
LOGOUT_ON_CONFIRMATION = True

# The two hosts are here so the main site can be over plain HTTP
# while the voting URLs are served over SSL.
URL_HOST = get_from_env("URL_HOST", "http://localhost:8000")

# IMPORTANT: you should not change this setting once you've created
# elections, as your elections' cast_url will then be incorrect.
# SECURE_URL_HOST = "https://localhost:8443"
SECURE_URL_HOST = get_from_env("SECURE_URL_HOST", "http://localhost:8000")

# this additional host is used to iframe-isolate the social buttons,
# which usually involve hooking in remote JavaScript, which could be
# a security issue. Plus, if there's a loading issue, it blocks the whole
# page. Not cool.
SOCIALBUTTONS_URL_HOST= get_from_env("SOCIALBUTTONS_URL_HOST", "http://localhost:8000")

# election stuff
SITE_TITLE = get_from_env('SITE_TITLE', 'Helios Voting')

# FOOTER links
FOOTER_LINKS = json.loads(get_from_env('FOOTER_LINKS', '[]'))
FOOTER_LOGO_URL = get_from_env('FOOTER_LOGO_URL', None)

WELCOME_MESSAGE = get_from_env('WELCOME_MESSAGE', "This is the default message")

HELP_EMAIL_ADDRESS = get_from_env('HELP_EMAIL_ADDRESS', 'help@heliosvoting.org')

AUTH_TEMPLATE_BASE = "server_ui/templates/base.html"
HELIOS_TEMPLATE_BASE = "server_ui/templates/base.html"
HELIOS_ADMIN_ONLY = False
HELIOS_VOTERS_UPLOAD = True
HELIOS_VOTERS_EMAIL = True

# are elections private by default?
HELIOS_PRIVATE_DEFAULT = False

# authentication systems enabled
#AUTH_ENABLED_AUTH_SYSTEMS = ['password','facebook','twitter', 'google', 'yahoo']
AUTH_ENABLED_AUTH_SYSTEMS = get_from_env('AUTH_ENABLED_AUTH_SYSTEMS', 'google').split(",")
AUTH_DEFAULT_AUTH_SYSTEM = get_from_env('AUTH_DEFAULT_AUTH_SYSTEM', None)

# facebook
FACEBOOK_APP_ID = get_from_env('FACEBOOK_APP_ID','')
FACEBOOK_API_KEY = get_from_env('FACEBOOK_API_KEY','')
FACEBOOK_API_SECRET = get_from_env('FACEBOOK_API_SECRET','')

# twitter
TWITTER_API_KEY = ''
TWITTER_API_SECRET = ''
TWITTER_USER_TO_FOLLOW = 'heliosvoting'
TWITTER_REASON_TO_FOLLOW = "we can direct-message you when the result has been computed in an election in which you participated"

# the token for Helios to do direct messaging
TWITTER_DM_TOKEN = {"oauth_token": "", "oauth_token_secret": "", "user_id": "", "screen_name": ""}

# LinkedIn
LINKEDIN_API_KEY = ''
LINKEDIN_API_SECRET = ''

# CAS (for universities)
CAS_USERNAME = get_from_env('CAS_USERNAME', "")
CAS_PASSWORD = get_from_env('CAS_PASSWORD', "")
CAS_ELIGIBILITY_URL = get_from_env('CAS_ELIGIBILITY_URL', "")
CAS_ELIGIBILITY_REALM = get_from_env('CAS_ELIGIBILITY_REALM', "")

# email server
EMAIL_HOST = get_from_env('EMAIL_HOST', 'localhost')
EMAIL_PORT = int(get_from_env('EMAIL_PORT', "2525"))
EMAIL_HOST_USER = get_from_env('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = get_from_env('EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = (get_from_env('EMAIL_USE_TLS', '0') == '1')

# set up logging
import logging
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s %(levelname)s %(message)s'
)


# set up django-celery
# BROKER_BACKEND = "kombu.transport.DatabaseTransport"
BROKER_URL = "django://"
CELERY_RESULT_DBURI = DATABASES['default']
import djcelery
djcelery.setup_loader()


# for testing
TEST_RUNNER = 'djcelery.contrib.test_runner.CeleryTestSuiteRunner'
# this effectively does CELERY_ALWAYS_EAGER = True

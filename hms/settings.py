from corsheaders.defaults import default_methods,default_headers
import environ, os 
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-wd!fk90x(zhq^0ea-y3xqdpaxt31=9xc#qj5zb*h8h!xstio$9"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost',
                 '127.0.0.1',
                 'http://localhost:8080',
                 'c6c2-102-0-6-211.ngrok-free.app'
                 ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'djoser',
    'rest_framework',
    'rest_framework.authtoken',
    'billing_management',
    'bookings',
    'customer_support',
    'doctor_profile.apps.DoctorProfileConfig',
    'company',
    'inventory_management',
    'lab_management',
    'patients_registration.apps.PatientsRegistrationConfig',
    'financial_accounts_chart_of_accounts.apps.FinancialAccountsChartOfAccountsConfig',
    'payroll',
    'rooms',
    'xtra.apps.XtraConfig',
    'statistical_data',
    'users.apps.UsersConfig',
    'django_filters',
    'import_export',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'hms.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASS'),
        'HOST':'localhost',
        'PORT':'8000',
        "TEST": {
            "NAME": env('TEST_DATABASE'),
        },
        'ATOMIC_REQUESTS': True,

    }
}

AUTH_USER_MODEL = 'users.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.IsAuthenticated',
    # ],
    "DATE_INPUT_FORMATS": ["%Y-%m-%d"],
}



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR /'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

        #DJOSER SETTINGS
DJOSER = {
    'LOGIN_FIELD': 'email',
    # 'ACTIVATION_URL': 'my-account/activate/{uid}/{token}',
    'PASSWORD_RESET_CONFIRM_URL': 'api/v1/password-reset/{uid}/{token}',
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    'LOGOUT_ON_PASSWORD_CHANGE': True
}

        #CORS SETTINGS
CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_METHODS = list(default_methods) + []

CORS_ALLOW_HEADERS = list(default_headers) + ["cache-control"]


        #CSRF SETTINGS

CSRF_TRUSTED_ORIGINS = ['http://localhost:8080','https://c6c2-102-0-6-211.ngrok-free.app']
CSRF_COOKIE_SECURE = False

#Email Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

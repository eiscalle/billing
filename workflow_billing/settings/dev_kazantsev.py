from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'wf_billing',
        'USER': 'postgres',
        'PASSWORD': '1',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}

TWO_CHECKOUT_PRIVATE_KEY = '56450759-5E57-42A8-B257-09FB3E6E4AC9'
TWO_CHECKOUT_PUBLIC_KEY = '2DFC0377-BB4F-42D4-9B41-2C65FE701835'
TWO_CHECKOUT_MODE = 'sandbox'
TWO_CHECKOUT_SELLER_ID = '901323033'

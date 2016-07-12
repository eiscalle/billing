import twocheckout

from django.conf import settings


def authorize():
    return twocheckout.Api.auth_credentials({
        'private_key': settings.TWO_CHECKOUT_PRIVATE_KEY,
        'seller_id': settings.TWO_CHECKOUT_SELLER_ID,
        'mode': settings.TWO_CHECKOUT_MODE,
    })
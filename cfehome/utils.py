import datetime
from django.conf import settings


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'expiryMS': int(round(((datetime.datetime.utcnow() + settings.JWT_AUTH['JWT_EXPIRATION_DELTA']).timestamp() * 1000))) # FIXME line too long
    }

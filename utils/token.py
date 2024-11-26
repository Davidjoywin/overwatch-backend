from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import User

from jwt import decode, ExpiredSignatureError
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken


def parse_token(token):
    secret_key = settings.SECRET_KEY

    return {
        "access": {
            "token": token['access'],
            "expiration_date": int(get_token_expiration(token['access'], secret_key))
        },
        "refresh": {
            "token": token['refresh'],
            "expiration_data": int(get_token_expiration(token['refresh'], secret_key))
        }
    }


def get_token_expiration(token, secret_key):
    
    try:
        decoded_token = decode(token, secret_key, algorithms=['HS256'])
        
        # get the expiration timestamp from the decoded token
        expiration_timestamp = decoded_token['exp']

        # get the current timestamp
        current_timestamp = datetime.now().timestamp()

        seconds_remaining = expiration_timestamp - current_timestamp

        return seconds_remaining
    
    except ExpiredSignatureError:
        print("Token expired")
        return 0
    
    except Exception as e:
        print(f"Error decoding token: {e}")
        return None

def create_token(user):
    token = RefreshToken.for_user(user)

    token = {
        "refresh": str(token),
        "access": str(token.access_token),
    }

    token = parse_token(token)

    return token

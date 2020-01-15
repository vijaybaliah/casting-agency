import json
from flask import request
from functools import wraps
from jose import jwt
from urllib.request import urlopen

from src.utils.helpers import get_env_variable

AUTH0_DOMAIN = get_env_variable('AUTH0_DOMAIN', 'vijayfsnd.auth0.com')
ALGORITHMS = [get_env_variable('ALGORITHMS', 'RS256')]
API_AUDIENCE = get_env_variable('API_AUDIENCE', 'casting')


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


def get_token_auth_header():
    auth = request.headers.get('Authorization', None)
    if not auth:
        raise AuthError({
            'code': 'authorization_header_missing',
            'message': 'Authorization header is expected.',
            'success': False
        }, 401)
    parts = auth.split()
    if parts[0].lower() != 'bearer':
        raise AuthError({
            'code': 'invalid_header',
            'message': 'Authorization header must start with "Bearer".',
            'success': False
        }, 401)
    elif len(parts) == 1:
        raise AuthError({
            'code': 'invalid_header',
            'message': 'Token not found.',
            'success': False
        }, 401)
    elif len(parts) > 2:
        raise AuthError({
            'code': 'invalid_header',
            'message': 'Authorization header must be bearer token.',
            'success': False
        }, 401)

    token = parts[1]
    return token


def check_permissions(permission, payload):
    if 'permissions' in payload:
        if permission in payload['permissions']:
            return True
        raise AuthError({
            'code': 'invalid_permission',
            'message': 'Requested permission is not found',
            'success': False
        }, 401)


def verify_decode_jwt(token):
    '''
        Gets the public key from auth0
    '''
    jsonurl = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
    jwks = json.loads(jsonurl.read())

    '''
        gets the jwt keys from the token passed in request header
    '''
    unverified_header = jwt.get_unverified_header(token)
    rsa_key = {}

    '''
        If keys does not exists then it throws invalid_header error
    '''
    if 'kid' not in unverified_header:
        raise AuthError({
            'code': 'invalid_header',
            'message': 'Authorization malformed.',
            'success': False
        }, 401)

    '''
        It iterates through the list of jwt keys and checks if both the
        keys matches. If it does we can generate rsa key which is used
        to decode the jwt which then can be used to read the permissions
    '''
    for key in jwks['keys']:
        if key['kid'] == unverified_header['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e']
            }

    '''
        Finally we decrypt the jwt with the generated rsa_key, the algorithms
        we used during auth0 config, audience, and domain
    '''
    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer='https://' + AUTH0_DOMAIN + '/'
            )

            return payload
        except jwt.ExpiredSignatureError:
            raise AuthError({
                'code': 'token_expired',
                'message': 'Token expired.',
                'success': False
            }, 401)
        except jwt.JWTClaimsError:
            raise AuthError({
                'code': 'invalid_claims',
                'message': 'Incorrect claims. Please\
                , check the audience and issuer.',
                'success': False
            }, 401)
        except Exception:
            raise AuthError({
                'code': 'invalid_header',
                'message': 'Unable to parse authentication token.',
                'success': False
            }, 400)
    raise AuthError({
        'code': 'invalid_header',
                'message': 'Unable to find the appropriate key.',
                'success': False
    }, 400)


def requires_auth(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()
            payload = verify_decode_jwt(token)
            check_permissions(permission, payload)
            return f(payload, *args, **kwargs)

        return wrapper
    return requires_auth_decorator

import os


def get_env_variable(name, option):
    try:
        ENVIRONMENT = os.environ.get('ENVIRONMENT', 'development')
        if ENVIRONMENT == 'development':
            return option
        else:
            return os.environ.get(name)
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)

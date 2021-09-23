import const as const
import os

# Default configurations are common across environments
class DefaultConfig(object):
    # Machine Configuration
    HOST_MACHINE_IP = '0.0.0.0'
    HOST_MACHINE_PORT = 5000

    # Debug Configuration
    DEBUG = os.environ.get('DEBUG')

    # Logging Configuration
    APPLICATION_LOG_LEVEL = const.log_level_debug

    # Database Configuration
    DB_URI = os.environ.get('DB_URI')
    DB_NAME = os.environ.get('DB_NAME')
    DB_PORT = 27017
    DB_CONNECTION_TIMEOUT = 100000  # in milliseconds (100 seconds)

    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')

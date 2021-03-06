from functools import lru_cache

from environs import Env

env = Env()
env.read_env()


@lru_cache
def get_database_url():
    host = env.str('DATABASE_HOST', '0.0.0.0')
    port = env.str('DATABASE_PORT', '5432')
    user = env.str('DATABASE_USER', 'postgres')
    database = env.str('DATABASE_NAME', 'postgres')
    password = env.str('DATABASE_PASSWORD', 'mysecretpassword')

    return f'postgresql://{user}:{password}@{host}:{port}/{database}'


DATABASE_URL = get_database_url()

SERVICE_HOST = env.str('SERVICE_HOST', '127.0.0.1')
SERVICE_PORT = env.str('SERVICE_PORT', '8000')
SERVICE_TEST = env.bool('SERVICE_TEST', False)

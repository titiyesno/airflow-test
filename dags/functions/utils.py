import os

def get_destination_database_config():
    return {
        'host': os.environ.get('DESTINATION_DATABASE_HOST'),
        'port': os.environ.get('DESTINATION_DATABASE_PORT'),
        'dbname': os.environ.get('DESTINATION_DATABASE_NAME'),
        'username': os.environ.get('DESTINATION_DATABASE_USERNAME'),
        'password': os.environ.get('DESTINATION_DATABASE_PASSWORD')
    }

def get_source_database_config():
    return {
        'host': os.environ.get('SOURCE_DATABASE_HOST'),
        'port': os.environ.get('SOURCE_DATABASE_PORT'),
        'dbname': os.environ.get('SOURCE_DATABASE_NAME'),
        'username': os.environ.get('SOURCE_DATABASE_USERNAME'),
        'password': os.environ.get('SOURCE_DATABASE_PASSWORD')
    }


def create_uri(conf):
    
    return f"postgresql+psycopg2://{conf['username']}:{conf['password']}@{conf['host']}:{conf['port']}/{conf['dbname']}"


def gomigrate_create_uri(conf):
    
    return f"postgresql://{conf['username']}:{conf['password']}@{conf['host']}:{conf['port']}/{conf['dbname']}"

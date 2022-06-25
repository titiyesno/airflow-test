from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
from functions import utils

def query_function():

    conf = utils.get_destination_database_config()
    uri = utils.create_uri(conf)
    engine = create_engine(uri, poolclass=NullPool)
    conn = engine.connect()

    try:
        conn.execute(open('/opt/airflow/dags/functions/query/query_monthly_best_seller.sql', 'r').read())
    except Exception as ex:
        print("Exception: ", ex)
        raise
    finally:
        conn.close()
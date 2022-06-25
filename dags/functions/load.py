import os
import json
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
from datetime import datetime, timedelta
from functions import utils

def load_data():

    source_conf = utils.get_source_database_config()
    source_uri = utils.create_uri(source_conf)
    source_engine = create_engine(source_uri, poolclass=NullPool)
    source_conn = source_engine.connect()

    destination_conf = utils.get_destination_database_config()
    

    print("Getting all olist tables..")
    q_result = source_conn.execute("select table_name from information_schema.tables where table_name like 'olist%%'").fetchall()
    list_of_tables = list(map(''.join, q_result))
    print("List of Tables: ",list_of_tables)
    source_conn.close()

    for table in list_of_tables:
        source_conn = source_engine.connect()
        print("Getting data from table ",table)
        select_result = source_conn.execute(f"select * from {table}").fetchall()
        result = reshape_result(select_result)
        source_conn.close()

        df = pd.DataFrame(result)
        try:
            destination_uri = utils.create_uri(destination_conf)
            destination_engine = create_engine(destination_uri)
            df.to_sql(table, destination_engine, if_exists= 'replace', index= False)

        except Exception as ex:
            print("Exception: ", ex)

        finally:
            destination_engine.dispose()
    print("Finished loading all data.")


def reshape_result(query_result):
    final_dict = {}

    for r in query_result:
        d = dict(r)
        for key, value in d.items():
            if key in final_dict:
                final_dict[key].append(normalize_datatype(value))
            else:
                final_dict[key] = [normalize_datatype(value)]
    
    return final_dict


def normalize_datatype(data):
    if type(data) == datetime:
        return data.strftime("%Y-%m-%d %H:%M:%S")
    if type(data) == timedelta:
        total_seconds = data.total_seconds()
        minutes = int(round(total_seconds / 60))

        return minutes
    
    return data


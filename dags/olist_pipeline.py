import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from functions import start, load, utils
from functions.query import query_monthly_total_purchase, query_monthly_best_seller


default_args = {
    'owner': 'ttsnovar',
    'depends_on_past': False,
    'start_date': datetime(2021, 4, 21, 0, 0, 0),
    'retries': 2,
    'retry_delay': timedelta(minutes=5)
}

dag_concurrency = 2

dag = DAG(
    'olist_pipeline',
    default_args=default_args,
    schedule_interval='0 * * * *',
    catchup=False,
    concurrency=dag_concurrency
)

point_start = PythonOperator(
    task_id='point_start',
    python_callable=start.migratedb,
    dag=dag
)

point_etl_finish = DummyOperator(task_id='point_etl_finish', dag=dag)

query_monthly_total_purchase = PythonOperator(
    task_id='query_monthly_total_purchase',
    python_callable=query_monthly_total_purchase.query_function,
    dag=dag
)

query_monthly_best_seller = PythonOperator(
    task_id='query_monthly_best_seller',
    python_callable=query_monthly_best_seller.query_function,
    dag=dag
)

point_end = DummyOperator(task_id='point_end', dag=dag)


load_task = PythonOperator(
    task_id=f'load_task',
    python_callable=load.load_data,
    dag=dag
)

point_start >> load_task >> point_etl_finish

point_etl_finish >> query_monthly_total_purchase >> query_monthly_best_seller >> point_end
import datetime as dt
from pathlib import Path

import pandas as pd
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

dag=DAG(
    dag_id="09_no_catchup",
    start_date=dt.datetime(year=2022, month=5, day=1),
    end_date=dt.datetime(year=2022, month=5, day=31),
    schedule_interval=dt.timedelta(days=1),
    catchup=False,
    tags=['igkim', 'test'],
)

fetch_events=BashOperator(
    task_id="fetch_events",
    bash_command=(
        "curl -o /opt/airflow/igkim/events.txt"
        " "
        "http://192.168.103.156:4399/events"
    ),
    dag=dag,
)

print_events=BashOperator(
    task_id="print_events",
    bash_command=(
        "echo "
        "\"start_date={{execution_date.strftime('%Y-%m-%d')}}\nend_date={{next_execution_date.strftime('%Y-%m-%d')}}\""
        " >> /opt/airflow/igkim/{{execution_date.strftime('%Y%m%d')}}-{{next_execution_date.strftime('%Y%m%d')}}"
    ),
    dag=dag
)

fetch_events >> print_events
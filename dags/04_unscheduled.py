import datetime as dt
from pathlib import Path

import pandas as pd
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

dag=DAG(
    dag_id="04_unscheduled",
    start_date=dt.datetime(2022, 5, 25),
    schedule_interval=None,
    tags=['igkim', 'test'],
)

fetch_events=BashOperator(
    task_id="fetch_events",
    bash_command=(
        "curl -o /home/igkim/apps/study/result/events.json "
        "http://192.168.103.156:4399/events"
    ),
    dag=dag,
)

fetch_events
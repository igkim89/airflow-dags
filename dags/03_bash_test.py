import datetime

import pendulum

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id='03_bash_test',
    schedule_interval='0 0 * * *',
    start_date=pendulum.datetime(2022, 5, 29, tz="Asia/Seoul"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=['igkim', 'test'],
    params={"name": "igkim"},
) as dag:
    run_bash = BashOperator(
        task_id='echo_hostname',
        bash_command='hostname -a',
    )

run_bash
import datetime

import pendulum

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id='01_exe_date',
    schedule_interval='0 * * * *',
    start_date=pendulum.datetime(2022, 8, 1, tz="Asia/Seoul"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=['igkim', 'test'],
    params={"name": "igkim"},
) as dag:
    run_bash = BashOperator(
        task_id='ds_touch',
        bash_command='touch /opt/airflow/logs/ds-{{ds}}.tmp',
    )

run_bash
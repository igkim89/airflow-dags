import os

import airflow.utils.dates as dates
from airflow import DAG
# from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from urllib import request

DIR_PATH = "/opt/airflow/data/wiki-po"

dag = DAG(
    dag_id="12_wiki_collector_po",
    start_date=dates.days_ago(1),
    schedule_interval="@hourly",
    catchup=False,
    tags=['igkim', 'test'],
)


def _mkdir_path(path):
    try:
        if not os.path.exists(path):
            os.mkdir(path)
    except Exception as e:
        print(f"[ERROR] {e}")


def _get_data(year, month, day, hour):
    # year, month, day, hour, *_=execution_date.timetuple()

    url = (
        "https://dumps.wikimedia.org/other/pageviews/"
        f"{year}/{year}-{month:0>2}/"
        f"pageviews-{year}{month:0>2}{day:0>2}-{hour:0>2}0000.gz"
    )

    print(url)

    request.urlretrieve(url, DIR_PATH + f"/{year}{month:0>2}{day:0>2}-{hour:0>2}.gz")


mkdir_path = PythonOperator(
    task_id="mkdir",
    python_callable=_mkdir_path,
    op_args=[
        DIR_PATH
    ],
    dag=dag,
)

get_data = PythonOperator(
    task_id="get_data",
    python_callable=_get_data,
    op_args=[
        "{{data_interval_start.year}}",
        "{{data_interval_start.month}}",
        "{{data_interval_start.day}}",
        "{{data_interval_start.hour}}",
    ],
    dag=dag,
)

mkdir_path >> get_data

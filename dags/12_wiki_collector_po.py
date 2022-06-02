import airflow.utils.dates as dates
from airflow import DAG
# from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from urllib import request

DIR_PATH="/opt/airflow/igkim/wiki"

dag=DAG(
    dag_id="12_wiki_collector_po",
    start_date=dates.days_ago(1),
    schedule_interval="@hourly",
    # catchup=False,
    tags=['igkim', 'test'],
)

def _get_data(execution_date):
    year, month, day, hour, *_=execution_date.timetuple()
    url=(
        "https://dumps.wikimedia.org/other/pageviews/"
        f"{year}/{year}-{month}"
        "pageviews-{{execution_date.strftime('%Y%m%d-%H')}}0000.gz"
    )
    request.urlretrieve(url, DIR_PATH)


get_data=PythonOperator(
    task_id="get_data",
    python_callable=_get_data,
    dag=dag,
)




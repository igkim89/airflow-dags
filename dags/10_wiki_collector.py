import airflow.utils.dates as dates
from airflow import DAG
from airflow.operators.bash import BashOperator

DIR_PATH="/opt/airflow/igkim/wiki"

dag=DAG(
    dag_id="10_wiki_collector",
    start_date=dates.days_ago(3),
    schedule_interval="@hourly",
    # catchup=False,
    tags=['igkim', 'test'],
)

get_data=BashOperator(
    task_id="get_data",
    bash_command=(
        f"curl -o {DIR_PATH}/wikipageviews-"
        "{{ execution_date.strftime('%Y%m%d-%H') }}.gz "
        "https://dumps.wikimedia.org/other/pageviews/"
        "{{ execution_date.year }}/"
        "{{ execution_date.year }}-"
        "{{ '{:02}'.format(execution_date.month) }}/"
        "pageviews-{{ execution_date.strftime('%Y%m%d-%H') }}0000.gz"
    ),
    dag=dag,
)

get_data
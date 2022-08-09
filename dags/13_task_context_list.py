import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator

dag = DAG(
    dag_id="13_task_context_list",
    start_date=pendulum.today('Asia/Seoul').add(days=-3),
    schedule_interval="@daily",
    catchup=True,
    tags=['igkim', 'test'],
)


def _print_context(**kwargs):
    print(kwargs)


print_context = PythonOperator(
    task_id="print_context",
    python_callable=_print_context,
    dag=dag,
)

print_context
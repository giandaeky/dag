from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def print_hello():
    return 'Hello from Airflow!'

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 1, 1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG('simple_git_sync_test',
          default_args=default_args,
          description='A simple DAG for testing Git synchronization',
          schedule_interval='@once',
          catchup=False)

task_hello = PythonOperator(
    task_id='hello_task',
    python_callable=print_hello,
    dag=dag,
)

task_hello

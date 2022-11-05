
from airflow import DAG
from airflow.decorators import task, dag
from airflow.utils.dates import days_ago
from airflow.utils.task_group import TaskGroup

default_args = {'start_date': days_ago(1)}


@task
def hello_task():
    print('hello world')
    return 'hello world'

@dag(schedule_interval='@once', default_args=default_args, catchup=False)
def hello_world():
    data = hello_task()

dag = hello_world()


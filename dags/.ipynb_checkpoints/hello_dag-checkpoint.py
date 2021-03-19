from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def hello():
    return 'Hello world!'

hello_dag = DAG('hello_world', start_date=datetime.now())

hello_task = PythonOperator(task_id='hello_task', python_callable=hello, dag=hello_dag)


from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

from datetime import datetime

# Define a function for the first task (_t1)
def _t1(ti):
    # Push a value (42) to XCom with the key 'my_key'
    ti.xcom_push(key="my_key", value=42)

# Define a function for the second task (_t2)
def _t2(ti):
    # Pull the value stored in XCom with the key 'my_key' from the first task (_t1)
    value_from_xcom = ti.xcom_pull(key='my_key', task_id='t1')
    print(f"Value from XCom in task t2: {value_from_xcom}")

# Define the main DAG named 'xcom_dag'
with DAG('xcom_dag', start_date=datetime(2023, 1, 1), schedule_interval='@daily', catchup=False) as dag:

    # Task 1: PythonOperator to execute the _t1 function
    t1 = PythonOperator(
        task_id='t1',
        python_callable=_t1
    )

    # Task 2: PythonOperator to execute the _t2 function
    t2 = PythonOperator(
        task_id='t2',
        python_callable=_t2
    )

    # Set task dependencies to create the execution flow
    t1 >> t2
